from fastapi.routing import APIRouter
from fastapi import Depends
from .order_usecase_new_order import CreateOrder, CreateOrderOffline

router = APIRouter(prefix="/order")


@router.post("/plain")
async def create_order(usecase: CreateOrder = Depends()):

    await usecase.create_order()


@router.post("/offline")
async def offline_order(usecase: CreateOrderOffline = Depends()):

    await usecase.create_order()
