# FastAPI 認証付きCRUD（Docker対応）

このリポジトリは、JWT認証付きCRUDを備えたFastAPI構成例です。
既存業務システムのAPI保守・改修や、JWT認証トラブル（401/403）の切り分けを想定しています。

Dockerで起動し、Swaggerおよびcurlを使って動作確認できます。


## 主な機能

Swagger UI（/docs）上でトークンを発行し、
認証付きエンドポイント（/me）が 200 OK で返るところまで確認できます。

- JWT認証（/token, /me）
- CRUD API
- Docker起動対応


## 想定ユースケース

- 既存FastAPIの改修・保守
- JWT認証事故（401/403）の切り分け
- Docker環境でのAPI運用・検証


## JWT事故対応メモ

- SECRET_KEY変更時に発生する401/403の挙動整理  
  詳細は `jwt_troubleshooting.md` を参照


## 起動方法（Docker）

1. 環境変数ファイルを作成します（初回のみ）

    Windows（PowerShell）:
    copy .env.sample .env

    macOS / Linux:
    cp .env.sample .env

2. Dockerイメージをビルドして起動します

    docker build -t fastapi-auth-crud .
    docker run -p 8000:8000 --env-file .env fastapi-auth-crud

3. 起動後、Swagger UIにアクセスします

    http://localhost:8000/docs


## 注意点

- `.env` の `SECRET_KEY` を変更すると、既存のJWTはすべて無効になります。
