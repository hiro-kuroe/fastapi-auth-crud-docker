# FastAPI 認証付きCRUD（Docker対応）

## 概要
既存業務システムを想定した、JWT認証付きFastAPIのサンプル構成です。

## 主な機能
- JWT認証（/token, /me）
- CRUD API
- Docker起動対応

## 想定ユースケース
- 既存FastAPIの改修・保守
- JWT認証事故の切り分け
- Docker環境でのAPI運用

## JWT事故対応メモ
- SECRET_KEY変更時の401挙動
（詳細は md 参照）

## 起動方法（Docker）

## 注意点
