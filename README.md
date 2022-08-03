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