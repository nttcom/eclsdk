---
agent: agent
description: 既存サービスに新規Resource/Proxyを追加する雛形を生成する
argument-hint: "{service名} {resource名} の追加内容（例: network service に QosOption resourceを追加し、create/get/list/deleteをサポートしたい）"
---

# Resource/Proxy 新規追加

`resource-proxy-pattern` skillのパターンに従い、既存サービスへ新規Resource/Proxyクラスの雛形を生成する。**いつ・なぜこのリソースを追加するかの判断は本プロンプトの対象外**。対象サービス・リソース名・サポートする操作・プロパティ一覧は、呼び出し側（ユーザーの指示、または別途共有された設計内容）から与えられる前提で進める。

## 参照

- `.github/instructions/resource-proxy.instructions.md`
- `.github/skills/resource-proxy-pattern/SKILL.md`

## 事前確認

以下が指示に含まれていない場合は質問する。

- 対象サービス（`ecl/{service}/v2/`の`{service}`）。新規サービスの場合はその旨を明示してもらう
- リソース名（単数形・クラス名）
- サポートする操作（create/get/update/delete/list のうち必要なもの）
- プロパティ一覧（プロパティ名・JSON上のキー名・型）
- 一覧取得時にフィルタ可能なクエリパラメータ

## 手順

1. 対象サービス配下の既存Resource/Proxyファイル（例: `ecl/network/v2/network.py`・`_proxy.py`）を読み、命名・インポート規約を確認する
2. `ecl/{service}/v2/{resource}.py`を新規作成し、`Resource`サブクラスを実装する
3. `ecl/{service}/v2/_proxy.py`に、サポートする操作に応じた`create_*`/`get_*`/`update_*`/`delete_*`/一覧メソッドを追記する

## 出力

- 作成・変更したファイルの一覧
- 未確定のまま仮置きした項目（プロパティの型、クエリパラメータ等）があれば明示する
