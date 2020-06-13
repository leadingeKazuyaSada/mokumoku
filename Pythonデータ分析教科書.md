# Chapter 1

## データ分析に使われる主なパッケージ

- Jupyter notebook (Jupyter Lab)
- NumPy
- pandas
- Matplotlib
- SciPy
- scikit-learn

## データサイエンティストの知識

- 数学
- 情報工学
- ドメイン知識 (対象分野の専門知識)

## データ分析エンジニアの技術

- 必須
    - データの入手や加工
    - データの可視化
    - プログラミング
    - インフラ
- オプション
    - 機械学習
    - 数学 (高校～大学初等レベル)
    - ドメイン知識

## 分類・予測の手法

- 機械学習
- ルールベース
- 統計的な手法

## 機械学習の種類

- 教師あり学習
    - 回帰
    - 分類
- 教師なし学習
    - クラスタリング
    - 次元削減
- 強化学習

## 機械学習の処理の流れ

1. データ入手
2. データ加工
3. データ可視化
4. アルゴリズム選択
5. 学習プロセス
6. 精度評価
7. 試験運用
8. 結果利用

# Chapter 2

## venv で仮想環境を作る

```
> python -m venv 仮想環境名
```

## Anaconda

- 独自の仮想環境・パッケージ管理方法を採用
- conda のリポジトリも独自 (pip とは別)

## Python の基礎

- PEP 8をチェックするのに pycodestyle がある。
- Flake8 は静的解析をする。
- IPython は高機能な対話モード (Jupyter っぽい)
- リスト内包表記の [] を () にするとジェネレータ式

### str のメソッド

- endswith()
- isdigit()

### 標準モジュール

```python
import logging

logging.basicConfig(
    filename='xxx.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)
```

