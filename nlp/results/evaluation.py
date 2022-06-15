import pickle
import os
import sys
import pandas as pd
sys.path.append('F:\\hku\\capstone\\pythonProject\\nlp')
from sklearn import metrics
from sklearn.metrics import roc_auc_score


from constants import *
from sklearn.metrics import accuracy_score

from sklearn.metrics import  accuracy_score

df  = pd.read_csv("elasticnet//results.csv")

labels = df[["labels"]]
probs = df[["probs"]]

predict = probs.where(probs>=0.5,0).where(probs<0.5,1)

print("accuracy: {}".format(accuracy_score(labels,predict)))
print("auc score: {}".format(roc_auc_score(labels,probs)))