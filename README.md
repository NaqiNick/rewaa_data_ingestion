
# Rewaa Data Ingestion

A microservice API for handling sensor data.


## API Reference

#### Post sensor data

```http
  POST /sensor-data-ingestion/post/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `sensor_id` | `integer` | **Required**. |
| `value` | `any` | **Required**. |

Adds sensor data to the database.


## Installation

1- Clone the git repository

```bash
  git clone <repo>
```
2- Build Docker Image
```bash
  docker build -t rewaa_ingestion_api -f D:\Naqi\projects\python\rewaa_ingestion_api\rewaa_ingestion_api\Dockerfile .
```
3- Run docker compose
```bash
  docker-compose up
```

The docker containers for this project will be up and running and the apis will be available on the following url
```bash
  http://localhost:8000
```
