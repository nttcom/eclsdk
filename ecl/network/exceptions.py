"""
Exception definitions for Network service.
"""
import json
from ecl import exceptions


class HttpException(exceptions.HttpException):
    api_error_key = 'error'


class NotFoundException(HttpException):
    pass
