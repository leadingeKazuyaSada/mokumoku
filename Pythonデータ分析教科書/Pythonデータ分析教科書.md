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

## 確率

- 全事象

$$P(U) = 1$$

- 条件付き確率

$$P_A(B) = \frac{P(A \cap B)}{P(A)}$$

- 期待値

$$E(X)$$

- 確率変数を表す関数
    - 確率質量関数 (離散的)
    - 確率密度関数 (連続的)

- 正規分布 (ガウス分布)

$$f(x) = \frac{1}{\sqrt{2\pi}}e^{-\frac{x^2}{2}}$$
$$(標準正規分布の場合)$$

$$f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}exp\Bigl(-\frac{(x - \mu)^2}{2\sigma^2}\Bigr)$$
$$(一般的な正規分布の場合)$$

# Chapter 4

## NumPy

- ndarray.reshape((r, c))
- ndarray.ravel() # 参照を返す
- ndarray.flatten() # コピーを返す
- ndarray.dtype
- ndarray.astype(np.float16)
- ndarray.astype(np.int16)
- ndarray.copy() # 深いコピー

list: スライスの結果はコピー  
ndarray: スライスの結果は参照

- np.arange(10)
- np.arange(0, 10, 2)
- np.random.seed(123)
- np.random.random((3, 2))
- np.random.rand(3, 2)
- np.random.randint(0, 10, (3, 2))
- np.random.uniform(0.0, 10.0, size=(3, 2))
- np.random.randn(3, 2) # 標準正規分布
- np.random.normal(mean, sigma, (3, 2))
- np.zeros((3, 2))
- np.ones((3, 2))
- np.eye(3) # 単位行列
- np.full((3, 2), np.pi) # 全要素が円周率

np.nan: float 型

- np.linspace(0, 1, 5) # 0-1で等間隔に5要素
- np.diff(arr) # 要素間の差分が要素となる
- np.concatenate([arr1, arr2])
- np.concatenate([arr1, arr2], axis=1) # 横方向
- np.hstack([arr1, arr2]) # 横方向
- np.vstack([arr1, arr2]) # 縦方向
- arr1, arr2 = np.hsplit(arr3, [2])
    - arr1: 最初の2列, arr2: 残り
- arr1, arr2 = np.vsplit(arr3, [2])
    - arr1: 最初の2行, arr2: 残り
- ndarray.T
- ndarray[np.newaxis, :] # 行として次元を増やす
- ndarray[:, np.newaxis] # 列として次元を増やす
- xx, yy = np.meshgrid(x, y)
    - 各軸の値の配列から格子点を作り、座標を軸ごとに返す

### ユニバーサルファンクション

スカラーに対するのと同じ演算を ndarray にすると、各要素に適用される。

- np.abs(arr1) # 各要素の絶対値が要素となる
- arr1 / (arr2 + 1e-6) # ゼロ割りを避ける

### 判定・論理値

- np.count_nonzero(arr1) # True の要素数
- np.any(arr1 > 0) # 0より大きい要素があるか
- np.all(arr1 > 0) # 全要素が0より大きいか
- arr1[arr1 > 0] # 0より大きい要素のみ抽出
- np.allclose(arr1, arr2, atol=10) # 全要素の誤差が10以内か

## pandas

- sr = pd.Series([0, 1, 2])
- df = pd.DataFrame([[0, 'a', True], [1, 'b', False]])

DataFrame は、列ごとに dtype が決まる。  
1列に数値や文字列が混在するとオブジェクト型となり計算できなくなる。

- df.dtypes
- df.shape
- df.index
- df.columns

辞書形式で DataFrame を作る

- pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})

### 抽出

- df['A'] # 'A' 列の Series
- df[1] # 1列目の Series
- df[:2] # 0-1行目の DataFrame
- df.loc[:, :] # 同じ DataFrame (参照)
- df.loc[:, 'A'] # 'A' 列の Series
- df.loc[:, ['A', 'B']] # 'A', 'B' 列の DataFrame
- df.loc[0, :] # 0行目の Series
- df.iloc[0, 1] # 位置指定で要素抽出

### 入出力

