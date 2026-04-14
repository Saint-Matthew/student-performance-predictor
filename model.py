
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def train_model():
    data = pd.read_csv("dataset.csv")

    X = data[["courses", "study_hours_per_week", "assignment_load", "sleep_hours"]]
    y = data["score"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    return model, accuracy


def predict(model, courses, study_hours, assignment_load, sleep_hours):
    prediction = model.predict([[courses, study_hours, assignment_load, sleep_hours]])
    return prediction[0]

