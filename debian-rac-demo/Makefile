NAME:="apnpucky/debian-rac-demo"
TAG:="$(shell date +%Y%m%d%H%M%S)"

seed:
	docker pull apnpucky/debian-rac:latest
	docker tag  apnpucky/debian-rac:latest ${NAME}:latest

build:
	docker build --target build --tag ${NAME}:latest --build-arg IMAGE=${NAME}:latest .

push: 
	docker tag  ${NAME}:latest ${NAME}:${TAG}
	docker push ${NAME}:latest
	docker push ${NAME}:${TAG}

publish:
	docker build --target publish --tag ${NAME}:latest --build-arg IMAGE=${NAME}:latest .
	docker tag  ${NAME}:latest ${NAME}:${TAG}
	docker push ${NAME}:latest
	docker push ${NAME}:${TAG}