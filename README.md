
# FastAPI JWT Incident Playground

FastAPI + JWT + Docker で発生しやすい  
**認証トラブルの再現・切り分け用構成** です。

新規開発サンプルではなく、  
「既存APIが壊れたとき、どこを見るべきか」に焦点を当てています。

---

## 🧠 Who I am

FastAPIを中心に、JWT認証やDocker環境における  
**認証・構成トラブルの分析（インシデント評価）** を専門にしています。

新規開発よりも、既存システムの  
**原因特定 → 構造整理 → 修正方針提示** を重視しています。

---

## 🎯 主な対象症状

以下のような「原因の層が見えない事故」を扱います。

- `/token` は通るのに `/me` が 401 / 403
- ローカルでは動くのに Docker 本番で認証失敗
- `InvalidSignatureError` が本番のみ発生
- 昨日まで動いていたのに急に落ちた

切り分け・分析・修正方針の整理を目的としています。

---

## 📚 関連記事（背景解説）

**FastAPIでログインできるのに認証だけ失敗するとき ── /token は通るのに /me が 401 になる原因**  
https://zenn.dev/fastapier/articles/0022f125547300

---

## 🔍 このリポジトリで確認できること

Swagger UI（`/docs`）上で、

- JWT認証（`/token`, `/me`）
- CRUD API
- Docker起動構成

まで確認できます。

**再現 → 原因特定 → 説明** の流れを意識した構成です。

---

## ⚠ 対応対象について

本リポジトリは、

**FastAPI単体、もしくは FastAPI が認証責務を持つ構成**

を前提としています。

Django 等と混在する構成の場合は、  
責務分離の状況を確認のうえ対応可否を判断します。

---

## 起動方法（Docker）

### 1. 環境変数ファイルを作成します（初回のみ）

#### Windows（PowerShell）

```powershell
copy .env.sample .env
```
#### macOS / Linux
```
cp .env.sample .env
```
### 2. Dockerイメージをビルドして起動します
```
docker build -t fastapi-auth-crud .
docker run -p 8000:8000 --env-file .env fastapi-auth-crud
```
## 3. Swagger UI にアクセスします
ブラウザで以下の URL を開いてください。

http://localhost:8000/docs

## デモユーザーについて
動作確認を簡単に行うため、起動時に以下のデモユーザーを自動作成します。

- username: demo
- password: demo123


このユーザーを使用して /token から JWT を発行し、
/me エンドポイントの認証動作を確認できます。

※ 実務ではこのような固定ユーザーは使用しません。

---

## 📩 相談窓口（Incident Consultation）

FastAPI / JWT / Docker まわりの認証トラブルを「原因の層」で切り分け、修正方針まで整理します。


ご相談は、
GitHubプロフィール記載のメールアドレス までご連絡ください。
https://github.com/hiro-kuroe

メール本文に、以下3点のみご記載ください（短文でOK）：

① 症状
（例：/me が 401 / 本番だけ署名エラー / Docker後に失敗）

② 環境
（例：ローカルOK・本番NG / Docker使用 / Gunicorn使用）

③ 直前に変更した点
（例：SECRET_KEY変更 / .env追加 / 依存更新）

※まずは 分析フェーズ（原因特定と構造整理） から進めます。
修正作業は、原因確定後にご提案します。

※現在、即日対応は行っておりません。順次ご返信いたします。

---

### 🔎 相談前に確認できる資料

相談をご検討中の方は、以下をご確認ください。

- 相談時の記載テンプレート  
  → docs/intake.md

- 分析 → 修正までの流れ  
  → docs/menu.md

- 分析レポートのサンプル構成  
  → docs/report-sample.md

事前に目を通していただくことで、やり取りがスムーズになります。
