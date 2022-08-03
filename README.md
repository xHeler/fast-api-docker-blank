[![fastapi-github-actions-test](https://github.com/xHeler/fast-api-docker-blank/actions/workflows/main.yml/badge.svg)](https://github.com/xHeler/fast-api-docker-blank/actions/workflows/main.yml)

# fast-api
Simple fast-api project including docker.

# Initialize & Run

```shell
docker build -t <image_name> .
docker-compose up -d # start server
docker-compose down # stop server
```

# Endpoints

| Method   | URL                                      | Description                              |
| -------- | ---------------------------------------- | ---------------------------------------- |
| `GET`    | [/api](http://127.0.0.1/api)                             | Retrieve all messages.                      |
| `GET`   | [/api/items/<pk:id>](http://127.0.0.1/api/items/1)                           | Get single item by id                     |


# Deployment
## Setup for heroku deployment:
```
heroku login
heroku create <app-name>
heroku auth:token #generate-auth-token
```
## Set github secrets:
Settings -> Secrets -> Actions -> New Repository Secret

| Repository secret | value |
| -------- | ------------|
| HEROKU_APP_NAME | <YOUR_APP_NAME>| 
| HEROKU_AUTH_TOKEN | [Generated](#generate-auth-token) |