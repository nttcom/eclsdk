"""
Exception definitions for Provider Connectivity
"""
import json
from ecl import exceptions


class HttpException(exceptions.HttpException):
    api_error_key = 'cause'


class NotFoundException(HttpException):
    pass
