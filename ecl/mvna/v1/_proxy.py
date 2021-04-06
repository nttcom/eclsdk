from ecl import proxy2
from ecl.mvna.v1 import load_balancer as _load_balancer


class Proxy(proxy2.BaseProxy):

    def load_balancers(self, **params):
        """List Managed Load Balancers."""
        return self._list(_load_balancer.LoadBalancer, paginated=False,
                          **params)

    def create_load_balancer(self, plan_id, interfaces,
                             name=None, description=None, tags=None,
                             default_gateway=None, syslog_servers=None):
        """Create Managed Load Balancer.

        :param string plan_id: Plan ID of Managed Load Balancer
        :param list interfaces: Interface of Managed Load Balancer
        :param string name: Name of Managed Load Balancer
        :param string description: Description of Managed Load Balancer
        :param dict tags: Tags of Managed Load Balancer
        :param string default_gateway: Default Gateway of Managed Load Balancer
        :param list syslog_servers: Syslog Servers of Managed Load Balancer
        :return: Managed Load Balancer
        """
        body = {"plan_id": plan_id, "interfaces": interfaces}
        if name:
            body["name"] = name
        if description:
            body["description"] = description
        if tags:
            body["tags"] = tags
        if default_gateway:
            body["default_gateway"] = default_gateway
        if syslog_servers:
            body["syslog_servers"] = syslog_servers
        return self._create(_load_balancer.LoadBalancer, **body)

    def get_load_balancer(self, load_balancer_id):
        """Retrieve Managed Load Balancer Information.

        :param string load_balancer_id: ID of Managed Load Balancer
        :return: Managed Load Balancer
        """
        return self._get(_load_balancer.LoadBalancer, load_balancer_id)

    def update_load_balancer(self, load_balancer_id,
                             name=None, description=None, tags=None):
        """Update Managed Load Balancer Attributes.

        :param string load_balancer_id: ID of Managed Load Balancer
        :param string name: Name of Managed Load Balancer
        :param string description: Description of Managed Load Balancer
        :param dict tags: Tags of Managed Load Balancer
        :return: Managed Load Balancer
        """
        body = {}
        if name:
            body["name"] = name
        if description:
            body["description"] = description
        if tags:
            body["tags"] = tags
        return self._update(_load_balancer.LoadBalancer, load_balancer_id,
                            **body)

    def delete_load_balancer(self, load_balancer_id, ignore_missing=False):
        """Delete Managed Load Balancer.

        :param string load_balancer_id: ID of Managed Load Balancer
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent resource2.
        :return: None
        """
        self._delete(_load_balancer.LoadBalancer, load_balancer_id,
                     ignore_missing=ignore_missing)

    def action_load_balancer(self, load_balancer_id, **body):
        """Reflect the configuration to Managed Load Balancer.

        :param string load_balancer_id: ID of Managed Load Balancer
        :param dict body: Request Body which want to apply.
        :return: None
        """
        load_balancer = _load_balancer.LoadBalancer()
        load_balancer.action(self.session, load_balancer_id, **body)

    def create_staged_load_balancer_configuration(self,
                                                  load_balancer_id,
                                                  default_gateway=None,
                                                  syslog_servers=None,
                                                  interfaces=None):
        """Create Staged Managed Load Balancer Configuration.

        :param string load_balancer_id: ID of Managed Load Balancer
        :param string default_gateway: Default Gateway of Managed Load Balancer
        :param list syslog_servers: Syslog Servers of Managed Load Balancer
        :param list interfaces: Interface of Managed Load Balancer
        :return: Managed Load Balancer
        """
        body = {}
        if default_gateway:
            body["default_gateway"] = default_gateway
        if syslog_servers:
            body["syslog_servers"] = syslog_servers
        if interfaces:
            body["interfaces"] = interfaces

        load_balancer = _load_balancer.LoadBalancer()
        return load_balancer.create_staged_configuration(self.session,
                                                         load_balancer_id,
                                                         **body)

    def get_staged_load_balancer_configuration(self, load_balancer_id):
        """Retrieve Staged Managed Load Balancer Configuration.

        :param string load_balancer_id: ID of Managed Load Balancer
        :return: Managed Load Balancer
        """
        load_balancer = _load_balancer.LoadBalancer()
        return load_balancer.get_staged_configuration(self.session,
                                                      load_balancer_id)

    def update_staged_load_balancer_configuration(self,
                                                  load_balancer_id,
                                                  default_gateway=None,
                                                  syslog_servers=None,
                                                  interfaces=None):
        """Update Staged Managed Load Balancer Configuration.

        :param string load_balancer_id: ID of Managed Load Balancer
        :param string default_gateway: Default Gateway of Managed Load Balancer
        :param list syslog_servers: Syslog Servers of Managed Load Balancer
        :param list interfaces: Interface of Managed Load Balancer
        :return: Managed Load Balancer
        """
        body = {}
        if default_gateway:
            body["default_gateway"] = default_gateway
        if syslog_servers:
            body["syslog_servers"] = syslog_servers
        if interfaces:
            body["interfaces"] = interfaces

        load_balancer = _load_balancer.LoadBalancer()
        return load_balancer.update_staged_configuration(self.session,
                                                         load_balancer_id,
                                                         **body)

    def cancel_staged_load_balancer_configuration(self, load_balancer_id):
        """Delete Staged Managed Load Balancer Configuration.

        :param string load_balancer_id: ID of Managed Load Balancer
        :return: None
        """
        load_balancer = _load_balancer.LoadBalancer()
        load_balancer.cancel_staged_configuration(self.session,
                                                  load_balancer_id)
