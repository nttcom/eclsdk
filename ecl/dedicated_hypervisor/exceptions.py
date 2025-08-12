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
            key = list(content.keys())[0]
            code = content[key]['code']
            message = content[key]['message']
            return '[' + str(code) + ']' + message

        except:
            pass

        return super()._get_exception_message(message=message)


class NotFoundException(HttpException):
    pass
