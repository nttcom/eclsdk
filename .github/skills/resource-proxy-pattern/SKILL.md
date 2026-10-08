---
name: resource-proxy-pattern
description: ecl/{service}/v2/ 配下への新規Resource/Proxy追加の具体的な実装パターン。/sdk-add-resource実行時に参照する。
---

# Resource / Proxy 追加パターン

既存サービス（例: `network`）に新しいリソースを追加する際の、具体的なコードパターン。実装規約は`.github/instructions/resource-proxy.instructions.md`を参照。

## 追加するファイル・箇所

| ファイル | 操作 |
|---|---|
| `ecl/{service}/v2/{resource}.py` | 新規作成（`Resource`サブクラス） |
| `ecl/{service}/v2/_proxy.py` | 追記（`Proxy`クラスにメソッド追加） |

> 既存の単体テスト（`ecl/tests/unit/`配下）は現状動作していないため、本skillの対象外とする。

## Resource クラスの実装例（`ecl/network/v2/network.py`より）

```python
# -*- coding: utf-8 -*-

from . import base
from ecl.network import network_service
from ecl import resource2
from ecl import exceptions


class Network(base.NetworkBaseResource):

    resource_key = 'network'
    resources_key = 'networks'
    service = network_service.NetworkService("v2.0")
    base_path = '/' + service.version + '/networks'

    # capabilities
    allow_create = True
    allow_get = True
    allow_update = True
    allow_delete = True
    allow_list = True

    # query mappings
    _query_mapping = resource2.QueryParameters(
        'description', 'id', 'name', 'plane', 'status', 'tenant_id',
        'network_id', "sort_key", "sort_dir",
    )

    # Properties
    #: admin_state_up status of network
    admin_state_up = resource2.Body('admin_state_up')

    #: The network description.
    description = resource2.Body('description')

    #: The network id.
    id = resource2.Body('id')

    #: The network name.
    name = resource2.Body('name')

    #: The ID of the project this network is associated with.
    project_id = resource2.Body('tenant_id')

    #: The network status.
    status = resource2.Body('status')

    #: admin_state displayed by 'UP' or 'DOWN'
    @property
    def admin_state(self):
        return 'UP' if self._body.get('admin_state_up') else 'DOWN'
```

- `base.NetworkBaseResource`のような、サービス固有の共通基底クラスがあればそれを継承する（存在しなければ`resource2.Resource`を直接継承する）
- `resource_key`/`resources_key`はAPIレスポンスのJSONキーに合わせる（単数/複数が異なる綴りの場合も実際のレスポンスに合わせる）
- `_query_mapping`は一覧APIがサポートするクエリパラメータのみを列挙する

## Proxy メソッドの実装例（`ecl/network/v2/_proxy.py`より）

```python
from ecl.network.v2 import network as _network


class Proxy(proxy2.BaseProxy):

    def create_network(self, admin_state_up=None, description=None,
                       name=None, plane=None, tenant_id=None, tags=None):
        """Create a new network from attributes

        :param bool admin_state_up: administrative state, default true
        :param string description: description of network
        :param string name: name of network
        :param string tenant_id: tenant id to create network

        :returns: The results of network creation
        :rtype: :class:`~ecl.network.v2.network.Network`
        """
        body = dict()
        body.setdefault("admin_state_up", False)
        if admin_state_up:
            body["admin_state_up"] = admin_state_up
        if description:
            body["description"] = description
        if name:
            body["name"] = name
        if tenant_id:
            body["tenant_id"] = tenant_id
        return self._create(_network.Network, **body)

    def get_network(self, network):
        """Get a single network

        :param network: The value can be the ID of a network or a
            :class:`~ecl.network.v2.network.Network` instance.
        :returns: One :class:`~ecl.network.v2.network.Network`
        :raises: :class:`~ecl.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_network.Network, network)

    def networks(self, **params):
        """Return a list of networks

        :param params: The parameters as query string to filter networks.
        :returns: A list of network objects
        :rtype: list of :class:`~ecl.network.v2.network.Network`
        """
        return list(self._list(_network.Network, paginated=False, **params))

    def update_network(self, network, **params):
        """Update a network

        :param network: Either the id of a network or a
            :class:`~ecl.network.v2.network.Network` instance.
        :returns: The updated network
        :rtype: :class:`~ecl.network.v2.network.Network`
        """
        if not isinstance(network, _network.Network):
            network = self._get_resource(_network.Network, network)
            network._body.clean()
        return self._update(_network.Network, network, **params)

    def delete_network(self, network, ignore_missing=False):
        """Delete a network

        :param network: The value can be either the ID of a network or a
            :class:`~ecl.network.v2.network.Network` instance.
        :param bool ignore_missing: When set to ``False``
            :class:`~ecl.exceptions.ResourceNotFound` will be raised when
            the network does not exist.
        :returns: ``None``
        """
        self._delete(_network.Network, network, ignore_missing=ignore_missing)
```

- `create_*`は許可された属性のみキーワード引数として受け取り、`None`でない値だけを`body`辞書に詰める
- 新規追加するProxyメソッドは、ファイル先頭の`from ecl.{service}.v2 import {resource} as _{resource}`のインポート規約に合わせる


- `test_proxy_base2.TestProxyBase`を継承し、`setUp`で対象サービスの`Proxy`をインスタンス化する
- `verify_create`/`verify_get`/`verify_update`/`verify_delete`/`verify_list`は`ecl/tests/unit/test_proxy_base2.py`が提供するヘルパーで、対応する`BaseProxy._create`等が正しい引数で呼ばれることを検証する（実HTTPリクエストは発生しない）
- 削除系は`ignore_missing=True`/`False`の両方をテストする
