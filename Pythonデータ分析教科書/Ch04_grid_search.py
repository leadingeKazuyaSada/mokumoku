# %% インポート
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


# %% データをロード
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3
)


# %% 決定木で交差検証
clf = DecisionTreeClassifier()

# 試したいパラメタを dict にする
param_grid = {'max_depth': [3, 4, 5]}

# 10分割の交差検証
cv = GridSearchCV(clf, param_grid=param_grid, cv=10)
cv.fit(X_train, y_train)

# 最適な深さ
print('最適な深さ')
print(cv.best_params_)

# 最適なモデル
print('最適なモデル')
print(cv.best_estimator_)



# %%
