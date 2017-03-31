connectivity
============

Usage::

    import ecl

    conn = ecl.connection.Connection(
        auth_url="https://keystone-<region>-ecl.api.ntt.com/v3/",
        project_id="Tenant ID",
        username="API Key",
        password="API Secret Key",
        user_domain_id="default",
        project_domain_id="default")

    cic = conn.connectivity.get_cic("<mcic_id>", "<cic_id>")
    print cic.cic_name

You can use methods corresponding to API like ``conn.connectivity.<method>``

Please refer to ``connectivity methods`` below to check available methods.

.. toctree::

    ecl.connectivity.v1
