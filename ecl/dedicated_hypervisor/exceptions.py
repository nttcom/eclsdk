"""
Exception definitions for Dedicated Hypervisor
"""
import json
from ecl import exceptions


class HttpException(exceptions.HttpException):

    def _get_exception_message(self, message=None):
        try:
            content = json.loads(self.response._content.decode('utf-8'))

            # vCenter error case.
            key = content.keys()[0]
            return content[key]['message']

        except:
            pass

        return super()._get_exception_message(message=message)


class NotFoundException(HttpException):
    pass
