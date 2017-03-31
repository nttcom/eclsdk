network
=======

Usage::

    import ecl

    conn = ecl.connection.Connection(
        auth_url="https://keystone-<region>-ecl.api.ntt.com/v3/",
        project_id="Tenant ID",
        username="API Key",
        password="API Secret Key",
        user_domain_id="default",
        project_domain_id="default")

    network = conn.network.get_network("<network_id>")
    print network.name

You can use methods corresponding to API like ``conn.network.<method>``

Please refer to ``network methods`` below to check available methods.

.. toctree::

    ecl.network.v2
