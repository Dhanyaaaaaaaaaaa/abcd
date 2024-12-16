# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.default_api_base import BaseDefaultApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.orders_get200_response_inner import OrdersGet200ResponseInner


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/orders",
    responses={
        200: {"model": List[OrdersGet200ResponseInner], "description": "A list of orders."},
    },
    tags=["default"],
    summary="List all orders",
    response_model_by_alias=True,
)
async def orders_get(
) -> List[OrdersGet200ResponseInner]:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().orders_get()


@router.get(
    "/orders/{orderId}",
    responses={
        200: {"model": OrdersGet200ResponseInner, "description": "Details of an order."},
    },
    tags=["default"],
    summary="Get details of an order",
    response_model_by_alias=True,
)
async def orders_order_id_get(
    orderId: str = Path(..., description=""),
) -> OrdersGet200ResponseInner:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().orders_order_id_get(orderId)
