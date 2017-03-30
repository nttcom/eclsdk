"""
Exception definitions for Remote Console Access.
"""
import json
from ecl import exceptions


class HttpException(exceptions.HttpException):
    pass


class NotFoundException(HttpException):
    pass
