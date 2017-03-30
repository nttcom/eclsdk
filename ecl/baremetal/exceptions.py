"""
Exception definitions for Baremetal Server
"""
import json
from ecl import exceptions


class HttpException(exceptions.HttpException):
    pass


class NotFoundException(HttpException):
    pass
