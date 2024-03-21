# House Price Prediction Project

## Overview
This project aims to predict the selling prices of houses using a dataset that includes various features such as living area size, lot size, number of rooms, age of the house, and other relevant characteristics. By leveraging machine learning models, specifically Random Forest Regressor, we seek to provide accurate price estimates that could be valuable for both sellers and buyers in the real estate market.

## Part 1: Data Handling, EDA, and Model Development

### Data Collection and Cleaning
- **Dataset Overview:** The dataset is sourced from the Multiple Listing Service (MLS) covering house sales in and around Raleigh, NC. It represents a comprehensive compilation of house sales data, covering a wide range of properties with diverse characteristics, which provides a robust foundation for analyzing and predicting house selling prices.
  
- **Cleaning Process:** The dataset underwent thorough cleaning, including handling missing values and removing outliers based on Z-scores and IQR to ensure data quality.

### Exploratory Data Analysis (EDA)
- **Key Findings:** 

### Feature Engineering
- **Features Used:** Features like living area sqft, lot sqft, number of rooms, total baths, and binary features for amenities such as basements, garages, and waterfront access were utilized. County data was transformed into dummy variables to capture the location's effect on price.
- **Rationale:** These features were chosen based on their expected influence on house prices, informed by real estate market knowledge and preliminary data analysis.

### Model Development and Evaluation
- **Model Choice:** The Random Forest Regressor was chosen for its robustness and ability to handle the complex non-linear relationships inherent in real estate data. Configured with 100 trees and a random state of 42 to ensure reproducibility, this model is well-suited for our prediction tasks.

#### Initial Model Performance
The initial evaluation of the Random Forest model yielded the following metrics:
- **MSE (Mean Squared Error):** 1,538,645.86, which measures the average of the squares of the errors between predicted and actual values. This high value indicates variability in the model's predictions.
- **RMSE (Root Mean Squared Error):** 1,240.42, offering a more interpretable metric in the same units as the target variable. This suggests that, on average, the model's predictions deviate from the actual selling prices by about $1,240.
- **R² (R-squared):** 0.9999, representing the proportion of the variance in the dependent variable that is predictable from the independent variables. Nearly reaching 1, this indicates an exceptionally good fit of the model to the data.

These results demonstrate a strong performance, with the model accurately capturing the variance in the house selling prices.





## Part 2: Model Use and Customer Interface


## Written Analysis:

Our data set provides a comprehensive overview of residential property listings. Descriptive statistics reveal a diverse range of property characteristics: the mean selling price stands at approximately $320,263, with notable variability indicated by a standard deviation of around $108,650. Property sizes vary widely, with an average living area of 2029 square feet and an average lot size of 25,348 square feet. The dataset spans houses built across different years, resulting in an average house age of approximately 25 years. Properties typically offer around 3 bedrooms and 2.5 baths, with amenities like basements, garages, and waterfront access also considered.

Examining the frequency of property listings across counties, Wake County emerges with the highest frequency, followed by Johnston and Durham. Conversely, some counties show limited property listings, suggesting potential regional market variations or differing property availability. Visual analyses further highlight key insights: the selling price histogram exhibits a right-skewed distribution, indicating a majority of properties with lower prices and a few outliers with significantly higher prices. Correlation matrices and pair plots demonstrate meaningful relationships between numerical features and selling prices. For instance, larger living areas, more bedrooms, and additional baths correlate positively with higher selling prices.

Delving into specific property features, box plots showcase the influence of features like garages and waterfront access on selling prices, with properties possessing these features generally commanding higher prices. However, the presence of basements does not exhibit a clear impact on selling price variations. Finally, histograms offer a visual narrative of the distribution of various features such as living area, lot size, and house age, providing additional context to the dataset's composition. Overall, the analysis underscores the significance of property attributes and regional factors in shaping residential property prices within the dataset.

