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
            if content.get('code') and content.get('message'):
                return '[' + str(content['code']) + '] ' + content['message']

        except:
            pass

        return super()._get_exception_message(message=message)


class NotFoundException(HttpException):
    pass
