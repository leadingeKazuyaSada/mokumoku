- 改訂2版
- Python 3.6

# 第1章

PEP (Python Enhancement Proposal)

- 通知 (Informing)
- 標準化 (Standardizing)
- 設計 (Designing)

遅延ロードモジュール

- インポート時に読み込まれないモジュール
- 出来る限り使わない

セマンティックバージョニング

- メジャー, マイナー, パッチ

compat.py

- Python 2と3の互換性維持のためにパッケージに入れておくモジュール

CPython 以外の実装

- Stackless Python
    - C 言語のコールスタックに依存しない
- Jython
    - Java による Python 実装
- IronPython
    - .NET 環境で使える Python
- PyPy
    - Python による Python 実装

仮想環境

- pip freeze は必要のないパッケージも書き出してしまう。
- この問題に対応するため、buildout というのがある。
- ただし buildout 2.x はもはや環境分離ツールではない。

システムレベルでの仮想環境

- Vagrant (仮想マシンまたはコンテナ)
    - 開発用
- Docker (コンテナ)
    - デプロイに使える

スタートアップスクリプト

- インタラクティブセッションの設定をするスクリプト
- PYTHONSTARTUP 環境変数で指定する。
- 自分でスクリプトを書かずにツールを使用する場合
    - IPython
    - bpython
    - ptpython

インタラクティブデバッガ

- pdb
    - デバッグ実行ができる。
    - ブレークポイントはコードとして書く。
- IPython, bpython, ptpython を元にしたデバッグ用モジュールもある。

# 第2章

文字列とバイト列

- Python 3では文字列は Unicode のみを格納できる
- bytearray は bytes を変更可能にしたもの
- bytearray にはリテラルはない
- 文字列をバイト列にするのは、`str.encode()`
    - または `bytes()` コンストラクタ
- バイト列を文字列にするのは `bytes.decode()`
    - または `str()` コンストラクタ
- 文字列もバイト列も immutable (不変)
- bytearray は list のように変更可能
- 文字列を繰返し連結するより `str.join()` の方が速い

コレクション

- CPython のリストは、リンクリストではない
    - Jython や IronPython も
- リスト内包表記を使っても、ループごとのリサイズは起きる
- アンパック式は、左辺と右辺の要素数が同じになるよう解釈する
```
first, *inner, last = 0, 1, 2, 3
# first: 0
# inner: [1, 2]
# last: 3
```

辞書

- 辞書の keys(), values(), items() の返り値はリストではない
    - ビューオブジェクト (dict_keys オブジェクトなど) を返す
- dict_keys と dict_values は、辞書の動的な変更に追従する
    - 辞書を変更しても、イテレーションの順序が同じとなる
- hashable なオブジェクトのみがキーとして使える
- hashable な型は \_\_hash\_\_() と \_\_eq\_\_() メソッドを持つべき
- 同値のオブジェクトはハッシュ値も同じになるべき
- 同値でないオブジェクトのハッシュ値が同じになっても良い
- イテレーションにかかる時間は、今まで格納してきた最大の要素数に比例する
    - 要素を大量に削除する代わりに、新しい辞書を作った方が良い

集合