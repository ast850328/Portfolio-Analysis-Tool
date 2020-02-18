import numpy as np
import pandas as pd
import math, random
from scipy.optimize import minimize


class Optimal_F:

    def __init__(self):
        pass

    # Excpected Returns
    def calc_exp_returns(self, avg_returns, weights):
        exp_returns = avg_returns.dot(weights.T)
        return exp_returns

    # Variance-covariance matrix
    def TWR(self, df, weights):
        stocks = df.columns.to_list()
        WCS = abs(df.min())
        TWRs = 0
        i = 0
        for stock in stocks:
            HPRs = (1 - weights[i] * (df[stock] / df[stock]))
            TWRs += np.prod(HPRs)
            i += 1
        return -TWRs

    def optimize(self, df):
        returns  = df.mean()
        target_return = sum(returns) / len(df.columns)

        # Initialize random weights
        np.random.seed(34522)
        weights =  np.random.dirichlet(np.ones(len(df.columns)),size=1) # makes sure that weights sums upto 1.
        bounds = ((0.0, 1.),) * len(df.columns)  # Bounds of the problem
        res = minimize(
            # Objective function defined here
            lambda x: self.TWR(df, x),
            weights, method='SLSQP'
            , bounds=bounds, options={'disp': False, 'ftol': 1e-04, 'maxiter': 1000}
            , constraints=[{'type': 'eq', 'fun': lambda x: sum(x) - 1.0},
                           {'type': 'eq', 'fun': lambda x: self.calc_exp_returns(returns, x) - target_return}])
        return res

    def get_weight(self, df):
        df = df.pct_change()
        df = df.dropna()
        stocks = df.columns.to_list()

        res = self.optimize(df)
        if res.success == True:
            weights = res.x
            weight_dict = {}
            for weight, stock in zip(weights, stocks):
                weight_dict[stock] = weight
            return weight_dict
        else:
            print("optimize is not successful.")
            return None
