image
=====

Usage::

    import ecl

    conn = ecl.connection.Connection(
        auth_url="https://keystone-<region>-ecl.api.ntt.com/v3/",
        project_id="Tenant ID",
        username="API Key",
        password="API Secret Key",
        user_domain_id="default",
        project_domain_id="default")

    image = conn.image.get_image("<image_id>")
    print image.name

You can use methods corresponding to API like ``conn.image.<method>``

Please refer to ``image methods`` below to check available methods.

.. toctree::

    ecl.image.v2
