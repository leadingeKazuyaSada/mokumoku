#%%
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target

print('X:')
print(X[:5, :])

print('y:')
print(y[:5])

# %%
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test \
    = train_test_split(X, y, test_size=0.3)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


# %%
