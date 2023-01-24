import gin
import random


# n_smaples can come from local/global scope or gin config file
@gin.configurable
def simulate(n_samples):
    return sum(random.random() for i in range(n_samples))


# n_samples must come from gin config file
@gin.configurable
def simulate_2(n_samples=gin.REQUIRED):
    return sum(random.random() for i in range(n_samples))


# helper functions, these can alse be configed
@gin.configurable
def random_uniform(minval=0, maxval=1):
    return random.uniform(minval, maxval)


@gin.configurable
def random_triangle(minval=0, maxval=1):
    middle = (maxval - minval) / 2
    return random.triangular(minval, maxval, middle)


@gin.configurable
def simulate_3(random_func, n_samples):
    return sum(random_func() for i in range(n_samples))


# external config
gin.external_configurable(random.uniform)
gin.external_configurable(random.triangular)

if __name__ == "__main__":
    gin.parse_config_file("config.gin")
    print(simulate(10))
    print(simulate_2())
    print(simulate_3(random_uniform))
    print(simulate_3())
