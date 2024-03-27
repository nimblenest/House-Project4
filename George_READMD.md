# Real Estate Value Estimator

## Overview
The Real Estate Value Estimator is an advanced web application designed to predict property values based on various parameters. Utilizing a robust Flask backend, PostgreSQL for data storage, and a machine learning model, this application provides users with accurate property value estimations.

## Features
- **Accurate Property Value Predictions:** Users can input detailed property information to receive precise value estimations.
- **Data-Driven Insights:** Leveraging a Random Forest model trained on comprehensive real estate data, the application ensures reliable estimations.
- **User-Friendly Interface:** Dynamic web forms with dropdowns populated from the database allow for easy data input.

## Installation and Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.6 or newer
- PostgreSQL
- Flask
- Python libraries as listed in `requirements.txt`

### Installation
1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd Real-Estate-Value-Estimator
   ```

2. **Install Dependencies:**
   Install the required Python libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration
- **Database Setup:** Ensure PostgreSQL is running. Configure the connection details in both `Flask.py` and the Jupyter notebook according to your local or hosted PostgreSQL server.
- **Model Setup:** Place the trained machine learning model file (`random_forest_model.joblib`) in the appropriate directory for the Flask application to access.

## Data Analysis and Model Training
The provided Jupyter notebook (`house-sales-analysis-ML.ipynb`) contains detailed exploratory data analysis (EDA) and the model training process.

### Exploratory Data Analysis (EDA)
- **Data Loading:** Data is fetched from a PostgreSQL database into a pandas DataFrame.
- **Statistical Analysis:** Includes descriptive statistics, distribution analysis, and outlier detection.
- **Visualization:** Histograms, box plots, and scatter plots are used to understand data characteristics and relationships.

### Feature Engineering
- Encoding categorical variables and normalizing numerical features to prepare the dataset for machine learning.

### Model Training and Evaluation
- **Random Forest Regressor:** Selected for its ability to handle non-linear relationships and interactions between features.
- **Cross-Validation:** Used to ensure the model's performance is robust and generalizable across different data samples.
- **Model Export:** The final model is saved as a `.joblib` file for integration with the Flask application.

## Running the Web Application

1. **Start the Flask Server:**
   Navigate to the project's root directory and run:
   ```bash
   python Flask.py
   ```
   This will start the Flask server on `localhost` with port `5000`.

2. **Accessing the Application:**
   Open a web browser and go to `http://localhost:5000/` to view and interact with the application.

## Usage
- On the web application, fill in the property details form and submit to get an estimated property value. The form includes fields such as county, square footage, number of bedrooms and bathrooms, and more, reflecting the comprehensive nature of the estimation process.
