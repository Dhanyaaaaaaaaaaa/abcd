# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.orders_get200_response_inner import OrdersGet200ResponseInner  # noqa: F401


def test_orders_get(client: TestClient):
    """Test case for orders_get

    List all orders
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/orders",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_orders_order_id_get(client: TestClient):
    """Test case for orders_order_id_get

    Get details of an order
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/orders/{orderId}".format(orderId='order_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

