import nltk
from nltk.tokenize import sent_tokenize, word_tokenize


# #nltk.download()
# word_token = "hello, there!. What going on there, send me resolution"
#
# print(word_tokenize(word_token))
#
# for i in word_tokenize(word_token):
#     print(i)

import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)

print(clf.predict([[-0.8, -1]]))

clf_pf = GaussianNB()
clf_pf.partial_fit(X, Y, np.unique(Y))

print(clf_pf.predict([[-0.8, -1]]))

##################################

from sklearn.gaussian_process.kernels import ConstantKernel, RBF
kernel = ConstantKernel(constant_value=1.0, constant_value_bounds=(0.0, 10.0)) * RBF(length_scale=0.5, length_scale_bounds=(0.0, 10.0)) + RBF(length_scale=2.0, length_scale_bounds=(0.0, 10.0))
for hyperparameter in kernel.hyperparameters: print(hyperparameter)
params = kernel.get_params()
for key in sorted(params): print("%s : %s" % (key, params[key]))
print(kernel.theta)  # Note: log-transformed
print(kernel.bounds)  # Note: log-transformed

