# Student Performance Predictor

A machine learning system that predicts student academic performance based on workload, study habits, and lifestyle factors.

This project is designed around the reality of University of the People (UoPeople) students, who often balance multiple courses alongside other responsibilities.

---

## Overview

This project uses linear regression to model how different factors influence student performance. It goes beyond basic prediction by providing insights and recommendations based on the results.

The system simulates a real-world data workflow: data → model → prediction → interpretation → storage.

---

## Features

- Predicts academic performance using:
  - Number of courses taken
  - Weekly study hours
  - Assignment workload intensity
  - Sleep duration

- Model evaluation using R² score

- Insight system explaining performance factors

- Recommendation system for improvement

- CSV export to store predictions for further analysis

---

## Example Output

```
Model Accuracy (R²): 0.82

--- Prediction ---
Courses Taken: 4
Study Hours/Week: 25
Assignment Load: 9/10
Sleep Hours: 5

Predicted Score: 78.40

--- Insight ---
Taking maximum course load increases academic pressure.
High study hours positively impact performance.
Heavy assignment load may affect consistency and stress levels.
Low sleep can negatively affect performance despite effort.

Recommendation:
Balance study, workload, and sleep for optimal performance.
```

## Project Structure

```
student-performance-predictor/
│── dataset.csv
│── model.py
│── main.py
│── requirements.txt
│── predictions.csv
```
