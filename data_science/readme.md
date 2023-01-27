# Contents:

## Annoy

Fast nearest neighbor calculation

Tutorial from calmcode.io
https://github.com/spotify/annoy


## Bad labels, cleanlab

Finding bad labels in dataset

- cleanlab.pruning.get_noise_indices: return rows that worth double-checking
- LearningWithNoisyLabels: more robust on data with bad labels

Tutorial from calmcode.io
https://github.com/cgnorthcutt/cleanlab


## Dirty cat

Dealing with categorical data

String similarity enconding with ngrams

https://dirty-cat.github.io/stable/index.html


## Human learn

Human-Learn contains scikit-learn compatible tools that should make it easier to construct and benchmark rule based systems that are designed by humans.
You can also use it in combination with ML models.

> python -m pip install human-learn

See documantetion at: https://koaning.github.io/human-learn/index.html

## Lin prog

cvxpy library for linear and convex optimization problems.

variable creation: cp.Variable(price.shape[0])

objective function with vector operations: cp.Minimize(cp.sum(c@x))

constraint creation: [x >= 0]

also: constraints.append(x@df[key] >= value)

Problem solving: 

prob = cp.Problem(objective, constraints)

prob.solve()

Tutorial from calmcode.io
https://www.cvxpy.org/


## Memo

Saving experiment data.

@memlist: function decorator to save output (as a dict) to create list of dicts where the keys are the function arguments

@memfile: save this list of dicts to file

grid and runner: parametertest running in parallel

Tutorial from calmcode.io

https://calmcode.io/memo/memlist.html


## Model-mining

Creating hand-engineered classifiers with the hulearn package's FunctionClassifier class. This can be used in sklearn grid search

Tutorial from calmcode.io

https://calmcode.io/model-mining/introduction.html


## Pandas pipe

Clean pandas code with decorators and pandas pipe

log_step: function decorator to save name, shape and execution time

df.pipe() apply previously defined function to dataframe

https://calmcode.io/pandas-pipe/introduction.html


## Partial fit

What if the dataset is too large for the memory?

In sklearn training in batch is available: model.partial_fit(X, Y)

This can be also used for augmentations

Tutorial from calmcode.io

https://calmcode.io/partial_fit/introduction.html

https://scikit-learn.org/0.15/modules/scaling_strategies.html


## Patsy

Preprocessing with R based tools

One-hot encoded arrays:

y, X = ps.dmatrices("col_y ~ col_x_1 + col_x_2 + C(col_x_3)", df)

where col_x_3 was numeric but changed to categorical

Using python or custom functions:

y, X = ps.dmatrices("col_y ~ date_to_num(col_x_1) * np.log(col_x_2)", df)

Using spline for feature generation:

y, X = ps.dmatrices("col_y ~ cc(col_x, df=12)", df)

ALso integration in scikit lego for more complex pipelines.

Tutorial from calmcode.io

https://calmcode.io/partial_fit/introduction.html

https://patsy.readthedocs.io/en/latest/overview.html


## Pigeon

Data annotation tool in jupyter

annotate(data, options_list, display_function)

Tutorial from calmcode.io

https://github.com/agermanidis/pigeon

## PythonExcel

Using openpyxl library to process xlsx files and convert them into dataframes

## Tesseract

Extracting text from images

Tutorial from calmcode.io