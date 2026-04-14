
from model import train_model, predict
import pandas as pd


def run():
    print("UoPeople Student Performance Predictor\n")

    model, accuracy = train_model()

    print(f"Model Accuracy (R²): {accuracy:.2f}")

    # Your real scenario
    courses = 4
    study_hours = 25
    assignment_load = 9
    sleep_hours = 5

    predicted_score = predict(model, courses, study_hours, assignment_load, sleep_hours)

    print("\n--- Prediction ---")
    print(f"Courses Taken: {courses}")
    print(f"Study Hours/Week: {study_hours}")
    print(f"Assignment Load: {assignment_load}/10")
    print(f"Sleep Hours: {sleep_hours}")

    print(f"\nPredicted Score: {predicted_score:.2f}")

    # --- SAVE TO CSV (NEW ADDITION) ---
    result = pd.DataFrame({
        "Courses": [courses],
        "StudyHours": [study_hours],
        "AssignmentLoad": [assignment_load],
        "SleepHours": [sleep_hours],
        "PredictedScore": [predicted_score]
    })

    # Save (append mode for multiple runs)
    try:
        result.to_csv("predictions.csv", mode='a', header=False, index=False)
    except FileNotFoundError:
        result.to_csv("predictions.csv", index=False)

    print("\nSaved prediction to predictions.csv")

    # Insight System (this is what makes it strong)
    print("\n--- Insight ---")

    if courses == 4:
        print("Taking maximum course load increases academic pressure.")

    if study_hours >= 25:
        print("High study hours positively impact performance.")

    if assignment_load >= 8:
        print("Heavy assignment load may affect consistency and stress levels.")

    if sleep_hours < 6:
        print("Low sleep can negatively affect performance despite effort.")

    print("\nRecommendation:")
    print("Balance study, workload, and sleep for optimal performance.")


if __name__ == "__main__":
    run()

    