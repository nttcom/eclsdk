security_portal
===============

Usage::

    import ecl

    conn = ecl.connection.Connection(
        auth_url="https://keystone-<region>-ecl.api.ntt.com/v3/",
        project_id="Tenant ID",
        username="API Key",
        password="API Secret Key",
        user_domain_id="default",
        project_domain_id="default")

    devices = conn.security_portal.security_devices()
    print devices

You can use methods corresponding to API like ``conn.security_portal.<method>``

Please refer to ``security_portal methods`` below to check available methods.

.. toctree::

    ecl.security_portal.v1
