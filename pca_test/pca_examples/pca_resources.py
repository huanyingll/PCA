#PCA主成分分析源代码
import numpy as np
class PCA:
    def __init__(self, n_components):
        # 主成分的个数n
        self.n_components = n_components
        # 具体主成分
        self.components_ = None
    def fit(self, X, eta=0.001, n_iters=1e4):
        '''均值归零'''
        def demean(X):
            return X - np.mean(X, axis=0)
        '''方差函数'''
        def f(w, X):
            return np.sum(X.dot(w) ** 2) / len(X)
        '''方差函数导数'''
        def df(w, X):
            return X.T.dot(X.dot(w)) * 2 / len(X)
        '''将向量化简为单位向量'''
        def direction(w):
            return w / np.linalg.norm(w)
        '''寻找第一主成分'''
        def first_component(X, initial_w, eta, n_iters, epsilon=1e-8):
            w = direction(initial_w)
            cur_iter = 0
            while cur_iter < n_iters:
                gradient = df(w, X)
                last_w = w
                w = w + eta * gradient
                w = direction(w)
                if (abs(f(w, X) - f(last_w, X)) < epsilon):
                    break
                cur_iter += 1
            return w
        # 过程如下：
        # 归0操作
        X_pca = demean(X)
        #print('均值归0结果：')
        #print(X_pca)
        # 初始化空矩阵，行为n个主成分，列为样本列数
        self.components_ = np.empty(shape=(self.n_components, X.shape[1]))
        # 循环执行每一个主成分
        for i in range(self.n_components):
            # 每一次初始化一个方向向量w
            initial_w = np.random.random(X_pca.shape[1])
            # 使用梯度上升法，得到此时的X_PCA所对应的第一主成分w
            w = first_component(X_pca, initial_w, eta, n_iters)
            # 存储起来
            self.components_[i:] = w
            # X_pca减去样本在w上的所有分量，形成一个新的X_pca，以便进行下一次循环
            X_pca = X_pca - X_pca.dot(w).reshape(-1, 1) * w
        return self

    # 将X数据集映射到各个主成分分量中
    def transform(self, X):
        print('协方差矩阵:')
        print(self.components_)
        assert X.shape[1] == self.components_.shape[1]
        return X.dot(self.components_.T)
    def inverse_transform(self, X):
        return X.dot(self.components_)







