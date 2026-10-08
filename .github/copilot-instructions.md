# eclsdk - GitHub Copilot Instructions

`eclsdk`はNTTのEnterprise Cloud 2.0（ECL2.0）向けのオープンソースPython SDKであり、GitHub上で公開されている。本リポジトリは常に、他のリポジトリとは独立した公開OSSプロジェクトとして扱うこと。

## 対応Pythonバージョン

本SDKはPython 3.5〜3.9に対応している。新規コードもこの範囲との互換性を維持すること。

## コーディング規約

- 新規`.py`ファイルの先頭には、リポジトリ全体で使われているApache License 2.0のヘッダーブロックを必ず付ける（同一ディレクトリ内の既存ファイルからコピーする）
- PEP 8 / flake8に従う（`tox -e pep8`）
- 公開`Resource`/`Proxy`メソッドにはSphinx形式のdocstring（`:param:`、`:returns:`、`:rtype:`）を付ける
- 単体テストは`pytest`ではなく`testtools.TestCase`（またはリポジトリ独自の`ecl.tests.unit.base.TestCase`）と`mock`を使う

## Markdownリンク規則

Markdownファイル内で他のドキュメントへリンクする場合、**リポジトリルートを`/`とする絶対パス**を使う（`../`等の相対パスは使わない）。同一ディレクトリ内のファイルへのリンクは`./`を使ってよい。

| 正しい例 | 誤った例 |
|---|---|
| `[instructions](/.github/instructions/resource-proxy.instructions.md)` | `[instructions](instructions/resource-proxy.instructions.md)` |
| `[instructions](/.github/instructions/resource-proxy.instructions.md)` | `[instructions](../instructions/resource-proxy.instructions.md)` |

## リポジトリ構成（日常的な変更に関連する範囲）

```
ecl/
  {service}/                   ← 例: network, compute, block_store
    {service}_service.py       ← ServiceFilterサブクラス（service_type, valid_versions）
    v2/
      _proxy.py                ← Proxyクラス。リソースごとにcreate_/get_/update_/delete_/listメソッド群を持つ
      {resource}.py             ← Resourceサブクラス
  tests/unit/{service}/v2/
    test_{resource}.py          ← Resourceのプロパティ・capabilityテスト
    test_proxy.py               ← Proxyメソッドのテスト（verify_create/get/update/delete/list）
```

## 関連するinstructions・skills

- [`instructions/resource-proxy.instructions.md`](/.github/instructions/resource-proxy.instructions.md)（`applyTo: ecl/**/v2/*.py`）— `Resource`/`Proxy`の実装規約
- [`skills/resource-proxy-pattern/SKILL.md`](/.github/skills/resource-proxy-pattern/SKILL.md) — 新規Resource/Proxy追加の具体的なパターン
- [`prompts/sdk-add-resource.prompt.md`](/.github/prompts/sdk-add-resource.prompt.md) — 新規Resource/Proxyのスキャフォールディング用プロンプト

単体テストの自動生成（`sdk-add-test`相当）は、既存の単体テストが現状動作していないため本整備の対象外とし、別途対応する。

これらのプロンプトはスキャフォールディング（生成）作業のみを担う。「なぜ・いつそのリソースを追加するか」という判断は別の場所で行われるものであり、本リポジトリの`.github/`設定の対象外として意図的に除外している。

