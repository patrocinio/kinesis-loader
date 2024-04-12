build:
	sam build

deploy: build
	sam deploy

invoke-local:
	aws lambda invoke --endpoint http://localhost:3001 --function-name RepeaterFunction out.txt
	
start-local: build
	DOCKER_HOST=unix://${HOME}/.docker/run/docker.sock sam local start-lambda
