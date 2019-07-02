# -*- coding: utf-8 -*-

from . import base
from ecl import resource2
from ecl.network import network_service


class LoadBalancerSyslogServer(base.NetworkBaseResource):

    resources_key = "load_balancer_syslog_servers"
    resource_key = "load_balancer_syslog_server"
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + "/load_balancer_syslog_servers"

    _query_mapping = resource2.QueryParameters(
        "acl_logging", "appflow_logging", "date_format",
        "description", "id", "ip_address", "load_balancer_id",
        "log_facility", "log_level", "name", "port_number",
        "priority", "status", "tcp_logging", "tenant_id",
        "time_zone", "transport_type", "user_configurable_log_messages",
        "sort_key", "sort_dir",
    )
    # Capabilities
    allow_list = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_create = True

    # Properties
    acl_logging = resource2.Body("acl_logging")

    appflow_logging = resource2.Body("appflow_logging")

    date_format = resource2.Body("date_format")

    #: Description of the Load Balancer Syslog Server.
    description = resource2.Body("description")

    #: Unique ID of the Load Balancer Syslog Server.
    id = resource2.Body("id")

    #: IP Address
    ip_address = resource2.Body("ip_address")

    #: The ID of load_balancer this load_balancer_interface belongs to.
    load_balancer_id = resource2.Body("load_balancer_id")

    log_facility = resource2.Body("log_facility")

    log_level = resource2.Body("log_level")

    #: Name of the Load Balancer
    name = resource2.Body("name")

    #: Port Number
    port_number = resource2.Body("port_number")

    #: Priority
    priority = resource2.Body("priority")

    #: The load_balancer Syslog Server status.
    status = resource2.Body("status")

    tcp_logging = resource2.Body("tcp_logging")

    #: Tenant ID of the owner (UUID)
    tenant_id = resource2.Body("tenant_id")

    #: Timezone
    time_zone = resource2.Body("time_zone")

    transport_type = resource2.Body("transport_type")

    user_configurable_log_messages = resource2.Body(
                    "user_configurable_log_messages")
