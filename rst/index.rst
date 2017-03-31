ECL2.0 Python SDK
=========================================

The ``eclsdk`` is a collection of libraries for building
applications to work with Enterprise Cloud 2.0

Install::

    pip install eclsdk

The following example simply connects to an Enterprise Cloud 2.0::

    import ecl

    conn = ecl.connection.Connection(
        auth_url="https://keystone-<region>-ecl.api.ntt.com/v3/",
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
        auth_url="https://keystone-<region>-ecl.api.ntt.com/v3/",
        project_id="Tenant ID")

    vols = conn.block_store.volumes()
    for vol in vols:
        print vol.name

If you want to log the API's REQ and RESP, please write the following code::

    import sys
    from ecl import utils

    utils.enable_logging(debug=True, path='ecl.log', stream=sys.stdout)
    # you may do as follows
    # utils.enable_logging(debug=True, stream=sys.stdout)
    # utils.enable_logging(debug=True, path='ecl.log')

.. toctree::
   :maxdepth: 2

   ecl
