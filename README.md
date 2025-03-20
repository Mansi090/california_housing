# California Housing Price Prediction

## 📌 Project Overview
This project analyzes the **California housing dataset** and builds predictive models to estimate house prices based on various features. The dataset contains information such as population, median income, and location-based attributes that influence housing prices. The project involves **data preprocessing, exploratory data analysis (EDA), and machine learning model implementation** to predict housing prices effectively.

## 📂 Dataset Details
The dataset used in this project comes from the **California housing data** available in the Scikit-Learn library. It includes:
- **Longitude & Latitude**: Geographic coordinates of the houses.
- **Housing Median Age**: Age of the house.
- **Total Rooms & Bedrooms**: The number of rooms and bedrooms in each block.
- **Population**: Number of people living in that area.
- **Households**: Number of households in the block.
- **Median Income**: The income level of residents.
- **Median House Value**: The target variable representing house prices.

## 🔧 Installation & Setup
To run this project, follow these steps:

### 1️⃣ Clone the Repository:
```sh
git clone https://github.com/Mansi090/california_housing.git
cd california_housing
```

### 2️⃣ Install Required Dependencies:
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Analysis:
```sh
jupyter notebook
```
Open the Jupyter Notebook file and execute the cells step by step.

## 🔍 Exploratory Data Analysis (EDA)
The project performs extensive **EDA** to understand the dataset:
- Data visualization using **Matplotlib & Seaborn**
- Checking for missing values and handling them
- Feature correlation analysis
- Geospatial data visualization

## 🤖 Machine Learning Models
The project implements the following ML models for prediction:
1. **Linear Regression**
2. **Decision Tree Regressor**
3. **Random Forest Regressor**
4. **Gradient Boosting**

Each model is evaluated based on **Mean Absolute Error (MAE)** and **Root Mean Squared Error (RMSE)**.

## 📊 Results & Insights
- The **Random Forest model** performed the best in terms of accuracy.
- **Median Income** was found to be the most important feature influencing housing prices.
- The project provides interactive visualizations for better insights.

## 📌 Future Improvements
- Implement **Deep Learning models** for better performance.
- Try different feature engineering techniques.
- Deploy the model using Flask or FastAPI.

## 👥 Contributions
Contributions are welcome! If you’d like to contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Added new feature"`)
4. Push to your branch (`git push origin feature-branch`)
5. Create a Pull Request

## 📜 License
This project is licensed under the **MIT License**.

---
🙌 If you found this project helpful, don’t forget to **star the repository**! 🚀


