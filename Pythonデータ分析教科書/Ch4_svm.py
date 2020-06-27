# %% ライブラリ、関数

import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

def plot_boundary_margin_sv(X0, y0, X1, y1, kernel,
        C, xmin=-1, xmax=1, ymin=-1, ymax=1):
    
    # モデルインスタンス
    svc = SVC(kernel=kernel, C=C)
    # 学習
    svc.fit(np.vstack((X0, X1)), np.hstack((y0, y1)))
    
    # グラフの準備
    fig, ax = plt.subplots()
    ax.scatter(X0[:, 0], X0[:, 1], marker='o', label='class 0')
    ax.scatter(X1[:, 0], X1[:, 1], marker='x', label='class 1')
    
    # 格子点
    grid_x = np.linspace(xmin, xmax, 100)
    grid_y = np.linspace(ymin, ymax, 100)
    xx, yy = np.meshgrid(grid_x, grid_y)
    # 各要素が (x, y) である配列を作る
    xy = np.vstack([xx.ravel(), yy.ravel()]).T
    # 各点のスコアを一括で求め、格子状に配置
    p = svc.decision_function(xy).reshape((100, 100))
    
    # 格子点における p の値 (スコア) で等高線を描画
    ax.contour(xx, yy, p,
        colors='k', levels=[-1, 0, 1],
        alpha=0.5, linestyles=['--', '-', '--'])
    
    # サポートベクタをプロット
    sv_x = svc.support_vectors_[:, 0]
    sv_y = svc.support_vectors_[:, 1]
    ax.scatter(sv_x, sv_y,
        s=250, facecolors='none',
        edgecolors=['black'])
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend(loc='best')
    plt.show()


# %% データの準備

# クラス 0 のデータとラベル
X0 = np.random.uniform(size=(100, 2))
y0 = np.repeat(0, 100)

# クラス 1 のデータとラベル
X1 = np.random.uniform(-1.0, 0.0, size=(100, 2))
y1 = np.repeat(1, 100)

fig, ax = plt.subplots()
ax.scatter(X0[:, 0], X0[:, 1], marker='o', label='class 0')
ax.scatter(X1[:, 0], X1[:, 1], marker='x', label='class 1')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
plt.show()


# %% マージンを小さめに取った場合

plot_boundary_margin_sv(X0, y0, X1, y1,
    kernel='linear', C=1e6)


# %% マージンを大きめに取った場合

plot_boundary_margin_sv(X0, y0, X1, y1,
    kernel='linear', C=0.1)


# %% 直線で分離できないデータ

X = np.random.random(size=(100, 2))
y = (X[:, 1] > 2 * (X[:, 0] - 0.5) ** 2 + 0.5).astype(int)

fig, ax = plt.subplots()
ax.scatter(X[y == 0, 0], X[y == 0, 1],
    marker='x', label='class 0')
ax.scatter(X[y == 1, 0], X[y == 1, 1],
    marker='o', label='class 1')
ax.legend()
plt.show()

# %% カーネルとして動径基底関数を使用

X0, X1 = X[y == 0, :], X[y == 1, :]
y0, y1 = y[y == 0], y[y == 1]

plot_boundary_margin_sv(X0, y0, X1, y1,
    kernel='rbf', C=1e3, xmin=0, ymin=0)


# %%
