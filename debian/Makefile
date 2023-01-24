NAME:="debian-rac-demo"
TAG:="$(shell date +%Y%m%d%H%M%S)"
init: 
	docker build --tag ${NAME}:latest --build-arg IMAGE=debian .
build:
	docker build --tag ${NAME}:latest .
push: build
	docker tag ${NAME}:latest apnpucky/${NAME}:${TAG}
	docker push apnpucky/debian-rac-demo:${TAG}