Zenn記事（本リポジトリの背景・事故解説）：
FastAPI × JWT事故メモ── /tokenは通るのに /me が401になる理由
https://zenn.dev/fastapier/articles/0022f125547300

## Who I am

FastAPIを中心に、JWT認証やDocker環境における「認証・構成トラブル」の分析を専門にしています。
新規開発よりも、既存システムの **インシデント分析・評価** を通じた現状回復を重視しています。


### Focus
- 「/token は通るのに /me が 401 になる」
- 「ローカルでは動くのに Docker環境だと認証が失敗する」

といった、原因特定が難しい事象の切り分け・分析・修正方針の整理。


### Contact
ご相談は GitHub のプロフィール（Website / 連絡先）からお願いします。
まずは状況を共有いただき、対応可否も含めて分析の進め方をご提案します。


## このリポジトリについて

このリポジトリは、FastAPI + JWT + Docker で起きがちな認証事故を
「再現→原因特定→説明」できる形でまとめたものです。

新規開発のサンプルではなく、
既存APIが壊れたときに、どこを見るべきかを重視しています。
実務での初動切り分けや、原因説明のための「診断用構成」を目的としています。


## この構成で確認できること

Swagger UI（/docs）上でトークンを発行し、
認証付きエンドポイント（/me）が 200 OK で返るところまで確認できます。

  - JWT認証（/token, /me）
  - CRUD API
  - Docker起動対応


## 想定している利用シーン

- 昨日まで動いていた FastAPI が急に 401 / 403 を返し始めた
- /token は通るのに /me だけが認証を通らない
- Docker 環境にした途端に挙動が変わった
- 新しく作り直す時間や余裕はない


## JWT事故対応メモ

- SECRET_KEY変更時に発生する401/403の挙動整理  
  実案件で最も多い事故パターンの一つです。  
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


## デモユーザーについて

本リポジトリでは、動作確認を簡単に行うため、
起動時に以下のデモユーザーを自動作成します。

- username: demo
- password: demo123

このユーザーを使用して `/token` からJWTを発行し、  
`/me` エンドポイントの認証動作を確認できます。

※ 実務ではこのような固定ユーザーは使用しません。


## 注意点

  - `.env` の `SECRET_KEY` を変更すると、既存のJWTはすべて無効になります。
