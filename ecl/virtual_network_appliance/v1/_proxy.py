# -*- coding: utf-8 -*-

from ecl.virtual_network_appliance.v1 \
    import virtual_network_appliance as _virtual_network_appliance
from ecl.virtual_network_appliance.v1 \
    import virtual_network_appliance_plan as _virtual_network_appliance_plan
from ecl.virtual_network_appliance.v1 import operation as _operation
from ecl import exceptions
from ecl import proxy2


class Proxy(proxy2.BaseProxy):

    @proxy2._check_resource(strict=False)
    def _get(self, resource_type, value=None, requires_id=True, **params):
        """Get a resource

        :param resource_type: The type of resource to get.
        :type resource_type: :class:`~ecl.resource2.Resource`
        :param value: The value to get. Can be either the ID of a
                      resource or a :class:`~ecl.resource2.Resource`
                      subclass.
        :param dict params: Parameters to be passed onto the
                            :meth:`~ecl.resource2.Resource.get` method.
                            These are used as query parameters
                            with GET request.
        :returns: The result of the ``get``
        :rtype: :class:`~ecl.resource2.Resource`
        """
        res = self._get_resource(resource_type, value)
        if not res.allow_get:
            raise exceptions.MethodNotSupported(res, "get")

        try:
            request = res._prepare_request(requires_id=requires_id)
            query_params = res._query_mapping._transpose(params)
            response = self.session.get(request.uri,
                                        endpoint_filter=res.service,
                                        params=query_params)
            res._translate_response(response)
            return res
        except exceptions.NotFoundException as e:
            raise exceptions.ResourceNotFound(
                message="No %s found for %s" %
                        (resource_type.__name__, value),
                details=e.details, response=e.response,
                request_id=e.request_id, url=e.url, method=e.method,
                http_status=e.http_status, cause=e.cause)

    def virtual_network_appliance_plans(self, **params):
        """List virtual network appliance plans.

        :param params: The parameters as query string format
            to get network appliance plans.
        :returns: A list of network appliance plans.
        :rtype: list of :class:`~ecl.virtual_network_appliance.v1.
            virtual_network_appliance_plan.VirtualNetworkAppliancePlan`
        """
        return list(self._list(
            _virtual_network_appliance_plan.VirtualNetworkAppliancePlan,
            paginated=False, **params))

    def get_virtual_network_appliance_plan(
            self, virtual_network_appliance_plan_id, **params):
        """Show virtual network appliance plan.

        :param string virtual_network_appliance_plan_id:
            ID of specified virtual network appliance plan.
        :param params: The parameters as query string format
            to get a network appliance plan.
        :return: :class:`~ecl.virtual_network_appliance.v1.
            virtual_network_appliance_plan.VirtualNetworkAppliancePlan`
        """
        return self._get(
            _virtual_network_appliance_plan.VirtualNetworkAppliancePlan,
            virtual_network_appliance_plan_id,
            **params
        )

    def virtual_network_appliances(self, **params):
        """List virtual network appliances.

        :param params: The parameters as query string format
            to get list of network appliance.
        :returns: A list of network appliance.
        :rtype: list of :class:`~ecl.virtual_network_appliance.v1.
            virtual_network_appliance.VirtualNetworkAppliance`
        """
        return list(self._list(
            _virtual_network_appliance.VirtualNetworkAppliance,
            paginated=False, **params))

    def get_virtual_network_appliance(self, virtual_network_appliance_id):
        """Show virtual network appliance.

        :param string virtual_network_appliance_id:
            ID of specified virtual network appliance.
        :return: :class:`~ecl.virtual_network_appliance.v1.
            virtual_network_appliance.VirtualNetworkAppliance`
        """
        return self._get(_virtual_network_appliance.VirtualNetworkAppliance,
                         virtual_network_appliance_id)

    def update_virtual_network_appliance(self, virtual_network_appliance,
                                         **body):
        """Update a virtual network appliance.

        :param virtual_network_appliance:
            ID of specified virtual network appliance.
        :param :attrs \*\*params: Parameters for updating
            specified virtual network appliance.
        :returns: :class:`~ecl.virtual_network_appliance.
            v1.virtual_network_appliance.VirtualNetworkAppliance`
        """
        return self._update(_virtual_network_appliance.VirtualNetworkAppliance,
                            virtual_network_appliance, **body)

    def find_virtual_network_appliance(self, name_or_id, ignore_missing=False):
        """Find a single virtual network appliance.

        :param name_or_id: The name or ID of a virtual network appliance.
        :param bool ignore_missing: When set to ``False``
            :class:`~ecl.exceptions.ResourceNotFound` will be
            raised when the resource does not exist.
            When set to ``True``, None will be returned when
            attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.virtual_network_appliance.v1.
            virtual_network_appliance.VirtualNetworkAppliance` or None
        """
        return self._find(_virtual_network_appliance.VirtualNetworkAppliance,
                          name_or_id,
                          ignore_missing=ignore_missing)

    def delete_virtual_network_appliance(self, virtual_network_appliance_id,
                                         ignore_missing=False):
        """Delete virtual network appliance.

        :param virtual_network_appliance_id:
            The ID of a virtual network appliance.
        :param bool ignore_missing: When set to ``False``
            :class:`~ecl.exceptions.ResourceNotFound` will be
            raised when the port does not exist.
            When set to ``True``, no exception will be set when
            attempting to delete a nonexistent port.
        :returns: ``None``
        """
        self._delete(_virtual_network_appliance.VirtualNetworkAppliance,
                     virtual_network_appliance_id,
                     ignore_missing=ignore_missing)

    def create_virtual_network_appliance(
            self,
            virtual_network_appliance_plan_id,
            interfaces,
            name=None,
            description=None,
            tags=None,
            default_gateway=None,
            availability_zone=None):
        """Create virtual network appliance.

        :param string virtual_network_appliance_plan_id:
            Plan ID for virtual network appliance.
        :param dict interfaces: Interface definition dictionary.
        :param string name: Name of virtual network appliance.
        :param string description: Description of virtual network appliance.
        :param dict tags: Tags of virtual network appliance.
        :param string default_gateway: Default gateway address for
            virtual network appliance.
        :param string availability_zone: Availability Zone
            for virtual network appliance.
        :returns: :class:`~ecl.virtual_network_appliance.v1.
            virtual_network_appliance.VirtualNetworkAppliance`
        """
        body = {}
        body["virtual_network_appliance_plan_id"] = \
            virtual_network_appliance_plan_id
        body["interfaces"] = interfaces
        if name:
            body["name"] = name
        if description:
            body["description"] = description
        if tags:
            body["tags"] = tags
        if default_gateway:
            body["default_gateway"] = default_gateway
        if availability_zone:
            body["availability_zone"] = availability_zone
        return self._create(_virtual_network_appliance.VirtualNetworkAppliance,
                            **body)

    def start_virtual_network_appliance(self, virtual_network_appliance):
        """Start the virtual network appliance.

        :param virtual_network_appliance:
            The ID of a virtual network appliance.
        :return: <Response 200>
        """
        virtual_network_appliance = \
            self.get_virtual_network_appliance(virtual_network_appliance)
        return virtual_network_appliance.start(self.session)

    def get_virtual_network_appliance_console(self,
                                              virtual_network_appliance,
                                              vnc_type):
        """Get console information for the virtual network appliance.

        :param virtual_network_appliance: Either the ID of a server or a
            :class:`~ecl.virtual_network_appliance.v1.
            virtual_network_appliance.VirtualNetworkAppliance` instance.
        :param vnc_type: should be `~string "novnc"`
        :return: <Response 200>
        """
        virtual_network_appliance = \
            self.get_virtual_network_appliance(virtual_network_appliance)
        return virtual_network_appliance.get_console(self.session, vnc_type)

    def stop_virtual_network_appliance(self, virtual_network_appliance):
        """Stop the virtual network appliance.

        :param virtual_network_appliance:
            The ID of a virtual network appliance.
        :return: <Response 200>
        """
        virtual_network_appliance = \
            self.get_virtual_network_appliance(virtual_network_appliance)
        return virtual_network_appliance.stop(self.session)

    def restart_virtual_network_appliance(self, virtual_network_appliance):
        """Restart the virtual network appliance.

        :param virtual_network_appliance:
            The ID of a virtual network appliance.
        :return: <Response 200>
        """
        virtual_network_appliance = \
            self.get_virtual_network_appliance(virtual_network_appliance)
        return virtual_network_appliance.restart(self.session)

    def reset_password_virtual_network_appliance(self,
                                                 virtual_network_appliance):
        """Reset the password of virtual network appliance.

        :param virtual_network_appliance:
            The ID of a virtual network appliance.
        :return: <Response 200>
        """
        virtual_network_appliance = \
            self.get_virtual_network_appliance(virtual_network_appliance)
        return virtual_network_appliance.reset_password(self.session)

    def operations(self, resource_ids=[], no_deleted=True, latest=False):
        """List operations.

        :param resource_ids: The list of resouce(appliance) IDs.
            If user specify this parameter,
            operations that has resource_id attribute is included in
            this list will be returned.
        :param bool no_deleted:
            ``True`` You can get operations for only existing resources.
            ``False`` You can get operations for all resources even removed.
        :param bool latest:
            ``True`` You can get only the latest operations for each resource.
            ``False`` You can get all of operations for each resource.
        :returns: A list of operation objects
        :rtype: list of :class:`~ecl.virtual_network_appliance.v1.
            operation.Operation`
        """
        return list(self._list(_operation.Operation, paginated=False,
                               resource_ids=resource_ids,
                               no_deleted=no_deleted,
                               latest=latest))

    def get_operation(
            self, operation_id):
        """Show operation.

        :param string operation_id: ID of specified operation.
        :return: :class:`~ecl.virtual_network_appliance.v1.
            operation.Operation`
        """
        return self._get(_operation.Operation, operation_id)

    def find_virtual_network_appliance_plan(self, name_or_id,
                                            ignore_missing=False):
        """Find a single virtual network appliance plan.

        :param name_or_id: The name or ID of a virtual network appliance plan.
        :param bool ignore_missing: When set to ``False``
            :class:`~ecl.exceptions.ResourceNotFound` will be
            raised when the resource does not exist.
            When set to ``True``, None will be returned when
            attempting to find a nonexistent resource.
        :returns: One :class:`~ecl.virtual_network_appliance.v1.
            virtual_network_appliance_plan.VirtualNetworkAppliancePlan`
            or None
        """
        return self._find(
            _virtual_network_appliance_plan.VirtualNetworkAppliancePlan,
            name_or_id,
            ignore_missing=ignore_missing)
