# Heart Disease Prediction

A Machine Learning classification project that predicts the likelihood of heart disease based on clinical and demographic features.

The project covers the complete ML workflow — from data exploration and preprocessing to model experimentation and deployment preparation.

## Project Overview

Heart disease is one of the major health concerns worldwide. This project uses machine learning classification techniques to analyze patient-related features and predict whether a patient belongs to:

* **0 → Lower likelihood of heart disease**
* **1 → Higher likelihood of heart disease**

> **Disclaimer:** This project is for educational and demonstration purposes only. It is not a medical diagnostic tool and should not be used as a substitute for professional medical advice.

## Objectives

* Understand and explore a heart disease dataset
* Perform data cleaning and exploratory data analysis
* Identify and remove duplicate records
* Analyze numerical features and potential outliers
* Prepare numerical and categorical features
* Apply appropriate preprocessing techniques
* Experiment with multiple classification algorithms
* Compare model performance using evaluation metrics
* Build a reusable ML pipeline
* Prepare the final model for deployment

## Dataset

The dataset contains 1,025 records and the following features:

| Feature    | Description                           |
| ---------- | ------------------------------------- |
| `age`      | Age of the patient                    |
| `sex`      | Sex of the patient                    |
| `cp`       | Chest pain type                       |
| `trestbps` | Resting blood pressure                |
| `chol`     | Serum cholesterol                     |
| `fbs`      | Fasting blood sugar                   |
| `restecg`  | Resting electrocardiographic results  |
| `thalach`  | Maximum heart rate achieved           |
| `exang`    | Exercise-induced angina               |
| `oldpeak`  | ST depression induced by exercise     |
| `slope`    | Slope of the peak exercise ST segment |
| `ca`       | Number of major vessels               |
| `thal`     | Thalassemia-related feature           |
| `target`   | Prediction target                     |

### Target

```text
0 → Lower likelihood of heart disease
1 → Higher likelihood of heart disease
```

## Exploratory Data Analysis

The project includes analysis of:

* Dataset shape and structure
* Data types
* Missing values
* Statistical summaries
* Target distribution
* Feature distributions
* Correlations
* Categorical feature distributions
* Numerical feature outliers

Visualizations were created using:

* Matplotlib
* Seaborn

## Data Cleaning

During data exploration, duplicate records were identified and removed before the final modeling workflow.

The cleaned dataset was then used for the final train/test split and model development.

## Data Preprocessing

Different preprocessing techniques were applied according to feature type.

### Numerical Features

* Missing value imputation using median
* Standardization using `StandardScaler`

### Categorical Features

* Missing value imputation using most frequent value
* One-hot encoding using `OneHotEncoder`
* `handle_unknown="ignore"` to make the preprocessing pipeline robust to unseen categories

### Pipeline

The preprocessing workflow is implemented using:

* `Pipeline`
* `ColumnTransformer`
* `SimpleImputer`
* `StandardScaler`
* `OneHotEncoder`

This keeps preprocessing and model prediction together and helps prevent data leakage.

## Machine Learning Models

Multiple classification algorithms were experimented with during the project, including:

* Logistic Regression
* K-Nearest Neighbors (KNN)
* Decision Tree
* Random Forest
* Naive Bayes
* Support Vector Machine (SVM)

The models were evaluated using appropriate classification metrics rather than relying only on accuracy.

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* ROC-AUC

## Project Workflow

```text
Raw Dataset
     ↓
Data Understanding
     ↓
Exploratory Data Analysis
     ↓
Duplicate Detection & Removal
     ↓
Outlier Analysis
     ↓
Feature / Target Separation
     ↓
Train-Test Split
     ↓
Numerical + Categorical Preprocessing
     ↓
Multiple ML Models
     ↓
Model Evaluation
     ↓
Final Model
     ↓
ML Pipeline
     ↓
Model Serialization
     ↓
Streamlit Application
     ↓
Deployment
```

## Project Structure

```text
Heart-Disease-Prediction/
│
├── data/
│   └── heart.csv
│
├── notebooks/
│   └── heart_disease_prediction.ipynb
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

> File names may differ depending on the final project structure.

## Application

The project is being prepared as an interactive Streamlit application where users can enter patient-related feature values and receive a model prediction.

The application is intended to demonstrate how a trained machine learning model can be integrated into a simple user-facing interface.

## Technologies Used

### Programming Language

* Python

### Data Analysis

* NumPy
* Pandas

### Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn

### Deployment

* Streamlit

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Heart-Disease-Prediction.git
```

### 2. Navigate to the project

```bash
cd Heart-Disease-Prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## Requirements

Example `requirements.txt`:

```text
numpy
pandas
matplotlib
seaborn
scikit-learn
streamlit
joblib
```

Use the versions from your actual environment if you have them pinned.

## Results

Multiple machine learning models were trained and compared after preprocessing and duplicate removal.

The final model was selected based on the project's evaluation results, considering multiple classification metrics rather than accuracy alone.

Final performance values will be added after the final evaluation of the deployment-ready pipeline.

## Future Improvements

Possible future improvements include:

* Hyperparameter tuning
* Cross-validation
* ROC curve visualization
* Improved Streamlit UI
* Better input validation
* Model monitoring
* Explainable AI techniques such as SHAP
* Improved deployment infrastructure

## Author

**Arooba Ali**

Aspiring Machine Learning Engineer focused on Python, Machine Learning, Data Science, and practical ML projects.

### Skills Demonstrated

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Exploratory Data Analysis
* Data Preprocessing
* Feature Engineering
* Machine Learning
* Model Evaluation
* Streamlit

## Project Status

**Completed ML workflow — deployment-ready / deployment in progress.**

This project was developed as part of a practical journey toward building real-world Machine Learning applications.
