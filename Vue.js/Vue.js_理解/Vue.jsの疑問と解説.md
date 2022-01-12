# Vue.js の疑問と解説

## Vue CLI によるビルドは何をするのか

<details>
<summary>解説</summary>

### Vue CLI について

- Vue CLI は、npm でインストールする。  
グローバルにインストールする場合
    ```
    > npm install -g @vue/cli
    > npm install -g @vue/cli-service-global
    ```
    - npm は Node.js のパッケージマネージャ
- インストールすると、vue というコマンドが使えるようになる。
    ```
    > vue version
    > vue init webpack my-app
    ```
- vue 自身はグローバルにインストールして、vue init でプロジェクトを作ってからプロジェクトごとのインストールをするのが一般的のよう。

### ビルドにより起こること

- vue init でテンプレートからプロジェクトを作ったなら、いきなりビルドすることも可能。
    ```
    > cd my-app
    > npm run build
    ```
- ビルドは、「単一ファイルコンポーネント」を、Web ブラウザで実行できる形に変換する。
    - `<template>`, `<script>`, `<style>` の各ブロックが、HTML, JavaScript, CSS に変換される。
    - 最終的に JavaScript になる (html や style は実行時に動的に生成される)。
- build コマンドではビルドしたものを dist フォルダ以下に配置し、**Web server でアクセスできる形**にする。
    - index.html を直接開いても動かない。
- 開発用のサーバを起動したいなら、dev コマンドでビルドから起動まで出来る。
    ```
    > npm run dev
    ```
</details>

---
## App.vue, index.html, xxPage.vue の関係とは

<details>
<summary>解説</summary>
(参考)「Vue.js 入門」8.4.2 - プロジェクト構造

- **App.vue** : 実行エントリポイントとなるコンポーネント
    - src フォルダ以下に置かれる。
    - この中のテンプレートに `<router-view/>` と書かれていることで SPA になる。
- **index.html** : SPA のテンプレートとなる html
    - プロジェクト直下に置かれる
    - これを元にビルドしたものが dist/index.html となる。
    - `<div id=app></div>` の下にビルドした JS を読む `<script>` タグが挿入される。
    - その JS は App.vue に書かれた内容を実行する。
- **xxPage.vue** : router によって読み込まれるコンポーネント
    - src/components フォルダ以下に置かれる。
    - router は、これらのコンポーネントを切り替えつつ読み込むことで、SPA で画面遷移を起こす。
    - ページそのものでなく、他のページに埋め込む部品としてのコンポーネントもある。

</details>

---
## $store と書けるのはなぜか

<details>
<summary>解説</summary>

</details>

---
## 子コンポーネントで $store と書かないのはなぜか

<details>
<summary>解説</summary>

</details>

---
## $route と書けるのはなぜか

<details>
<summary>解説</summary>

</details>

---
## $route と $router の違いは何か

<details>
<summary>解説</summary>

</details>

---
## store の actions が受け取る context とは何か

<details>
<summary>解説</summary>

</details>

---
## style scoped はどういう仕組か

<details>
<summary>解説</summary>

</details>

---
## JS の非同期処理の理解

<details>
<summary>解説</summary>

</details>
