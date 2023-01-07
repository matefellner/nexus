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