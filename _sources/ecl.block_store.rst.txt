block_store
===========

Usage::

    import ecl

    conn = ecl.connection.Connection(
        auth_url="https://keystone-<region>-ecl.api.ntt.com/v3/",
        project_id="Tenant ID",
        username="API Key",
        password="API Secret Key",
        user_domain_id="default",
        project_domain_id="default")

    volume = conn.block_store.get_volume("<volume_id>")
    print volume.name

You can use methods corresponding to API like ``conn.block_store.<method>``

Please refer to ``block_store methods`` below to check available methods.

.. toctree::

    ecl.block_store.v2
