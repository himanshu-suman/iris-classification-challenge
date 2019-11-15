from sklearn.datasets import load_iris
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def iris_model():
    iris_df = load_iris()
    x = iris_df.data
    y = iris_df.target

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    model = DecisionTreeClassifier()
    model.fit(x_train, y_train)

    pred = model.predict(x_test)

    accuracy = accuracy_score(y_test, pred)

    joblib.dump(model, "iris_model.model")

    print("Model is Trained.")
    print("Accuracy obtained : {}".format(accuracy))
