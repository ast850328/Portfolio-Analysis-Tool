import numpy as np
import pandas as pd
import math, random
from scipy.optimize import minimize
from sklearn.preprocessing import MinMaxScaler

class OptimalF:

    def __init__(self, config):
        self.model_name = 'OptimalF'
        self.config = config

    # Excpected Returns
    def calc_exp_returns(self, avg_returns, weights):
        exp_returns = avg_returns.dot(weights.T)
        return exp_returns

    def TWR(self, df, weights):
        names = df.columns.to_list()
        WCS = df.min()
        # print(WCS)
        TWRs = 1
        i = 0
        for name in names:
            if WCS[name] >= 0:
                i += 1
                continue
            HPRs = 1 + (weights[i] * (- df[name] / WCS[name]))
            TWRs = TWRs + np.prod(HPRs)
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
            , bounds=bounds, options={'disp': False, 'ftol': 1e-04, 'maxiter': 10000}
            , constraints=[{'type': 'eq', 'fun': lambda x: sum(x) - 1.0},
                           {'type': 'eq', 'fun': lambda x: self.calc_exp_returns(returns, x) - target_return}])
        return res

    def get_weight(self, df):
        names = df.columns.to_list()
        scaler = MinMaxScaler()
        df[names] = scaler.fit_transform(df)

        res = self.optimize(df)
        if res.success == True:
            weights = res.x
            weight_dict = {}
            for weight, name in zip(weights, names):
                weight_dict[name] = weight
            return weight_dict
        else:
            print("optimize is not successful.")
            weight = 1.0 / len(names)
            weight_dict = {}
            for name in names:
                weight_dict[name] = weight
            return weight_dict
