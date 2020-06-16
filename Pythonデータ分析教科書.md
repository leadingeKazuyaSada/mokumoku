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

```python
import pickle

d = ...
print(pickle.dumps(d))

with open('xxx.pkl', 'wb') as f:
    pickle.dump(d, f)
```

```python
from pathlib import Path

p = Path()
for filepath in p.glob('*.txt'): # すべての .txt ファイル
    with open(filepath, encoding='utf_8_sig'):
        data = f.read()

p = Path('/spam')
p / 'ham' / 'eggs.txt'  # /spam/ham/eggs.txt
p.exists()              # 存在チェック
p.is_dir()              # ディレクトリか
```

### Jupyter Notebook

#### マジックコマンド

- %timeit   (行の実行時間計測)
- %%timeit  (セルの実行時間計測)
- !         (OS コマンド実行)

# Chapter 3

## e の定義

$$e = \sum_{n\,=\,0}^{\infty} \frac{1}{n!}$$

## シグモイド関数

$$f(x) = \frac{1}{1 + e^{-x}}$$

## 行列の分解

- 行列を分解して次元数を小さくできる。
- 主成分分析、非負値行列因子分解に使われる。

## 微分積分

- 積分の範囲が決まっているものを定積分という (<-> 不定積分)。

$$F'(x) = f(x)$$
- F を f の原始関数、f を F の導関数という。

$$\int{\frac{1}{x}}dx = log|x| + C$$

## 統計

### 統計量
- 最頻値 (mode)
- 四分位数 (第1～, 第3～)
- IQR (Interquartile Range) = 第3四分位数 - 第1四分位数
- 分散の不偏推定量 (不偏分散, 標本分散)

$$\frac{1}{n-1}\sum_{i\,=\,1}^{n}(x_i - \bar{x})^2$$

### ヒストグラム

- 分布が特定の階級に集中している時は、縦軸の度数を対数表示にすると把握しやすくなる。

### 箱ひげ図

- ひげは箱から最大値/最小値まで、または IQR * 1.5 の距離までのばす (近い方)。
- IQR * 1.5 よりも離れている値は「外れ値」とする。

### 相関

- 共分散

$$s_{xy} = \frac{1}{n}\sum_{i\,=\,1}^{n}(x_i - \bar{x})(y_i - \bar{y})$$

- 相関係数

$$r_{xy} = \frac{s_{xy}}{s_xs_y}$$
$$s_x: x の標準偏差$$
$$s_y: y の標準偏差$$
$$-1 \leq r_{xy} \leq 1$$
$$r_{xy} を「ピアソンの積率相関係数」という。$$

- スピアマンの順位相関係数

$$\rho_{xy} = 1-\frac{6\sum d\,_i^2}{n(n^2 - 1)}$$
$$d_i は、x_i の順位と y_i の順位の差$$

