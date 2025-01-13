import uuid


def add_celery_task(task, queue, args):

    task_id = str(uuid.uuid1())

    result = task.apply_async(args, queue=queue, task_id=task_id)

    return result