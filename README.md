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
- Features Used: Features like living area sqft, lot sqft, number of rooms, total baths, and binary features for amenities such as basements and garages, were utilized. County data was transformed into dummy variables to capture the location's effect on price.
- Rationale: These features were chosen based on their expected influence on house prices, informed by real estate market knowledge and preliminary data analysis.
- Utilized VIF testing to ensure against multicollinearity among features.

### Model Training and Evaluation
- **Random Forest Regressor:**  The Random Forest Regressor was chosen for its robustness and ability to handle the complex non-linear relationships inherent in real estate data. Configured with 100 trees and a random state of 42 to ensure reproducibility, this model is well-suited for our prediction tasks. The initial evaluation of the Random Forest Model yielded a RMSE of 1,240.42 and a R² of .9999.
- **Cross-Validation:** Used 10-Fold-Cross-Validation to ensure the model's performance is robust and generalizable across different data samples.
- **Model Export:** The final model is saved as a `.joblib` file for integration with the Flask application.
- **Model Download:** https://1drv.ms/f/s!AjRAg4mNHj8RgijFeSOIHquV1M7c?e=5CfPQ5

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



### General Data Analysis
Our data set provides a comprehensive overview of residential property listings. Descriptive statistics reveal a diverse range of property characteristics: the mean selling price stands at approximately $320,263, with notable variability indicated by a standard deviation of around $108,650. Property sizes vary widely, with an average living area of 2029 square feet and an average lot size of 25,348 square feet. The dataset spans houses built across different years, resulting in an average house age of approximately 25 years. Properties typically offer around 3 bedrooms and 2.5 baths, with amenities like basements, garages, and waterfront access also considered.

Examining the frequency of property listings across counties, Wake County emerges with the highest frequency, followed by Johnston and Durham. Conversely, some counties show limited property listings, suggesting potential regional market variations or differing property availability. Visual analyses further highlight key insights: the selling price histogram exhibits a right-skewed distribution, indicating a majority of properties with lower prices and a few outliers with significantly higher prices. Correlation matrices and pair plots demonstrate meaningful relationships between numerical features and selling prices. For instance, larger living areas, more bedrooms, and additional baths correlate positively with higher selling prices.

Delving into specific property features, box plots showcase the influence of features like garages and waterfront access on selling prices, with properties possessing these features generally commanding higher prices. However, the presence of basements does not exhibit a clear impact on selling price variations. Finally, histograms offer a visual narrative of the distribution of various features such as living area, lot size, and house age, providing additional context to the dataset's composition. Overall, the analysis underscores the significance of property attributes and regional factors in shaping residential property prices within the dataset.
