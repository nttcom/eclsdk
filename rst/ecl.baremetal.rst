baremetal
=========

Usage::

    import ecl

    conn = ecl.connection.Connection(
        auth_url="https://keystone-<region>-ecl.api.ntt.com/v3/",
        project_id="Tenant ID",
        username="API Key",
        password="API Secret Key",
        user_domain_id="default",
        project_domain_id="default")

    server = conn.baremetal.get_server("<server_id>")
    print server.name

You can use methods corresponding to API like ``conn.baremetal.<method>``

Please refer to ``baremetal methods`` below to check available methods.

.. toctree::

    ecl.baremetal.v2