- df = pd.read_csv('xx.csv', encoding='utf_8_sig')
- df = pd.read_excel('xx.xlsx')
- tables = pd.read_html(url)
df = tables[0]
- df.to_csv('xx.csv')
- df.to_excel('xx.xlsx')
- df.to_pickle('xx.pickle')
- df = pd.read_pickle('xx.pickle')

### 条件で抽出

- df['A'] >= 1000 # 'A' 列が1000以上かどうかの真理値の Series
- df1 = df[df['A'] >= 1000] # 'A' 列が1000以上の行の DataFrame
- df1 = df.query('A >= 1000 and B <= 1000')

### 並べ替え

- df = df.sort_values(by='A')
- df = df.sort_values(by='A', ascending=False)
- df = df.drop('A', axis=1)
- df = df.reset_index()

One-hot エンコーディング

- df1 = df.get_dummies(df.loc[:, 'B'], prefix='B')
'B_値' という列が値の種類だけ作られ、列の要素は1か0となる

### 時系列データ

- pd.date_range(start='2000_01_01', end='2000_01_31') # DatetimeIndex 型
- pd.date_range(start='2000_01_01', periods=365)

月の平均

- df.groupby(pd.Grouper(freq='M')).mean()
- df.resample('M').mean() # DataFrame を返す
- df.loc[:, 'A'].resample('M').mean() # Series を返す

### 欠損値

- df = df.dropna() # 欠損値の行を削除
- df = df.fillna(0) # 欠損値を0で置き換え
- df = df.fillna(method='ffill') # 前の行の値で置き換え
- df = df.fillna(df.mean()) # 平均値で置き換え
- df = df.fillna(df.median()) # 中央値で置き換え
- df = df.fillna(df.mode().iloc[0, :]) # 最頻値で置き換え

### 連結

- df = pd.concat([df1, df2], axis=0) # 縦方向
- df = pd.concat([df1, df2], axis=1) # 横方向

### 統計量

- count()
- mean()
- std()
- min()
- quantile([.25, .5, .75])
- max()
- corr() # カラム間の相関係数

### 散布図行列

```python
from pandas.plotting import scatter_matrix
_ = scatter_matrix(df)
```

### 変換

- df.values # ndarray に変換

## Matplotlib

- コードスタイル
    - MATLAB スタイル
    - オブジェクト指向スタイル

- グラフのスタイル
    - ggplot スタイルなど
    ```python
    import matplotlib.stype
    
    matplotlib.style.use('ggplot')
    ```

### MATLAB スタイル

```python
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 9]

plt.plot(x, y)
plt.title('グラフのタイトル')

plt.show()
```

### オブジェクト指向スタイル

```python
fig.ax = plt.subplots()
ax.plot(x, y)
ax.set_title('サブプロットのタイトル')

plt.show()
```

- 複数のサブプロットを配置する
    - fig, axes = plt.subplots(2)
    - fig, axes = plt.subplots(2, 2)
    - fig, axes = plt.subplots(ncols=2)

- 描画オブジェクトのタイトル
    - fig.suptitle('描画オブジェクトのタイトル')

- 軸ラベル
    - ax.set_xlabel('X 軸のラベル')
    - ax.set_ylabel('Y 軸のラベル')

- 凡例
    - ax.plot(x, y, label='凡例')
    - ax.legend(loc='best')

- ファイルに出力
    - fig.savefig('ファイル名.png')
    - fig.savefig('ファイル名.svg')

### グラフの種類

- 折れ線グラフ
    - ax.plot(x, y)

- 棒グラフ
    - ax.bar(x, y)
    - ax.bar(x, y, tick_label=['1', '2', '3']) # 目盛りラベル
    - ax.barh(x, y) # 横向き
- 2個の棒グラフ
    ```python
    width = 0.4
    ax.bar(x1, y1) # 1個め
    x2 = [i + width for i in x1]
    ax.bar(x2, y2) # 2個め
    ```
    - 積み上げグラフを描画するには、合計値から順に描画して重ねていく

- 散布図
    - ax.scatter(x, y) # デフォルトは丸
    - ax.scatter(x, y, marker='v') # 下向き三角

