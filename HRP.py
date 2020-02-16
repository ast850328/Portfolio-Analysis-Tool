import math
# import matplotlib.pyplot as mpl
import scipy.cluster.hierarchy as sch, random, numpy as np, pandas as pd

class HRP:

    def __init__(self, config):
        self.cluster_method = config['cluster_method']
        self.order_method = config['order_method']
        self.weight_method = config['weight_method']
        self.weight_dict = {}

    def correl_dist(self, corr):
        # A distance matrix based on correlation, where 0<=d[i,j]<=1
        # This is a proper distance metric
        dist=((1-corr)/2.) ** .5 # distance matrix
        return dist

    def get_IVP(self, cov,**kargs):
        # Compute the inverse-variance portfolio
        ivp = 1. / np.diag(cov)
        ivp /= ivp.sum()
        return ivp

    def get_cluster_var(self, cov, cItems):
        # Compute variance per cluster
        cov_ = cov.loc[cItems,cItems] # matrix slice
        w_ = self.get_IVP(cov_).reshape(-1, 1)
        cVar = np.dot(np.dot(w_.T, cov_), w_)[0, 0]
        return cVar

    def get_quasi_diag(self, link):
        # Sort clustered items by distance
        link = link.astype(int)
        sortIx = pd.Series([link[-1, 0], link[-1, 1]])
        numItems = link[-1, 3] # number of original items
        while sortIx.max() >= numItems:
            sortIx.index = range(0, sortIx.shape[0]*2, 2) # make space
            df0 = sortIx[sortIx>=numItems] # find clusters
            i = df0.index
            j = df0.values - numItems
            sortIx[i] = link[j, 0] # item 1
            df0 = pd.Series(link[j, 1], index=i+1)
            sortIx = sortIx.append(df0) # item 2
            sortIx = sortIx.sort_index() # re-sort
            sortIx.index = range(sortIx.shape[0]) # re-index
        return sortIx.tolist()

    def plot_corr_matrix(self, path, corr, labels=None): # Heatmap of the correlation matrix
    #     if labels is None:
        labels = []
        mpl.pcolor(corr)
        mpl.colorbar()
        mpl.yticks(np.arange(.5, corr.shape[0]+.5), labels)
        mpl.xticks(np.arange(.5, corr.shape[0]+.5), labels)
        mpl.show()
        mpl.clf()
        mpl.close() # reset pylab
        return

    def plot_linkage(self, link):
        mpl.figure(figsize=(25, 10))
        sch.dendrogram(link)
        mpl.show()
        mpl.clf();
        mpl.close();

    def top_down(self, tree, weight, cov):
        if (tree.is_leaf()):
            treeId = tree.get_id()
            self.weight_dict[cov.index[treeId]] = weight
            return

        leftTree = tree.get_left()
        rightTree = tree.get_right()

        if self.weight_method == 'equal':
            alpha = 1 - 0.5
        elif self.weight_method == 'var':
            leftList = leftTree.pre_order(lambda x:x.id)
            leftList = cov.index[leftList].tolist()
            leftVar = self.get_cluster_var(cov, leftList)

            rightList = rightTree.pre_order(lambda x:x.id)
            rightList = cov.index[rightList].tolist()
            rightVar = self.get_cluster_var(cov, rightList)

            alpha = 1 - leftVar/(leftVar+rightVar)

        self.top_down(leftTree, weight*alpha, cov)
        self.top_down(rightTree, weight*(1-alpha), cov)

    def bisection(self, leaves_list, cov):

        sortIx = cov.index[leaves_list].to_list()
        # Compute HRP alloc
        w = pd.Series(1,index=sortIx)
        cItems = [sortIx] # initialize all items in one cluster
        while len(cItems) > 0:
            cItems = [i[j:k] for i in cItems for j, k in ((0, len(i)/2),
                                                       (len(i)/2, len(i))) if len(i)>1] # bi-section
            for i in xrange(0, len(cItems), 2): # parse in pairs
                cItems0 = cItems[i] # cluster 1
                cItems1 = cItems[i+1] # cluster 2
                if self.weight_method == 'equal':
                    alpha = 1 - 0.5
                elif self.weight_method == 'var':
                    cVar0 = self.get_cluster_var(cov, cItems0)
                    cVar1 = self.get_cluster_var(cov, cItems1)
                    alpha = 1 - cVar0 / (cVar0 + cVar1)
                w[cItems0] *= alpha # weight 1
                w[cItems1] *= 1 - alpha # weight 2
        for key in w.keys():
            self.weight_dict[key] = w[key]

    def alloc_weight(self, link, cov):

        tree = sch.to_tree(link)
        leaves_list = sch.leaves_list(link)
        order_method = self.order_method

        if order_method == 'top-down':
            self.top_down(tree, 1.0, cov)
        elif order_method == 'bisection':
            self.bisection(leaves_list, cov)
        return

    def get_weight(self, df):
        df = df.pct_change()
        df = df.dropna()
        x = df
        cov, corr = x.cov(), x.corr()

        # cluster
        dist = self.correl_dist(corr)
        link = sch.linkage(dist, self.cluster_method)

        # weighting
        self.alloc_weight(link, cov)
        return self.weight_dict
