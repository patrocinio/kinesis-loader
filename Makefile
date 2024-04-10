build:
	sam build

deploy: build
	sam deploy

invoke-local:
	aws lambda invoke --endpoint http://localhost:3001 --function-name RepeaterFunction out.txt
	
start-local: build
	sam local start-lambda
