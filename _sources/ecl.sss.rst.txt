sss
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

    contract = conn.sss.get_contract("<contract_id>")
    print contract.name

You can use methods corresponding to API like ``conn.sss.<method>``

Please refer to ``sss methods`` below to check available methods.

.. toctree::

    ecl.sss.v1
