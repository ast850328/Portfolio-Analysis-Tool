import numpy as np
import pandas as pd
import math, random
from scipy.optimize import minimize

class CLA:

    def __init__(self, config):
        self.config = config

    # Excpected Returns
    def calc_exp_returns(self, avg_returns, weights):
        exp_returns = avg_returns.dot(weights.T)
        return exp_returns

    # Variance-covariance matrix
    def var_cov_matrix(self, df, weights):
        sigma = np.cov(np.array(df).T, ddof=0)  # Covariance
        var = (np.array(weights) * sigma * np.array(weights).T).sum()
        return var

    def optimize(self, df):
        returns  = df.mean()
        target_return = sum(returns) / len(df.columns)

        # Initialize random weights
        np.random.seed(34522)
        weights =  np.random.dirichlet(np.ones(len(df.columns)),size=1) # makes sure that weights sums upto 1.
        bounds = ((0.0, 1.),) * len(df.columns)  # Bounds of the problem
        res = minimize(
            # Objective function defined here
            lambda x: self.var_cov_matrix(df, x),
            weights, method='SLSQP'
            # Jacobian using automatic differentiation
            #, jac=ad.gh(lambda x: var_cov_matrix(df, x))[0]
            # bounds given above
            , bounds=bounds, options={'disp': False, 'ftol': 1e-04, 'maxiter': 1000}
            , constraints=[{'type': 'eq', 'fun': lambda x: sum(x) - 1.0},
                           {'type': 'eq', 'fun': lambda x: self.calc_exp_returns(returns, x) - target_return}])
        return res

    def get_weight(self, df):
        names = df.columns.to_list()

        res = self.optimize(df)
        if res.success == True:
            weights = res.x
            weight_dict = {}
            for weight, name in zip(weights, names):
                weight_dict[name] = weight
            return weight_dict
        else:
            print("optimize is not successful.")
            return None
