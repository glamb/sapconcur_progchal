Gregg Lamb SAP Concur Programming challenge.

## Introduction

A simple flask microservice that response to a single POST request. The Post request accept a payload with the following structure:

{"input": "This is the text of the email"}

It should then return the output of the model prediction in json as well:

{"output": "HAM"}

The microservice is containerized within a Docker container and cna be ran using docker-compose.



## Testing

Unit test are written in Pythons built in unit testing package.

Steps to run unit test:
* First install the required package
    * pip install -r requirements.txt
* Then run test via Python command
    * python -m unittest test.py

## Docker

I ended up using docker-compose to simplify application installation.

To run the application in a self hosted container run the following commands.

    docker-compose build
    docker-compose up

## Usage

Once the application is running in Docker a suer can perform curl requests against the server.

Right now there is only a single endpoint.

curl -d '{"input":"You have been hacked. Call 1-800-unlock-me for help. This is totally not spam."}' -H "Content-Type: application/json" -X POST http://localhost:5000/api/load

curl -d '{"input":"this should be ham"}' -H "Content-Type: application/json" -X POST http://localhost:5000/api/load

## Takeaway

* I wanted to add more test to validate response, but I believe I need to mock the joblib and the predict method.

* I would clean up the error reporting in the app. Create a single method or class that would be the error response handler.

* Scikit is a new package to me and I accidently went down that rabbit hole.



