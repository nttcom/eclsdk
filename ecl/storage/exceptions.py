"""
Exception definitions for Network service.
"""
import json
from ecl import exceptions


class HttpException(exceptions.HttpException):
    api_error_key = 'api_error_message'


class NotFoundException(HttpException):
    pass
