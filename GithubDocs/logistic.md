To perform logistic regression

1. If haven't, install sklearn package
```
    pip install sklearn
```

2. Set up your variables and target vectors, a preferred way is to implement a function  ```load_data``` that return a X matrix and y vector, with the same number of rows:
```
    X, y = load_data()
```
In our context, X is the predicting variables, different columns represent different features. Say first column is rank differences, second column is home-guest binary indicator, and so on.

3. Create a logistic regression model, and fit it
```
logreg = LogisticRegression()
logreg.fit(X, y)
```

4. You can see the coefficients of each feature and the fitted constant by 
```
logreg.coef_
```

5. To check how accurate the model is, can also perform ```.score``` function of the model on test data.


```
accuracy = logreg.score(X_test, y_test)
print("Accuracy:", accuracy)
```

Test data need to be disjoint from the training data. A common practice is splitting the original data by the following code. 
```
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```
Train the model on the ```X_train, y_train``` and test on ```X_test, y_test```.

You can specify the ```test_size```, which is how much fraction of the original data would test data. A default choice is ```0.2```.

6. Besides from the Brier score for probability output. There are many other metrics one may perform on binary output, including precision, recall, F1-score and area under ROC curve.

```
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
```
The above four metrics all comes from the confusion matrix. You many want to look up the notions to understand what each metric is measuring.

The area under ROC curve is less direct, but is a good metric for binary output. Look it up if interested.

7. Models may suffer from overfitting if given too many variables. This would not be a concern if we are using just a few variables. When overfitting happens, it is a good practice to prevent it by performing cross validation and regularization. We would discuss that if necessariy.
