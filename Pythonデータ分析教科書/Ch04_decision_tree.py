# %%
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# データ準備
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3)


# %% 学習
tree = DecisionTreeClassifier(max_depth=3)
tree.fit(X_train, y_train)


# %% 木を描画
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz

dot_data = export_graphviz(tree, filled=True,
    rounded=True,
    class_names=[
        'Setosa',
        'Versicolor',
        'Virginica'],
    feature_names=[
        'Sepal Length',
        'Sepal Width',
        'Petal Length',
        'Petal Width'],
    out_file=None)

graph = graph_from_dot_data(dot_data)
graph.write_png('tree.png')


# %% 予測
y_pred = tree.predict(X_test)
y_pred


# %% ランダムフォレスト
from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(n_estimators=100)


# %% 学習
forest.fit(X_train, y_train)


# %% 予測
y_pred = forest.predict(X_test)
y_pred


# %%
