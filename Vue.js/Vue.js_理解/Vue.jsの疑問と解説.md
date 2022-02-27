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
- 2行目は webpack というテンプレートを使ってプロジェクトを作成している。
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
    - これを (router の機能をつけて) マウントしているのは "main.js"。
- **index.html** : SPA のテンプレートとなる html
    - プロジェクト直下や、public フォルダに置かれる。
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

- Vuex は、ルートコンポーネントに store オプションを指定する (main.js でやっている) ことで (これは、 Vue.use(Vuex) で有効にできます)、すべての子コンポーネントにストアを "注入" する機構を提供しています:
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

- 理由が不明だが、前任者が `$store` を使わず独自に `import` していた。
- ためしに `$store` を使ってみたが問題なかった。

</details>

---
## $route と書けるのはなぜか

<details>
<summary>解説</summary>

- `$router` と `$route` は違うもの。
- よって、`$router` の代わりに `$route` と書ける訳ではない。

</details>

---
## $route と $router の違いは何か

<details>
<summary>解説</summary>
(参考) 「Vue.js 入門」4.5.1 - Router インスタンス と Route オブジェクト

- `$router` は Router インスタンスを表す (アプリケーション全体に対してひとつ存在)。
- `$route` は Route オブジェクトを表す (ページ遷移ごとに生成される)。
</details>

---
## store の actions が受け取る context とは何か

<details>
<summary>解説</summary>

(参考) [アクション | Vuex](https://vuex.vuejs.org/ja/guide/actions.html)

- アクションハンドラはストアインスタンスのメソッドやプロパティのセットと同じものを呼び出せるコンテキストオブジェクトを受け取ります。
- したがって `context.commit()` を呼び出すことでミューテーションをコミットできます。
- あるいは `context.state` や `context.getters` で、状態やゲッターにアクセスできます。
- 他のアクションを `context.dispatch()` で呼ぶこともできます。
</details>

---
## style scoped はどういう仕組か

<details>
<summary>解説</summary>
(参考) 「Vue.js 入門」6.6.2 - スコープ付き CSS

- 単一ファイルコンポーネントの `<style>` ブロックに `scoped` 属性をつけることによって、そのコンポーネント内の要素にのみ適用するスタイルとなる。
- `<style>` ブロックは複数定義できるので、スコープ付きとスコープなしの両方を定義することもできる。
- スコープ付き `<style>` ブロックを持つコンポーネントをビルドすると、そのブロック内のスタイルとそれが適用される要素に、スコープ ID (ハッシュ値) をもつ属性が設定される。これにより疑似的に名前空間を実現している。
</details>

---
## JS の非同期処理の理解

<details>
<summary>解説</summary>

(参考) [【図解】1から学ぶ JavaScript の 非同期処理 - Qiita](https://qiita.com/ryosuketter/items/dd467f827c1b93a74d76)

- JS はシングルスレッドで、基本的には同期処理。
- 非同期処理が起きるのは以下の Web API。
    - `setTimeout()`
    - `fetch()` などサーバのレスポンスを待つ処理
    - `onClick` などの DOM Event
    - `Promise`
- Web API は受け取った非同期処理をタスクキューに送る。
- タスクキューにある処理は、コールスタックが空になったら実行される。
- コールスタックは LIFO、タスクキューは FIFO。

Promise  
(参考) [Promise - JavaScript | MDN](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Promise)

- 非同期処理の結果によってさらに非同期処理をする、といったようなもの。
- 引数を `(resolve, reject)` とした場合、Promise の中で `resolve()` したら正常終了、`reject()` したら異常終了したということ。
- `then()` には2つまでの引数 (関数) を指定できて、`resolve()` されて来たのか `reject()` されて来たのかによって実行される関数が決まる。関数の引数には `resolve()` や `reject()` の引数を取る。
    - 大抵は1個だけ指定して、`resolve()` されて来た時の処理とする。
- `catch()` の引数 (1個) となる関数は、`reject()` されて来た場合のみ実行される。
- `then()`, `catch()`, `finally()` の (引数になっている) 関数は、非同期的に実行される。

async, await
(参考) [async/await 入門（JavaScript） - Qiita](https://qiita.com/soarflat/items/1a9613e023200bbebcb3)

- async function は呼び出されると Promise を返す。
- async function が値を return した場合、Promise は戻り値を resolve する。
- async function が例外や何らかの値を throw した場合はその値を reject する。
- await は非同期処理の結果が返る (resolve または reject される) まで待機する。
- await は async function の中でしか使えない。

</details>
