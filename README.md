# Heart Disease Risk Prediction Using Random Forest Classification

## Overview
This project aims to predict the likelihood of heart disease in patients based on a range of health metrics using the **Random Forest Classification** algorithm. The model is trained on the Heart Disease dataset and provides an accurate and reliable prediction, helping medical professionals in identifying at-risk patients early on.

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Results](#results)
- [Contributing](#contributing)


## Dataset
The dataset used for this project contains patient data with several features that are used to predict heart disease. The dataset includes:
- Age
- Sex
- Chest Pain Type (4 values)
- Resting Blood Pressure
- Serum Cholesterol in mg/dl
- Fasting Blood Sugar > 120 mg/dl
- Resting Electrocardiographic Results
- Maximum Heart Rate Achieved
- Exercise Induced Angina
- ST Depression Induced by Exercise
- Slope of Peak Exercise ST Segment
- Number of Major Vessels Colored by Fluoroscopy
- Thalassemia (3 values)

**Target Variable:**
- Presence of Heart Disease (binary classification: 0 for No, 1 for Yes)

## Model Training
The Random Forest model was trained in the Heart Disease Risk Prediction.ipynb notebook. The steps include:

+ Data Preprocessing: Handling missing values, encoding categorical variables, scaling features.
+ Model Training: Training the model using a Random Forest Classifier.
+ Model Evaluation: Using metrics such as accuracy, precision, recall, and AUC to evaluate the model performance.
+ The trained model is saved as random_forest_model.pkl for use in the Streamlit application.

## Results
The Random Forest model provides an accuracy of approximately 85% on the test set. Below are other evaluation metrics:

+ Accuracy: 85%
+ Precision: 83%
+ Recall: 82%
+ F1-Score: 82%
+ AUC: 0.88
These results indicate that the model is effective in predicting the risk of heart disease.

## Contributing
Contributions are welcome! If you find any issues or have suggestions, feel free to open an issue or submit a pull request.
