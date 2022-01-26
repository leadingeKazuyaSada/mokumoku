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
(参考) 「Vue.js 入門」8.4.2 - プロジェクト構造

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

(参考) [Vuex の状態を Vue コンポーネントに入れる](https://vuex.vuejs.org/ja/guide/state.html#vuex-%E3%81%AE%E7%8A%B6%E6%85%8B%E3%82%92-vue-%E3%82%B3%E3%83%B3%E3%83%9B%E3%82%9A%E3%83%BC%E3%83%8D%E3%83%B3%E3%83%88%E3%81%AB%E5%85%A5%E3%82%8C%E3%82%8B)

- Vuex は、ルートコンポーネントに store オプションを指定することで (これは、 Vue.use(Vuex) で有効にできます)、すべての子コンポーネントにストアを "注入" する機構を提供しています:
    ```JavaScript
    const app = new Vue({
    el: '#app',
    // "store" オプションで指定されたストアは、全ての子コンポーネントに注入されます
    store,
    components: { Counter },
    template: `
        <div class="app">
        <counter></counter>
        </div>
    `
    })
    ```
- ルートインスタンスに store オプションを渡すことで、渡されたストアをルートの全ての子コンポーネントに注入します。これは this.$store で各コンポーネントから参照することができます。

(参考) 「Vue.js 入門」7.7.1 - コンポーネント から ストア に アクセス する

- コンポーネント から ストア を 使う ため に、 ルート の Vue インスタンス 生成 時 に ストア を 渡し ます。
- コンポーネント から ストア を 参照 する には this.$ store から ストア を 直接 使う 方法、 Vuex が 提供 し て いる ヘルパー 関数 を 使用 する 方法 の 2 つ が あり ます。
</details>

---
## 子コンポーネントで $store と書かないのはなぜか

<details>
<summary>解説</summary>

- 不明。要調査。
- 単にそれをしていないだけなのか、上記の store オプションをルートコンポーネントに指定していなかったのかも知れない。

</details>

---
## $route と書けるのはなぜか

<details>
<summary>解説</summary>

- $route で Router にアクセスしている訳ではない。
- よって、Router にアクセスするのに $route と書ける訳ではない。

</details>

---
## $route と $router の違いは何か

<details>
<summary>解説</summary>
(参考) 「Vue.js 入門」4.5.1 - Router インスタンス と Route オブジェクト

- $router は Router インスタンスを表す (アプリケーション全体に対してひとつ存在)。
- $route は Route オブジェクトを表す (ページ遷移ごとに生成される)。
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
