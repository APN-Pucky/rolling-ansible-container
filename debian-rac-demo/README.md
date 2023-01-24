Simple Debian Ansible Rolling Container Example
================================================

Seed with base image, any image with ansible will work:

```
make seed
```

Optionally push the image once
```
make push
```

Now repeatedly build the images on top of each other and adjust the ansible configuration in `./ansible/`

```
make build
```

Once you are happy with the results you can squash/flatten the image (typical `COPY / /`)
```
make publish
```

Since the `COPY` operation is quite slow you can also publish the many debugging layers through:
```
make push
```