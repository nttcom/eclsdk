rca
===

Usage::

    import ecl

    conn = ecl.connection.Connection(
        auth_url="https://keystone-<region>-ecl.api.ntt.com/v3/",
        project_id="Tenant ID",
        username="API Key",
        password="API Secret Key",
        user_domain_id="default",
        project_domain_id="default")

    user = conn.rca.get_user("<username>")
    print user.name

You can use methods corresponding to API like ``conn.rca.<method>``

Please refer to ``rca methods`` below to check available methods.

.. toctree::

    ecl.rca.v1
