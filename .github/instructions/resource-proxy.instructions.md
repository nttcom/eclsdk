---
applyTo: "ecl/**/v2/*.py"
---

# Resource / Proxy 実装規約

`ecl/{service}/v2/` 配下の `Resource` サブクラスと `Proxy` クラスを実装・修正する際の規約。具体的なコード例は`resource-proxy-pattern` skillを参照する。

## 必須事項

- ファイル冒頭に既存ファイルと同じApache License 2.0ヘッダーを付ける
- `Resource`サブクラスは`ecl.resource2.Resource`（または各サービスの`base.XxxBaseResource`）を継承する
- `Proxy`クラスのメソッドは`ecl.proxy2.BaseProxy`の`_create`/`_get`/`_update`/`_delete`/`_list`/`_find`に委譲し、HTTPリクエストの組み立てを自分で書かない
- 公開メソッド（Proxyのpublicメソッド、Resourceの`find`等）にはSphinx形式のdocstring（`:param:`・`:returns:`・`:rtype:`）を付ける
- Python 3.5〜3.9 互換を維持する

## Resource クラスの構成要素

| 項目 | 必須 | 説明 |
|---|---|---|
| `resource_key` | 単数リソース名の場合 | レスポンスの単数キー（例: `'network'`） |
| `resources_key` | 一覧取得する場合 | レスポンスの複数キー（例: `'networks'`） |
| `service` | ○ | `{service}_service.XxxService("v2.0")`のインスタンス |
| `base_path` | ○ | `'/' + service.version + '/{resources_key}'` |
| `allow_create`/`allow_get`/`allow_update`/`allow_delete`/`allow_list` | ○ | サポートするCRUD操作のみ`True`にする |
| `_query_mapping` | 一覧取得にフィルタがある場合 | `resource2.QueryParameters('key1', 'key2', ...)` |
| プロパティ | ○ | `resource2.Body('json_key')` / `resource2.Header(...)` / `resource2.URI(...)` |

- プロパティ名とJSONキー名が異なる場合は`resource2.Body('json_key_name')`のように明示する（例: `project_id = resource2.Body('tenant_id')`）
- 計算プロパティは`@property`で実装する

## Proxy クラスの構成要素

- 1つのResourceにつき、必要な操作ごとに`create_{resource}` / `get_{resource}` / `update_{resource}` / `delete_{resource}` / `{resources_key}`（一覧。単数形`list_{resource}`にはしない）のメソッド名規約に従う
- `create_*`は個別のキーワード引数を受け取り、`body`辞書を組み立てて`self._create(ResourceClass, **body)`を呼ぶ
- `get_*`/`update_*`/`delete_*`は、ID文字列とResourceインスタンスの両方を受け取れるようにする（`self._get`/`self._update`/`self._delete`がこれを内部で吸収する）
- 一覧メソッドは`list(self._list(ResourceClass, paginated=False, **params))`で`list`化して返す（ページネーション不要なAPIの場合）
- 既存の同サービス内の他Proxyメソッドと命名・引数順序の一貫性を保つ

## 新規サービス追加時の注意

既存サービス（`network`・`compute`等）への新規Resource/Proxy追加が大半を占める。新規サービス自体を追加する場合は、`{service}_service.py`（`ServiceFilter`サブクラス）の作成に加えて、`ecl/profile.py`・`ecl/connection.py`側の登録箇所も確認する必要があるため、既存の類似サービス追加差分を参照する。
