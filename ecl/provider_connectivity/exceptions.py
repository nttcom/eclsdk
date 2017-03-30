"""
Exception definitions for Provider Connectivity
"""
import json
from ecl import exceptions


class HttpException(exceptions.HttpException):
    pass


class NotFoundException(HttpException):
    pass
