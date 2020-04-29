# The Central Limit Theorem I

The central limit theorem (CLT) states that, for a large enough sample (n), the distribution of the sample mean will approach normal distribution. This holds for a sample of independent random variables from any distribution with a finite standard deviation.

Let `{X1, X2, ..., Xn}` be a random data set of size `n`, that is, a sequence of independent and identically distributed variables drawn from distributions of expected values given by the mean [miu] and finite variances given by [sigma_squared]. The sample average is:

![CLT formula][CLT_formulae]

For large `n`, the distribution of sample sums `Sn` is close to normal distribution `N(u', sigma')` where:

* `u' = n x u`
* `sigma' = sqrt(n) x sigma`

## Task I

A large elevator can transport a maximum of `9800` pounds. Suppose a load of cargo containing `49` boxes must be transported via the elevator. The box weight of this type of cargo follows a distribution with a mean of `u = 205` pounds and a standard deviation of `sigma = 15` pounds. Based on this information, what is the probability that all `49` boxes can be safely loaded into the freight elevator and transported?

### Input format

```python
9800 # maximum weight the elevator can transport
49   # contains the number of boxes in the cargo
205  # mean weight of a cargo box
15   # standard deviation
```

## Task II

A number of tickets purchased by each student for the University X vs. University Y football game follows a distribution that has a mean of `mu = 2.4` and a standard deviation `sigma = 2.0`.

A few hours before the game starts, `100` eager students line up to purchase last-minute tickets. If there are only `250` tickets left, what is the probability that all `100` students will be able to purchase tickets?

*Input Format:*

```python
250 # Number of last-minute tickets available at box office
100 # Number of students waiting to buy tickets
2.4 # Mean of the purchased tickets
2.0 # Std Dev of the purchased tickets
```

## Task III

You have a sample of `100` values from a population with mean `mu = 500` and with standard deviation `sigma = 80`. Compute the interval that covers the middle `95%` of the distribution in the sample mean. In other words, compute A and B such that `P(A < x < B) = 0.95`. Use the value of `z = 1.96`. Note that `z` is the [z-score](https://en.wikipedia.org/wiki/Standard_score).

*Input format:*

```python
100 # Sample size
500 # Mean
80  # Std Dev
0.95 # Interval probability
1.96 # Z-Score
```

[CLT_formulae]: https://wikimedia.org/api/rest_v1/media/math/render/svg/fda934052c42d3797714ecd1eaa90910e9f6e050