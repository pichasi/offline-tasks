# Asynchronous Tasks

We will use FastAPI, RabbitMQ and Celery to implement offline tasks.

### Run RabbitMQ
```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4.0-management
```

### Run API Server - FastAPI
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Run the Celery Worker - Celery
```bash
celery -A app.tasks.message_send_task worker -Q "New Order Messsages"
```