import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def predict_fansign_cut():
    data = pd.read_csv('llm_crawl_dataset.csv')
    X = data[['First-Week Sales (X)']]
    y = data[['Est. Fansign Cut (Y)']]

    # log
    log_X = np.log(X) # log(x)
    log_model = LinearRegression()
    log_model.fit(log_X, y)

    # linear
    linear_model = LinearRegression()
    linear_model.fit(X, y)
 
    # exp
    log_y = np.log(y) # log(y) -> meaning exp(x) = y
    exp_model = LinearRegression()
    exp_model.fit(X, log_y)
    exp_a = exp_model.coef_[0][0]
    exp_b = np.exp(exp_model.intercept_[0]) # inter

    

    first_week_sales = float(input("Enter the first-week sales number (numeber only): "))
    predicted_cut_log = log_model.predict(np.log(np.array([[first_week_sales]])))
    print(f"log (Most Accurate one): {predicted_cut_log[0][0]} albums")

    predicted_cut_linear = linear_model.predict(np.array([[first_week_sales]]))
    print(f"linear: {predicted_cut_linear[0][0]} albums")

    predicted_cut_exp = exp_b * np.exp(exp_a * first_week_sales)
    print(f"exp: {predicted_cut_exp} albums")

if __name__ == "__main__":
    predict_fansign_cut() 
