ARG IMAGE
FROM ${IMAGE} as build
COPY ansible /ansible/
RUN ansible-playbook -i localhost, --connection=local  /ansible/site.yaml && rm -r /ansible 

# Flatten/Squash the image
# This is more efficient than running a fresh init + build for source based images
FROM scratch as publish
COPY --from=build / /
