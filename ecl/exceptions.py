# Copyright 2010 Jacob Kaplan-Moss
# Copyright 2011 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
"""
Exception definitions.
"""

import six
import json


class SDKException(Exception):
    """The base exception class for all exceptions this library raises."""
    def __init__(self, message=None, cause=None):
        self.message = self.__class__.__name__ if message is None else message
        self.cause = cause
        super(SDKException, self).__init__(self.message)


class EndpointNotFound(SDKException):
    """A mismatch occurred between what the client and server expect."""
    def __init__(self, message=None):
        super(EndpointNotFound, self).__init__(message)


class InvalidResponse(SDKException):
    """The response from the server is not valid for this request."""

    def __init__(self, response):
        super(InvalidResponse, self).__init__()
        self.response = response


class InvalidRequest(SDKException):
    """The request to the server is not valid."""

    def __init__(self, message=None):
        super(InvalidRequest, self).__init__(message)


class HttpException(SDKException):

    def __init__(self, message=None, details=None, response=None,
                 request_id=None, url=None, method=None,
                 http_status=None, cause=None):
        super(HttpException, self).__init__(message=message, cause=cause)
        self.details = details
        self.response = response
        self.request_id = request_id
        self.url = url
        self.method = method
        self.http_status = http_status
        if self.response is not None:
            self.message = self._get_exception_message(message=self.message)

    def _is_compute_form_error(self, content):
        try:
            if 'message' in content.items()[0][1]:
                return True
        except:
            return False

    def _get_exception_message(self, message=None):
        try:
            content = json.loads(self.response._content.decode('utf-8'))

            if self._is_compute_form_error(content):
                return content.items()[0][1]['message']

            # API-GW
            if 'fault' in content and 'faultstring' in content['fault']:
                return content['fault']['faultstring']

            # IAM error case.
            if content.get('errorMessage'):
                return content[self.api_error_key]

            # Function specific case.
            if hasattr(self, 'api_error_key') \
                    and content.get(self.api_error_key):
                return content[self.api_error_key]

            # Default case.
            if content.get('message'):
                return content['message']
        except:
            pass

        if message:
            return message

        # In case parse failed.
        return 'Unknown Exception'

    def __unicode__(self):
        msg = self.__class__.__name__ + ": " + self.message
        if self.details:
            msg += ", " + six.text_type(self.details)
        return msg

    def __str__(self):
        return self.__unicode__()


class NotFoundException(HttpException):
    """HTTP 404 Not Found."""
    pass


class MethodNotSupported(SDKException):
    """The resource does not support this operation type."""
    def __init__(self, resource, method):
        # This needs to work with both classes and instances.
        try:
            name = resource.__name__
        except AttributeError:
            name = resource.__class__.__name__

        message = ('The %s method is not supported for %s.%s' %
                   (method, resource.__module__, name))
        super(MethodNotSupported, self).__init__(message=message)


class DuplicateResource(SDKException):
    """More than one resource exists with that name."""
    pass


class ResourceNotFound(NotFoundException):
    """No resource exists with that name or id."""
    pass


class ResourceTimeout(SDKException):
    """Timeout waiting for resource."""
    pass


class ResourceFailure(SDKException):
    """General resource failure."""
    pass
