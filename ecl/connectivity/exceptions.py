"""
Exception definitions for Interconnectivity.
"""
from ecl import exceptions


class HttpException(exceptions.HttpException):
    api_error_key = 'reason'


class NotFoundException(HttpException):
    pass
