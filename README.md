# iris_dataset

The Iris flower data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. The data set consists of 50 samples from each of three species of Iris (Iris Setosa, Iris virginica, and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters.

This project consists of 2 parts:
1. Firstly a jupyter notebook, where I have trained my iris model to classify Iris-Setosa, Iris-Virginica, and Iris-Versicolor using [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html).
2. In building_api_for_iris folder, I have trained and created a RESTful API to classify Iris-Setosa, Iris-Virginica, and Iris-Versicolor. Here, the model is trained using the [DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html). I have used [flask-restful](https://flask-restful.readthedocs.io/en/latest/) module to create API for the same.

I have used [POSTMAN](https://www.getpostman.com/) as my API client to send requests and inspect the response.

Response:

![Postman Response](/building_api_for_iris/response_from_postman.png)
