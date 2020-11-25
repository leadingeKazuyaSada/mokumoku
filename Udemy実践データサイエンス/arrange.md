## セクション 1-3

- Canopy はもうダウンロードできない
- やっていること
    - Canopy をインストール
    - scikit-learn をインストール
    - xlrd をインストール
    - statsmodels をインストール
    - pydot2 をインストール
- 自分はどうやったか
    - pipenv install
    - pipenv install scikit-learn
        - 機械学習
    - pipenv install xlrd
        - エクセル読み書き
    - pipenv install statsmodels
        - 解析
    - pipenv install pydot2
        - グラフ描画
- さらに足りない (Canopy には入ってる) package を追加
    - pipenv install jupyterlab
        - Jupyter notebook の代わり
    - pipenv install matplotlib
        - グラフ描画


## 以降の読み替え

- 「.ipynb ファイルをダブルクリック」の読み替え
    1. pipenv run jupyter lab して、
    2. 開いた JupyterLab のエクスプローラからそのファイルを選択
    3. Kernel を聞かれるので Python 3 を選択
    4. あとは教材で Jupyter notebook でやっているのと同様に実行

- コード内の print 文
    - print(...) の形にする
    - 改行したくない時は、',' をつけるのでなく、", end=' '" をつける
        - before: print x,
        - after:  print(x, end='')

- `MatPlotLib.ipynb` でグラフを画像として保存する時
    - `plt.savefig` の引数 (保存先パス) が 'C:\\JupiterImages\\MyPlot.png' のままだと、保存できない。
    - 書き込み権限のあるフォルダにする (例: 'C:\\Users\\sata\\Pictures\\MyPlot.png')。
- 決定木を描画する時
    - `sklearn.externals.six` の代わりに `six` をインポートする。
    - `pydot` の代わりに `pydotplus` をインポートする。
- 「38.類似映画の取得」で、u.item というファイルが UTF-8 で使えない文字を使っている。エンコードを変えて (Shift-JIS とか) 保存し直せば OK。
- `sklearn` の `cross_validation` の代わりに `model_selection` を使うこと。

- ビデオでは Jupyter Notebook の Tools メニューから　Canopy Command Prompt を実行しているが、Jupyter Lab にはそのメニューはないし、Canopy もインストールしていないので、普通に PowerShell から仮想環境に入って `spark-submit` を実行する。

- pyspark の mllib の KMeans で、KMeans.train() のキーワード引数 `runs` は、Spark 2.2.0 から無くなった (指定しなくて OK)。

## 補足

- arange() を「アレンジ関数」と言っているけど、たぶん「エーレンジ」(array-range)。
- 二項分布とかの説明がないのはどうかと思うけど、ググって勉強しましょう。
- 「凡例」のことを「ぼんれい」と言っている。
- R-二乗値の説明で、「偏差の二乗和」のことを「分散の二乗和」と言っている。
- 多変量回帰で `pd.Categorical()` を使っているのが良くない。Q&A で指摘されていたが、講師も分かってない。 `get_dummies` を使った方が良いと思う。
- 映画を財産で分類するという例があったが、おそらく小道具 (Prop) の間違い。英語の資料を翻訳したものらしい。
- 「40.映画のレコメンドを行う」で、おすすめ度のリストに同じ映画が複数回出ていることの説明が、「ユーザが評点した映画が2つ以上の映画と似ていたため」と言っているが、正しくは「ユーザが評価した映画のうち2つ以上の映画が、同じ映画と似ていたため」。
    - 複数回出たからといって足して良いのかというのも気になる。
- 「43.KNN で映画の評価を予測する」で、「人気度」「人気の高い」と言っているのは popularity (評価の値に関わらず、投票数の多さ) のことと思われる。
- KNN.ipynb で、`map(int, genres)` となっている箇所を `list(map(int, genres))` にする必要がある。
