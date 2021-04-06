from ecl import proxy2
from ecl.mvna.v1 import certificate as _certificate
from ecl.mvna.v1 import load_balancer as _load_balancer
from ecl.mvna.v1 import target_group as _target_group


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
                    attempting to delete a nonexistent load balancer.
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

    def target_groups(self, **params):
        """List Target Groups."""
        return self._list(_target_group.TargetGroup, paginated=False, **params)

    def create_target_group(self, default_port, load_balancer_id, members,
                            name=None, description=None, tags=None):
        """Create Target Group.

        :param string default_port: Default Port of Target Group
        :param string load_balancer_id: Load Balancer ID of Target Group
        :param string members: Members of Target Group
        :param string name: Name of Target Group
        :param string description: Description of Target Group
        :param dict tags: Tags of Target Group
        :return: Target Group
        """
        body = {
            'default_port': default_port,
            'load_balancer_id': load_balancer_id,
            'members': members
        }
        if name:
            body["name"] = name
        if description:
            body["description"] = description
        if tags:
            body["tags"] = tags
        return self._create(_target_group.TargetGroup, **body)

    def get_target_group(self, target_group_id):
        """Retrieve Target Group Information.

        :param string target_group_id: ID of Target Group
        :return: Target Group
        """
        return self._get(_target_group.TargetGroup, target_group_id)

    def update_target_group(self, target_group_id,
                            name=None, description=None, tags=None):
        """Update Target Group Attributes.

        :param string target_group_id: ID of Target Group
        :param string name: Name of Target Group
        :param string description: Description of Target Group
        :param dict tags: Tags of Target Group
        :return: Target Group
        """
        body = {}
        if name:
            body["name"] = name
        if description:
            body["description"] = description
        if tags:
            body["tags"] = tags
        return self._update(_target_group.TargetGroup, target_group_id, **body)

    def delete_target_group(self, target_group_id, ignore_missing=False):
        """Delete Target Group.

        :param string target_group_id: ID of Target Group
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent target group.
        :return: None
        """
        self._delete(_target_group.TargetGroup, target_group_id,
                     ignore_missing=ignore_missing)

    def create_staged_target_group_configuration(
            self, target_group_id, members=None, default_port=None):
        """Create Staged Target Group Configuration.

        :param string target_group_id: ID of Target Group
        :param string members: Members of Target Group
        :param string default_port: Default Port of Target Group
        :return: Target Group
        """
        body = {}
        if members:
            body["members"] = members
        if default_port:
            body["default_port"] = default_port

        target_group = _target_group.TargetGroup()
        return target_group.create_staged_configuration(self.session,
                                                        target_group_id,
                                                        **body)

    def get_staged_target_group_configuration(self, target_group_id):
        """Retrieve Staged Target Group Configuration.

        :param string target_group_id: ID of Target Group
        :return: Target Group
        """
        target_group = _target_group.TargetGroup()
        return target_group.get_staged_configuration(self.session,
                                                     target_group_id)

    def update_staged_target_group_configuration(
            self, target_group_id, members=None, default_port=None):
        """Update Staged Target Group Configuration.

        :param string target_group_id: ID of Target Group
        :param string members: Members of Target Group
        :param string default_port: Default Port of Target Group
        :return: Target Group
        """
        body = {}
        if members:
            body["members"] = members
        if default_port:
            body["default_port"] = default_port

        target_group = _target_group.TargetGroup()
        return target_group.update_staged_configuration(self.session,
                                                        target_group_id,
                                                        **body)

    def cancel_staged_target_group_configuration(self, target_group_id):
        """Delete Staged Target Group Configuration.

        :param string target_group_id: ID of Target Group
        :return: None
        """
        target_group = _target_group.TargetGroup()
        target_group.cancel_staged_configuration(self.session, target_group_id)

    def certificates(self, **params):
        """List Certificates."""
        return self._list(_certificate.Certificate, paginated=False,
                          **params)

    def create_certificate(self, name=None, description=None, tags=None):
        """Create Certificate.

        :param string name: Name of Certificate
        :param string description: Description of Certificate
        :param string tags: Tags of Certificate
        :return: Certificate
        """
        body = {}
        if name:
            body["name"] = name
        if description:
            body["description"] = description
        if tags:
            body["tags"] = tags
        return self._create(_certificate.Certificate, **body)

    def get_certificate(self, certificate_id):
        """Retrieve Certificate Information.

        :param string certificate_id: ID of Certificate
        :return: Certificate
        """
        return self._get(_certificate.Certificate, certificate_id)

    def update_certificate(self, certificate_id,
                           name=None, description=None, tags=None):
        """Update Certificate Attributes.

        :param string certificate_id: ID of Certificate
        :param string name: Name of Certificate
        :param string description: Description of Certificate
        :param dict tags: Tags of Certificate
        :return: Certificate
        """
        body = {}
        if name:
            body["name"] = name
        if description:
            body["description"] = description
        if tags:
            body["tags"] = tags
        return self._update(_certificate.Certificate, certificate_id,
                            **body)

    def delete_certificate(self, certificate_id, ignore_missing=False):
        """Delete Certificate.

        :param string certificate_id: ID of Certificate
        :param bool ignore_missing: When set to ``False``
                    :class:`~ecl.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent certificate.
        :return: None
        """
        self._delete(_certificate.Certificate, certificate_id,
                     ignore_missing=ignore_missing)

    def upload_certificate(self,
                           certificate_id, certificate_type, certificate_file):
        """Upload the Certificate.

        :param string certificate_id: ID of Certificate
        :param string certificate_type: Type of Certificate
        :param string certificate_file: File of Certificate
        :return: None
        """
        body = {'type': certificate_type, 'file': certificate_file}
        certificate = _certificate.Certificate()
        certificate.upload(self.session, certificate_id, **body)