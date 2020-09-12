# パッケージの作成

参考
- [python の pip でインストールできる自作モジュールを作ってみる / 桃缶食べたい。](https://blog.chocolapod.net/momokan/entry/117)
- [【Techの道も一歩から】第21回「setup.pyを書いてpipでインストール可能にしよう」 - Sansan Builders Blog](https://buildersbox.corp-sansan.com/entry/2019/07/11/110000)

## 自作モジュールのパッケージ化

### 最低限のフォルダ構成

```
pyplaysc
    │  setup.py
    └─pyplaysc
            __init__.py
            play_sc.py
```

### \_\_init\_\_.py の中での import 

参考
- [Pythonの相対インポートで上位ディレクトリ・サブディレクトリを指定 | note.nkmk.me](https://note.nkmk.me/python-relative-import/)

例: 同じパッケージの同じフォルダにあるモジュールからクラスをインポート
```
from .play_sc import PlaySc, PlayScElement
```

## pipenv install の仕方

参考
- [バージョン管理システムについての但し書き](https://pipenv-ja.readthedocs.io/ja/translate-ja/basics.html#a-note-about-vcs-dependencies)

ローカルの git リポジトリからインストール
```
> pipenv install -e git+file://F:/Dev/Python/my_pckg/playscript#egg=playscript
```

※ #egg=xxx をつけないとエラー。
※ -e は、editable mode (依存性解決をするモード)。
※パスに @master をつけるとエラー (ローカルだから？)。

ローカルのディレクトリをインストール
```
> pipenv install -e F:/Dev/Python/my_pckg/playscript
```

### アンインストール

普通にアンインストールするとエラーになる。

```
> pipenv uninstall playscript
(エラーメッセージ)
```

Pipfile から playscript の行を削除してから pipenv clean するとアンインストールできる。
```
> pipenv clean
```

※ローカルの git リポジトリからインストールした場合、なぜかアンインストールできない (というか、アンインストールしても認識される)。
※.venv/src フォルダから削除したら認識されなくなった。

## Pipfile の書き方

ローカルのディレクトリをインストールする場合は、`packages` ディレクティブに以下の行を追加して `pipenv update` する。

```
[packages]
playscript = {editable = true,path = "F:/Dev/Python/my_pckg/playscript"}
```
または
```
[packages]
playscript = {editable = true,git = "file:///F:/Dev/Python/my_pckg/playscript"}
```

そして
```
> pipenv update
```

## pip install の仕方

ローカルの git リポジトリからインストール
```
> pip install -e git+file://F:/Dev/Python/my_pckg/playscript@master#egg=playscript
```

※ #egg=xxx をつけないとエラー。
※ -e は、editable mode (依存性解決をするモード)。

ローカルのディレクトリをインストール
```
> pip install -e F:/Dev/Python/my_pckg/playscript
```

### アンインストール

```
> pip uninstall playscript
```

※ローカルの git リポジトリからインストールした場合、なぜかアンインストールできない (というか、アンインストールしても認識される)。
※.venv/src フォルダから削除したら認識されなくなった。

## requirements.txt の書き方

```
# Editable Git install with no remote (pyplaysc==0.1)
-e f:/dev/python/my_pckg/pyplaysc
```

※ pip freeze すると、パスの区切りが `\` になっていて `pip install -r` で使えないので、`\` を `/` に置換しておくこと。

または
```
-e git+file://F:/Dev/Python/my_pckg/playscript@master#egg=playscript
```
