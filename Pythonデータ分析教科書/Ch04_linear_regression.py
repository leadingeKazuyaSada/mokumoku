# %%
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split


# %% Boston データセットを読み込む
boston = load_boston()
X, y = boston.data, boston.target

# 学習データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3
)


# %% 学習
lr = LinearRegression()
lr.fit(X_train, y_train)


# %% 予測
y_pred = lr.predict(X_test)


# %% 可視化
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.scatter(y_pred, y_test)

# 基準線
ax.plot((0, 50), (0, 50), linestyle='dashed', color='red')
# ラベル
ax.set_xlabel('predicated value')
ax.set_ylabel('actual value')

# 描画
plt.show()


# %%
