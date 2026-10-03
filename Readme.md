# BodyIndex AI 🧠✨

> An AI-powered web application that predicts a Body Index category using Gender, Height, and Weight.

## 🌐 About the Project

**BodyIndex AI** is a machine learning based web application built with Python and Streamlit.

The application takes three inputs:

- 👤 Gender
- 📏 Height (cm)
- ⚖️ Weight (kg)

and uses a trained machine learning classification model to predict the corresponding **Body Index category**.

The project provides a modern, interactive and animated user interface designed to make the prediction process simple and user-friendly.

---

## 🚀 Features

- 🎯 Machine learning based classification
- 👤 Gender-based input
- 📏 Height and weight input
- ⚡ Instant prediction
- 🎨 Modern pastel dark-theme interface
- ✨ Animated user interface
- 📊 Easy-to-understand prediction result
- 🖥️ Interactive Streamlit web application
- 🤖 Trained classification model
- 📦 Saved model and scaler using Joblib

---

## 🧠 Body Index Categories

The application predicts one of the following categories:

| Index | Category |
|------:|----------|
| 0 | Extremely Weak |
| 1 | Weak |
| 2 | Normal |
| 3 | Overweight |
| 4 | Obesity |
| 5 | Extreme Obesity |

> **Note:** These categories represent the classes present in the dataset used for this machine learning project and should not be interpreted as a medical diagnosis.

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **NumPy**
- **Scikit-learn**
- **Joblib**
- **Machine Learning**

---

## 🤖 Machine Learning Workflow

The project follows this workflow:

```text
Dataset
   ↓
Data Preprocessing
   ↓
Feature Encoding
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
Machine Learning Models
   ↓
Model Evaluation
   ↓
Best Model Selection
   ↓
Model Serialization
   ↓
Streamlit Web Application
   ↓
Prediction