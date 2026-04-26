# ToDo アプリケーション

早稲田大学の Python 授業で作成した Bottle ベースの Web ToDo アプリです。SQLite3 でタスクを永続化し、一覧・追加・編集・完了切り替え・削除を実装しています。

## 機能

- タスク一覧表示
- タスク追加
- タスク詳細表示
- タスク編集
- 完了状態の切り替え
- タスク削除

## 技術スタック

- Python 3
- Bottle
- SQLite3
- HTML / CSS

## 実行

```bash
pip install bottle
python final_report.py
```

## 構成

- `final_report.py`: メインアプリ
- `views/`: Bottle テンプレート
- `static/style.css`: スタイル
- `todo.db`: データベース
- `期末課題_仕様と考察.pdf`: 課題資料

## 学習メモ

- Web フレームワークの基本
- データベースの CRUD 操作
- テンプレートと静的ファイルの分離
