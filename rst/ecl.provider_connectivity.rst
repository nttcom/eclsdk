provider_connectivity
=====================

Usage::

    import ecl

    conn = ecl.connection.Connection(
        auth_url="https://keystone-<region>-ecl.api.ntt.com/v3/",
        project_id="Tenant ID",
        username="API Key",
        password="API Secret Key",
        user_domain_id="default",
        project_domain_id="default")

    aws_connection = conn.provider_connectivity.get_aws_connection("<connection_id>")
    print aws_connection.name

You can use methods corresponding to API like ``conn.provider_connectivity.<method>``

Please refer to ``provider_connectivity methods`` below to check available methods.

.. toctree::

    ecl.provider_connectivity.v1
