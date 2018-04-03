"""
Exception definitions for Virtual Network Appliance
"""
import json
from ecl import exceptions


class HttpException(exceptions.HttpException):

    def _get_exception_message(self, message=None):
        try:
            content = json.loads(self.response._content)

            # API-GW
            if 'fault' in content and 'faultstring' in content['fault']:
                return content['fault']['faultstring']

            # IAM error case.
            if content.get('errorMessage'):
                return content[self.api_error_key]

            # In VNA API, we need to handle both "cause" and "message" key
            # as API error.
            k = content.keys()
            if 'message' in k and 'cause' not in k:
                return content['message']
            if 'cause' in k and 'message' not in k:
                return content['cause']
        except:
            pass

        if message:
            return message

        # In case parse failed.
        return 'Unknown Exception'


class NotFoundException(HttpException):
    pass
