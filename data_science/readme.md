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


## Memo

Saving experiment data.
@memlist: function decorator to save output (as a dict) to create list of dicts where the keys are the function arguments
@memfile: save this list of dicts to file
grid and runner: parametertest running in parallel

Tutorial from calmcode.io
https://calmcode.io/memo/memlist.html



## Pandas pipe

Clean pandas code with decorators and pandas pipe

log_step: function decorator to save name, shape and execution time
df.pipe() apply previously defined function to dataframe

https://calmcode.io/pandas-pipe/introduction.html

# Lin prog

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