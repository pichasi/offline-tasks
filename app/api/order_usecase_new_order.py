import uuid

from fastapi import Depends
from fastapi.background import BackgroundTasks

from ..tasks import MessageSendTask, add_celery_task


def send_msg(order_id: str, message: str):

    print(f"Will send message. {order_id}:{message}")


class CreateOrder:

    def __init__(self, background_task: BackgroundTasks):
        self.background_task = background_task

    async def create_order(self):

        order_id = str(uuid.uuid1())
        # send_msg(order_id, "New Order Created")
        self.background_task.add_task(send_msg, order_id, "New Order Created")


class CreateOrderOffline:

    def __init__(self, background_task: BackgroundTasks):
        self.background_task = background_task

    async def create_order(self):

        order_id = str(uuid.uuid1())
        self.background_task.add_task(
            add_celery_task,
            MessageSendTask,
            MessageSendTask.queue,
            (
                order_id,
                "Offline New Order Created",
            ),
        )
