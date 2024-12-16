# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.orders_get200_response_inner import OrdersGet200ResponseInner


class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    async def orders_get(
        self,
    ) -> List[OrdersGet200ResponseInner]:
        ...


    async def orders_order_id_get(
        self,
        orderId: str,
    ) -> OrdersGet200ResponseInner:
        ...
