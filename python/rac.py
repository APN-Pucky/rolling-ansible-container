import argparse
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(
        prog="RAC", description="rolling ansible container", epilog="Enjoy"
    )

    parser.add_argument(
        "-i",
        "--image",
        required=True,
        help="Image to pull",
    )

    parser.add_argument(
        "-r",
        "--role",
        help="Role to run",
    )

    parser.add_argument(
        "-pb",
        "--playbook",
        help="Role to run",
    )

    parser.add_argument(
        "-d",
        "--dir",
        default="ansible",
        help="directory with roles",
    )

    parser.add_argument(
        "-s",
        "--seed",
        help="start with a fresh base seed image",
    )

    parser.add_argument(
        "-f",
        "--flatten",
        default=False,
        action="store_true",
    )

    parser.add_argument(
        "-p",
        "--push",
        default=False,
        action="store_true",
    )

    args = parser.parse_args()

    dockerfile = ""

    if args.seed:
         dockerfile += f"""
FROM {args.seed} as build
ADD https://raw.githubusercontent.com/APN-Pucky/rolling-ansible-container/master/bootstrap-rac.sh /bootstrap-rac.sh
RUN chmod +x /bootstrap-rac.sh && /bootstrap-rac.sh && rm /bootstrap-rac.sh 
            """
    else:
        # Check if image exists
        p = subprocess.run(["docker", "image", "inspect", args.image])
        if p.returncode != 0:
            # Pull it
            p = subprocess.run(["docker", "pull", args.image])
            if p.returncode != 0:
                print (f"Could not find {args.image}")
                exit(1)
        dockerfile += f"""FROM {args.image} as build"""

    dockerfile += f"""
COPY { args.dir } /ansible/
    """

    if args.role:
        dockerfile += f"""
RUN . ansible-env/bin/activate && cd ansible && ansible localhost --connection=local  --module-name include_role --args name={ args.role } && cd .. && rm -r /ansible 
        """

    if args.playbook:
        dockerfile += f"""
RUN . ansible-env/bin/activate && cd ansible && ansible-playbook -i localhost, --connection=local { args.playbook } && cd .. && rm -r /ansible 
        """

    if args.flatten:
        dockerfile += f"""
RUN rm -rf ansible-env
FROM scratch
COPY --from=build / /
        """

    # Write the dockerfile to a temporary file and build the image
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write(dockerfile)
        f.flush()
        print(dockerfile)
        subprocess.run(["docker", "build", "--tag", args.image, "-f", f.name, "."])

    if args.push:
        subprocess.run(["docker", "push", args.image])

    print("All done")

if __name__ == "__main__":
    main()
