
# coding: utf-8

# In[6]:

import os
import numpy as np 
import re
import io
from utilities.features_csv import to_csv
import pandas as pd
from IPython.display import display


# # Preprocessing

# In[7]:

import re 
import csv 
docs = {}
labels = {}
#I only work if you run me in the same folder as the actual text files 

with open('training_labels.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            id = int(row[1])
            score= float(row[2])
            labels[id]=score
            line_count += 1
i = 0
for root, dirs, files in os.walk("corpus/"):
    for file in files:
        if file.endswith(".txt"):
            id = re.sub("[^0-9]", "", file)
            id = int(id) 
            path_file = os.path.join(root,file)
            curdir = path_file
            file = open(curdir, 'r', errors='ignore')
            i+=1
            text = file.read()
            docs[id] = text

        


# In[8]:

to_csv(docs, labels, "sike")


# In[9]:

data = pd.read_csv("final.csv")
display(data.head(n=10))


# In[10]:

#Split the data into labels and features
scores = data['Score']

features_raw = data.drop(['Score', 'iD', 'vendors'] , axis = 1)
# features_raw = data.drop("vendors", axis =1)


# In[11]:

from sklearn.preprocessing import MinMaxScaler
# Initialize a scaler, then apply it to the features
scaler = MinMaxScaler()
numerical = ['fog_index', 'avg_sentence_length', 'flesch_reading_ease', 'dale_chall_readability_score']
features_log_minmax_transform = pd.DataFrame(data = features_raw)
features_log_minmax_transform[numerical] = scaler.fit_transform(features_raw[numerical])


# Show an example of a record with scaling applied
display(features_log_minmax_transform.head(n = 5))


# In[12]:

# Import train_test_split
from sklearn.model_selection import train_test_split
# Split the 'features' and 'income' data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features_log_minmax_transform, 
                                                    scores, 
                                                    test_size = 0.2, 
                                                    random_state = 0)
# Show the results of the split
print("Training set has {} samples.".format(X_train.shape[0]))
print("Testing set has {} samples.".format(X_test.shape[0]))


# # Random Forrest

# In[13]:

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

forest = RandomForestClassifier(n_estimators=50, max_depth=None,random_state=1, criterion="entropy")

forest.fit(X_train, y_train)

forrest_predict = forest.predict(X_test)
f1_score(y_test, forrest_predict, average='macro')


# In[15]:

from sklearn.metrics import classification_report
target_names = ['1', '2', '3', '4', '5']
print(classification_report(y_test, forrest_predict, target_names=target_names))


# # Extra Decision Trees

# In[17]:

from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import ExtraTreesClassifier


extra = ExtraTreesClassifier(n_estimators = 5, random_state = 14, criterion='entropy')
extra.fit(X_train, y_train)

predictions_extra = extra.predict(X_test)
f1_score(y_test, predictions_extra, average='micro')


# In[22]:

print(classification_report(y_test, predictions_extra, target_names=target_names))


# # AdaBoost

# In[16]:

from sklearn.ensemble import AdaBoostClassifier
tree = DecisionTreeClassifier(max_depth=10, criterion='gini', min_samples_split=5)
ada = AdaBoostClassifier(base_estimator=extra, 
                         n_estimators=50, learning_rate=.2,
                         algorithm='SAMME.R', random_state=4)
ada.fit(X_train, y_train)
predictions_ada = ada.predict(X_test)
f1_score(y_test, predictions_ada, average='micro')


# In[12]:

print(classification_report(y_test, predictions_ada, target_names=target_names))


# In[12]:

from sklearn import model_selection
X = features_log_minmax_transform
y = scores
num_folds = 5
num_instances = len(X)
loocv = model_selection.LeaveOneOut()
model = ExtraTreesClassifier(n_estimators=200, max_depth=11,random_state=None, 
                             criterion="gini", min_samples_split=5)
results = model_selection.cross_val_score(model, X, y, cv=loocv)
print("Accuracy: %.3f%% (%.3f%%)" % (results.mean()*100.0, results.std()*100.0))


# In[ ]:



