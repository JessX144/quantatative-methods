############## Modern Portfolio Theory - Markowitz Model
# mean, variance and covariance https://www.alchemer.com/resources/blog/variance-covariance-correlation/
# variance = std ∂^2
# correlation standardises units unlike covariance https://www.cuemath.com/correlation-coefficient-formula/

# Markowitz Model introduces diversification to reduce risk
# For a given level of risk, we can construct portfolio for maximum profit
#   Assumptions
#       Returns are normally distributed with mean µ and variance ∂
#       Investors are risk averse (take on more risk if expecting more return)
#       Only deals with long positions, not short (only buy, don't sell stocks)
# For stock i, wi = weight, ri = return, µi = expected/mean return based on historical data
# Expected/mean value E[X] = ∑ p(x) * x where p(x): probability/weight. ∑ p(x) = 1, hence why don't need division by N

# Daily return of a stock = S(t + 1) - S(t) / S(t)
# Log daily return of a stock = ln S(t + 1) / S(t) for normalization
# portfolio µ = w^T * µ

# Risk of portfolio can be calculated with variance/std dev
# Define covariance matrix between portfolios I and J
#   ∂ij = E[(ri - µi)(rj - µj)]
# If ∂ij > 0 stocks are proportional, ∂ij < 0 inversely proportional
# High covariance ∂ij doesn't provide diversification

# Variance is covariance with itself, relationship between stocks within portfolio
#  Expected portfolio variance ∂i^2 = E[(ri - µi)^2]
#                                   = ∑i ∑j wi wj ∂ij (row by column)      ∂ij = ∂ji symmetric matrix
#                                   = w^T ∑ w  ∑: covariance matrix

# Plotting expected return vs expected volatility for different sets of weights = produces graph
# Graph horizon gives efficient frontier - maximum return given fixed risk/minimum risk given fixed return
# https://images.app.goo.gl/5oee2ny1K4w7By269

# Sharpe ratio = measures how much excess return you receive for excess volatility
# S(x) = rx - Rf / ∂x
#      rx: expected return of stock x
#      Rf: return of a risk free stock f e.g bond, interest rate (lending to bank)
#      ∂x: std of stock x
# Higher Sharpe ratio is better investment

# Capital Market Line connects risk free asset (e.g gov bond) to efficient frontier, intersects at max Sharpe Ratio point https://images.app.goo.gl/DnGhap7zC5GJxjf26
# Moving along the line provides most efficient portfolio mix of risk-free assets and stocks

import numpy as np
import pandas
import yfinance as yf
import matplotlib.pyplot as plt
import scipy.optimize as optimization

# stocks
stocks = ['AAPL', 'WMT', 'TSLA', 'GE', 'AMZN', 'DB']
start_date = '2020-01-01'
end_date = '2023-12-01'


def download_data():
    stock_data = {}
    for stock in stocks:
        # ticker is unique ID for listing security on stock exchange
        ticker = yf.Ticker(stock)
        # take closing prices for stock
        stock_data[stock] = ticker.history(start=start_date, end=end_date)['Close']

    return pandas.DataFrame(stock_data)

def show_data(data):
    data.plot()
    plt.show()

if __name__ == '__main__':
    show_data(download_data())

