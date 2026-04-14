
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from model import train_model, predict

st.title("UoPeople Student Performance Dashboard")

# Load dataset
data = pd.read_csv("dataset.csv")

# Train model
model, accuracy = train_model()

st.write(f"Model Accuracy (R²): {accuracy:.2f}")

# Show dataset
st.subheader("Dataset Overview")
st.write(data.head())

# Input section
st.header("Enter Your Study Data")

# 🔥 Improved layout (2 columns)
col1, col2 = st.columns(2)

with col1:
    courses = st.slider("Courses Taken", 1, 4, 4)
    study_hours = st.slider("Study Hours per Week", 0, 40, 25)

with col2:
    assignment_load = st.slider("Assignment Load (1–10)", 1, 10, 9)
    sleep_hours = st.slider("Sleep Hours per Day", 0, 10, 5)

if st.button("Predict Performance"):
    predicted_score = predict(model, courses, study_hours, assignment_load, sleep_hours)

    # 🔥 Metrics (clean professional look)
    st.subheader("Performance Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Predicted Score", f"{predicted_score:.2f}")

    with col2:
        avg_score = data["score"].mean()
        st.metric("Average Score", f"{avg_score:.2f}")

    # Insights
    st.subheader("Insights")

    if courses == 4:
        st.write("Taking maximum course load increases academic pressure.")

    if study_hours >= 25:
        st.write("High study hours positively impact performance.")

    if assignment_load >= 8:
        st.write("Heavy assignment load may affect stress levels.")

    if sleep_hours < 6:
        st.write("Low sleep can negatively affect performance.")

    # Recommendation
    st.subheader("Recommendation")
    st.write("Balance study, workload, and sleep for optimal performance.")

    # 🔥 Improved chart (with your prediction highlighted)
    st.subheader("Performance Trends")

    fig, ax = plt.subplots()

    ax.scatter(data["study_hours_per_week"], data["score"], label="Dataset")
    ax.scatter(study_hours, predicted_score, color='red', label='Your Prediction')

    ax.set_xlabel("Study Hours")
    ax.set_ylabel("Performance Score")
    ax.legend()

    st.pyplot(fig)
    