dedicated_hypervisor
====================

Usage::

    import ecl

    conn = ecl.connection.Connection(
        auth_url="https://keystone-<region>-ecl.api.ntt.com/v3/",
        project_id="Tenant ID",
        username="API Key",
        password="API Secret Key",
        user_domain_id="default",
        project_domain_id="default")

    server = conn.dedicated_hypervisor.get_server("<server_id>")
    print server.name

You can use methods corresponding to API like ``conn.dedicated_hypervisor.<method>``

Please refer to ``dedicated_hypervisor methods`` below to check available methods.

.. toctree::

    ecl.dedicated_hypervisor.v1
