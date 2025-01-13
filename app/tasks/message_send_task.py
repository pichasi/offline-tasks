from celery import Task
from ..celery_app import celery_app

class MessageSendTask(Task):

    name = "Order Integration Webhook Task"
    queue = "New Order Messsages"

    def run(self, *args, **kwargs):

        print(f"Task: {args[0]}, Message: {args[1]}")

MessageSendTask = celery_app.register_task(MessageSendTask())
