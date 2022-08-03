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
| `GET`    | `/api/`                             | Retrieve all messages.                      |
| `GET`   | `/api/item`                             | Single item detail                     |