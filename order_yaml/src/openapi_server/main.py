# coding: utf-8

"""
    Orders API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from fastapi import FastAPI

from openapi_server.apis.default_api import router as DefaultApiRouter

app = FastAPI(
    title="Orders API",
    description="No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)",
    version="1.0",
)

app.include_router(DefaultApiRouter)
