storage
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

    storage = conn.storage.get_storage("<storage_id>")
    print storage.name

You can use methods corresponding to API like ``conn.storage.<method>``

Please refer to ``storage methods`` below to check available methods.

.. toctree::

    ecl.storage.v1
