Enterprise Cloud 2.0 Python SDK
================================

The ``eclsdk`` is a collection of libraries for building
applications to work with Enterprise Cloud 2.0.

Usage
-----

The following example simply connects to an Enterprise Cloud 2.0.::

    import ecl

    conn = ecl.connection.Connection(
        auth_url="http://ecl:5000/v3/",
        project_id="Tenant ID",
        username="API Key",
        password="API Secret Key",
        user_domain_id="default",
        project_domain_id="default")

    vols = conn.block_store.volumes()
    for vol in vols:
        print vol.name


Token can be used instead of username/password using auth_plugin='token'::

    import ecl

    conn = ecl.connection.Connection(
        auth_plugin='token'
        token='my-fancy-token1234'
        auth_url="http://ecl:5000/v3/",
        project_id="Tenant ID")

    vols = conn.block_store.volumes()
    for vol in vols:
        print vol.name


Documentation
-------------

Documentation is available at
https://ecl.ntt.com

License
-------

Apache 2.0
