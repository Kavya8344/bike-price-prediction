# Bike Price Prediction Using Linear Regression

## Project Overview

This project predicts the selling price of used bikes using Machine Learning. The dataset contains information such as bike brand, age, power, kilometers driven, and ownership details. A Linear Regression model is trained to estimate the bike's price based on these features.

---

## Features Used

* Age of the bike
* Brand
* Engine Power
* Kilometers Driven
* Number of Owners

### Target Variable

* Price

---

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-Learn

---

## Project Workflow

### 1. Data Loading

The dataset is loaded using Pandas.

```python
df = pd.read_csv("clen_bike.csv")
```

### 2. Data Preprocessing

* Checked dataset information
* Removed duplicate records
* Dropped unnecessary columns
* Converted categorical brand names into numerical values using label mapping

### 3. Feature Selection

```python
X = total_df[['age', 'brand', 'power', 'kms_driven', 'owner']]
y = total_df['price']
```

### 4. Train-Test Split

```python
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

### 5. Model Training

```python
model = LinearRegression()
model.fit(x_train, y_train)
```

### 6. Prediction

```python
predictions = model.predict(x_test)
```

---

## Dataset

The dataset contains information about used motorcycles, including:

| Column     | Description               |
| ---------- | ------------------------- |
| age        | Age of the bike           |
| brand      | Manufacturer name         |
| power      | Engine power              |
| kms_driven | Distance traveled         |
| owner      | Number of previous owners |
| price      | Selling price             |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/bike-price-prediction.git
```

Install dependencies:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

Run the notebook:

```bash
jupyter notebook model_trainng.ipynb
```

---

## Results

The Linear Regression model learns the relationship between bike specifications and market price, allowing price estimation for unseen bikes.

---

## Future Improvements

* Feature Engineering
* Hyperparameter Tuning
* Random Forest Regressor
* XGBoost Regressor
* Model Evaluation Metrics Dashboard
* Deployment using Flask or Streamlit

---

## Author

Kavya Sharma

Machine Learning Project – Bike Price Prediction
