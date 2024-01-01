import xgboost as xgb
from xgboost import XGBClassifier

# https://xgboost.readthedocs.io/en/stable/tutorials/categorical.html
def stock_boost(X_train, y_train, X_test):
    bst = XGBClassifier(n_estimators=2, max_depth=2, learning_rate=1, objective='binary:logistic')
    # fit model
    bst.fit(X_train, y_train)
    # make predictions
    return bst.predict(X_test)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("PyCharm")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
