import re
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from io import StringIO
import os.path


# Removes the dividers and URLs from the text that will be vectorized
def filter_text(text):
    text = re.sub(r'\|\|\|', r' ', text)
    text = re.sub(r'http\S+', r' ', text)
    return text


'''
Takes in a string that represents a user's text that they inputted.
Returns a string representation of the personality type based on the parameter
The function creates a logistic regression model that predicts
personality-type after being trained with a dataset
'''


def logistic_regression(msg):

    # Formats the text to be converted to a pandas dataframe
    text = f"""Post
    {msg}
    """
    StringData = StringIO(text)
    message = pd.read_csv(StringData)

#   Loads file with pandas and then filters the posts
    SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
    file = pd.read_csv(SITE_ROOT + '/mbti_1.csv')
    file['filtered'] = file['posts'].apply(filter_text)

#   Splits the dataset into training and testing sets
    train, test = train_test_split(file, test_size=0.2)
    X_train = train['filtered']
    Y_train = train['type']
    X_test = test['filtered']
    Y_test = test['type']

#   Creates a CountVectorizer that can convert the text to token counts
    c_vectorizer = CountVectorizer(ngram_range=(1, 1), stop_words='english')

#   Vectorizes the posts in the training, testing, and message
    X_train = c_vectorizer.fit_transform(X_train)
    X_test = c_vectorizer.transform(X_test)
    message = c_vectorizer.transform(message)

#   Creates a logistic regression model
    lr_model = LogisticRegression(class_weight="balanced", C=0.01,
                                  max_iter=7500, n_jobs=-1)

#   Fitting the model to the training data
    lr_model.fit(X_train, Y_train)

#   Making predictions with the model
    y_pred = lr_model.predict(X_test)
    text_pred = lr_model.predict(message)
    score = accuracy_score(Y_test, y_pred)
    print(f'Accuracy: {score}')

#   Returns the string representation of the personality type
    return str(text_pred[0])
