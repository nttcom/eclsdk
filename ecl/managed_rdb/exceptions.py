"""
Exception definitions for Managed RDB
"""
import json
from ecl import exceptions


class HttpException(exceptions.HttpException):

    def _get_exception_message(self, message=None):
        try:
            content = json.loads(self.response._content.decode('utf-8'))

            # mRDB error case.
            if content.get('errorCode') and content.get('errorMessage'):
                return '[' + str(content['errorCode']) + '] ' + content['errorMessage']

        except:
            pass

        return super()._get_exception_message(message=message)


class NotFoundException(HttpException):
    pass
