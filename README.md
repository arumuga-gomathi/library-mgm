# library-mgm-cosmocloud

Library management system task for cosmocloud back end intern

This project uses python 3.12, FastAPI, uvicorn, Pymongo and other dependencies required used for deployment.

Used MongoDB Atlas Free tier Database

Deployed using docker container image, uploaded to ECR repository and deployed to lambda function which uses function URL and exposes HTTP API

Function URL: https://mfkanj77xesdcwchdy3b4jctmq0hjtao.lambda-url.ap-south-1.on.aws/students

# steps to deploy

Configure AWS CLI Credentials

Build docker image
- docker build --platform linux/arm64 -t python-fastapi .

Tag Docker image
- docker tag python-fastapi:latest <account_id>.dkr.ecr.ap-south-1.amazonaws.com/python-fastapi:latest

Push Docker image to ECR
- docker push <account_id>.dkr.ecr.ap-south-1.amazonaws.com/python-fastapi:latest

Create a lambda function with container image uploaded to ECR

Enable function URL

Success!!