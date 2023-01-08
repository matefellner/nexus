# Advanced scikit learn 

From https://calmcode.io/

Requires scikit-lego: python -m pip install scikit-lego

## Introduction

- sklearn.pipeline to use preprocessing (scaler) and model as a single unit
- this can be used inside a gridsearch as well

## Dummy

- be careful about benchmarking, sklearn.dummy has classifier to measure models with uniform, most frewuent or stratified predictions
- for imbalanced dataset, the score of these can be higher than a "normal model"
- also available for dummy regressor

## Preprocessing

- applying sklearn's quantileTransformer to preprocess data which has outliers
- applying sklearn.preprocessing's polynomialFeatures to get polynoms of the input vectors, see in https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html
- using sklearn.preprocessing's OneHotEncoder to encode text values to vectors

## Metrics

- creating custom scoring function to use in grid search optimization, e.g. minimum of precision and recall
- example of using it on imbalanced data, for outlier detection with isolation forest

## Meta-estimators

- creating ensemble method from differenct modeld with sklearn.ensemble's VotingClassifier, seting different weights for them
- changing model predictions by adjusting probability threshold (using sci-kit lego)
- creating different models for different groups of data with sci-kit lego's GroupedPredictor
- using sklearn.multioutput's methods to create models and fit models with multiple outputs


## Human learn

> python -m pip install human-learn

See documantetion at: https://koaning.github.io/human-learn/index.html

Interactive selection for classification, can be used in model creation
