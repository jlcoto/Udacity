#!/usr/bin/python

import sys
import pickle
import pprint
import numpy as np
sys.path.append("tools/")
from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data, test_classifier

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi',
'deferred_income', 
'long_term_incentive', 
'total_payments',
'total_stock_value', 
'total_pay_comp', 
'total_stock_comp',
'sal_to_bonus']# You will need to use more features

### Load the dictionary containing the dataset
with open('final_data_zeros_proj.pickle', "r") as data_file:
    data_dict = pickle.load(data_file)

#


### Task 2: Remove outliers
### Task 3: Create new feature(s)
### Store to my_dataset for easy export below.
my_dataset = data_dict


#
#### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

#### Task 4: Try a varity of classifiers
#### Please name your classifier clf for easy export below.
#### Note that if you want to do PCA or other multi-stage operations,
#### you'll need to use Pipelines. For more info:
#### http://scikit-learn.org/stable/modules/pipeline.html
#
## Provided to give you a starting point. Try a variety of classifiers.
#

from sklearn.preprocessing import MinMaxScaler
from sklearn.naive_bayes import GaussianNB
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.svm import SVC

features_train_zero, features_test_zero, labels_train_zero, labels_test_zero = train_test_split(features, labels, test_size=0.3, random_state=42)




clf = GaussianNB()
clf.fit(features_train_zero, labels_train_zero)
print test_classifier(clf, my_dataset, features_list, folds = 1000)

#
#### Task 5: Tune your classifier to achieve better than .3 precision and recall 
#### using our testing script. Check the tester.py script in the final project
#### folder for details on the evaluation method, especially the test_classifier
#### function. Because of the small size of the dataset, the script uses
#### stratified shuffle split cross validation. For more info: 
#### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html
#
## Example starting point. Try investigating other evaluation techniques!
#from sklearn.cross_validation import train_test_split
#features_train, features_test, labels_train, labels_test = \
#    train_test_split(features, labels, test_size=0.3, random_state=42)
#
#### Task 6: Dump your classifier, dataset, and features_list so anyone can
#### check your results. You do not need to change anything below, but make sure
#### that the version of poi_id.py that you submit can be run on its own and
#### generates the necessary .pkl files for validating your results.
#
dump_classifier_and_data(clf, my_dataset, features_list)#