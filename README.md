# FastAPI Todo API

A simple Todo API built with FastAPI.

## Features

- Create Todo
- Read Todos
- Update Todo
- Delete Todo

## Requirements

- Python 3.11+
- FastAPI
- Uvicorn

## Installation

```bash
git clone <your-repository-url>
cd <repository-name>
pip install -r requirements.txt
```

## Run the project

```bash
uvicorn main:app --reload
```

## API Documentation

Open:

http://127.0.0.1:8000/docs

## Endpoints

- GET /todos
- GET /todos/{id}
- POST /todos
- PUT /todos/{id}
- DELETE /todos/{id}
