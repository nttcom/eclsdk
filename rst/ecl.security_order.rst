security_order
==============

Usage::

    import ecl

    conn = ecl.connection.Connection(
        auth_url="https://keystone-<region>-ecl.api.ntt.com/v3/",
        project_id="Tenant ID",
        username="API Key",
        password="API Secret Key",
        user_domain_id="default",
        project_domain_id="default")

    result = conn.security_order.devices()
    print result.devices

You can use methods corresponding to API like ``conn.security_order.<method>``

Please refer to ``security_order methods`` below to check available methods.

.. toctree::

    ecl.security_order.v1