- ヒストグラム
    - n, bins, patches = ax.hist(x)
        - n: 度数の array
        - bins: 境界値の array
        - patches: 描画情報？の array
    - ax.hist(x, bins=20)
        - デフォルトは bins=10
    - ax.hist(x, orientation='horizontal') # 横向き
    - ax.hist((x1, x2), label=['1', '2']) # 2個
    - ax.hist((x1, x2), label=labels, stacked=True) # 積み上げ

- 箱ひげ図
    - ax.boxplot((x1, x2, x3), labels=labels)
    - ax.boxplot((x1, x2, x3), labels=labels, vert=False) # 横向き

    ※ labels が複数形 (凡例 (label) ではない)

- 円グラフ
    - ax.pie(x, labels=labels)
    - ax.axis('equal') # 楕円でなく円にする
    - pie() の引数
        - startangle=90 # 12時の方向から
        - counterclock=False # 時計回り
        - shadow=True # 影をつける
        - autopct='%1.2f%%' # %表記
        - explode=[0, 0.2, 0] # 2個目を飛び出し

### スタイル

- ax.plot(x, y, color=color)
    - color: 線の色 (名前, 16進数, RGBA値)
- ax.bar(x, y, color=color, edgecolor=ecolor)
    - edgecolor: 枠線の色
- ax.plot(x, y, linewidth=10)
    - linewidth: 線の太さ (pt)
- ax.plot(x, y, linestyle='--')
    - linestyle: 線の種類

ラベルのフォントの指定
- ax.set_xlabel('x', family='fantasy', size=20, weight='bold')
- ax.set_xlabel('x', fontdic={...})
    - まとめて指定して使い回せる
- ax.set_xlabel('x', fontdic={...}, size=40)
    - 直接指定した size が優先される

テキストの描画
- ax.text(0.2, 0.4, 'Text', size=20)

### pandas でグラフ描画

```python
import ...

matplotlib.style.use('ggplot')
df = pd.DataFrame({'A':[1, 2, 3], 'B':[2, 4, 6]})
df.plot() # 折れ線グラフ
plt.show()
```

- 1個のグラフに複数のデータを自動的に書き込む
- df.plot.bar() # 棒グラフ
- df.plot.bar(stacked=True) # 積み上げ棒グラフ
- df.plot.xx() で大体のグラフが描ける

## scikit-learn

### 前処理

- fit メソッドと transform メソッド
- または fit_transform メソッド

#### 欠損値

- pandas では
    - isnull メソッド
    - dropna メソッド
    - fillna メソッド
- scikit-learn
    - preprocessing モジュール
    - Imputer クラス
    - imp = Imputer(strategy='mean', axis=0)
    - imp.fit(df)
    - imp.transform(df) # (注意) 返り値は ndarray

#### エンコーディング

LabelEncoder クラス

- le = LabelEncoder()
- le.fit(db['列名'])
- le.transform(df['列名'])
    - 列の値を整数値に変換
- le.classes_
    - 0, 1, 2, ... に対応する元の値の配列

OneHotEncoder クラス

- pandas の get_dummies の方が使いやすい
- ohe = OneHotEncoder(categorical_features=[1])
    - 引数は、変換する列の位置のリスト
- ohe.fit_transform(df).toarray()
    - toarray() で scipy.sparse から ndarray に変換

#### 特徴量の正規化

分散正規化

- 平均が0、標準偏差が1となるよう正規化

$$x' = \frac{x - \mu}{\sigma}$$

StandardScaler クラス

- stdsc = StandardScaler()
- stdsc.fit(df)
- stdsc.transform(df)

最小最大正規化

- 最小値が0、最大値が1となるよう正規化

$$x' = \frac{x - x_{min}}{x_{max} - x_{min}}$$

MinMaxScaler クラス

- mmsc = MinMaxScaler()
- mmsc.fit(df)
- mmsc.transform(df)

#### 分類

- 学習は fit メソッド
- 予測は predict メソッド

学習データとテストデータに分ける

- model_selection モジュール
    - train_test_split 関数
    - 説明変数: ndarray や DataFrame
    - 目的変数: ndarray
    - test_size: テストデータの割合
    - random_state: 乱数シード

サポートベクタマシン

- 分類、回帰、外れ値検出
- カーネル (高次元空間での内積)
- 決定境界 (分類のための直線)
- サポートベクタ (各クラスのデータ)
- マージン (クラス間の距離)
