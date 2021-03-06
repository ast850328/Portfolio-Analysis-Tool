import pandas as pd

class EqualWeight:

    def __init__(self, config):
        self.model_name = 'EqualWeight'
        self.config = config

    def get_weight(self, df):
        names = df.columns.to_list()
        weight = 1.0 / len(names)
        weight_dict = {}
        for name in names:
            weight_dict[name] = weight
        return weight_dict
