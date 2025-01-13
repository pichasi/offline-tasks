from celery import Celery


celery_app = Celery('hello', broker='amqp://guest@localhost//')

