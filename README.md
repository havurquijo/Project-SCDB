# A Machine Learning App for Studying the U.S. Supreme Court Database
[![Static Badge](https://img.shields.io/badge/pypi-v1.0.1-blue)](https://pypi.org/project/SCDB-ML-app/1.0.1/)
[![Static Badge](https://img.shields.io/badge/license-APGL3.0-green)](https://github.com/havurquijo/Project-SCDB/blob/v1.0.1-alpha/LICENSE.txt)
[![Static Badge](https://img.shields.io/badge/data_analyzed%3A-SCDB-AD1313)](http://scdb.wustl.edu/about.php)
[![Static Badge](https://img.shields.io/badge/running_on%3A-AWS(ec2)-red)](http://18.222.133.83:5000/)

# Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
    1. [Running the App](#running-the-app)
    2. [Endpoints](#endpoints)
5. [Data](#data)
    1. [Dataset Description](#dataset-description)
    2. [Preprocessing](#preprocessing)
6. [Machine Learning Model](#machine-learning-model)
    1. [Model Selection](#model-selection)
    2. [Training the Model](#training-the-model)
    3. [Model Evaluation](#model-evaluation)
7. [Prediction](#prediction)
    1. [DecisionDirection Variable](#decisiondirection-variable)
    2. [Prediction Accuracy](#prediction-accuracy)
8. [Deployment](#deployment)
9. [Contributing](#contributing)
10. [License](#license)
11. [Contact](#contact)

# Introduction

This application leverages machine learning techniques to analyze the U.S. Supreme Court Database. Built with Python and Flask, this app utilizes the scikit-learn library, specifically the Decision Tree Classifier, to predict the variable `decisionDirection` with up to 96% accuracy. The primary goal of this project is to provide insights into the Supreme Court's decisions and to offer a predictive model for legal researchers, students, and enthusiasts.

By integrating Flask for the web framework and scikit-learn for machine learning, the application offers a user-friendly interface and robust analytical capabilities. Users can interact with the app to train the model and generate predictions based on the data provided by the Supreme Court site. This README.md provides detailed instructions on installation, usage, and the underlying methodologies used in this project.

This project is also deployd into a AWS server running online. See the link in the section befor the table of content (#a-machine-learning-app-for-studying-the-u.s.-supreme-court-database)


# Features

- **Historical Data Analysis**: Explore and analyze historical Supreme Court decisions using various filters and parameters (incoming in future releases).
- **Predictive Modeling**: Utilize the Decision Tree Classifier to predict the outcome of Supreme Court decisions (`decisionDirection` variable) with up to 96% accuracy. (In future releases, other machine learning models may be used).
- **Interactive Dashboard**: A user-friendly interface that allows users to interact with the data, view trends, and generate visualizations.
- **Data Visualization**: Generate charts and graphs to visualize decision trends, justice voting patterns, and other relevant statistics (incoming in future releases).
- **API Endpoints**: Access the application's features programmatically through well-documented API endpoints.
- **Custom Predictions**: Train the model with different parameters to generate custom predictions on Supreme Court decisions.
- **Model Insights**: Understand the model's decision-making process with feature importance and decision tree visualization.
- **Responsive Design**: Ensure the app is accessible on various devices, including desktops, tablets, and smartphones.
- **Documentation and Tutorials**: Provide comprehensive documentation and tutorials to help users understand and use the application effectively.


# Installation
You can install this application in your machine and access the webpage in your localhost by installig throught PyPi instller

```bash
pip install SCDB-ML-app
```

For installing an specific version use:
```bash
pip install SCDB-ML-app==1.0.0
```


# Usage
## Running the App
If installed you should import it and then run it into a python enviroment as:
```bash
import SCDB-ML-app
```

## Endpoints
List and describe the API endpoints available in the app.

# Data
## Dataset Description
Provide an overview of the U.S. Supreme Court Database, including the source and main variables.

## Preprocessing
Explain any data preprocessing steps performed before training the model.

# Machine Learning Model
## Model Selection
Discuss why the Decision Tree Classifier was chosen for this analysis.

## Training the Model
Describe the training process and parameters used.

## Model Evaluation
Present the evaluation metrics and how the model's performance was measured.

# Prediction
## DecisionDirection Variable
Explain what the decisionDirection variable represents.

## Prediction Accuracy
Detail the model's prediction accuracy and any validation methods used.

# Deployment
Instructions for deploying the Flask app to a production environment.

# Contributing
Guidelines for contributing to the project.

# License
Information about the project's license.

# Contact
Provide contact information for project maintainers or relevant contributors.

