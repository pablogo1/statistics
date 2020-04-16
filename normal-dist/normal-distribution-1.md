# Day 5 - Normal Distribution I

## Normal Distribution

The probability density function of normal distribution is:

![Normal PDF][normal-pdf]

Where ![miu][miu-sign] denotes the mean, ![sigma squared][sigma-squared] is the variance and ![sigma][sigma-sign] is the standard deviation.

## Standard Normal Distribution

If the mean is 0 and the standard deviation is 1, then the normal distribution is known as Standard Normal Distribution:

![Standard Normal PDF][standard-normal-pdf]

Every normal distribution can be represented as standard normal distribution:

[!Can be represented as standard normal distribution][general-distribution]

## Cumulative Probability

Consider a real-valued random variable, X. The cumulative distribution function (CDF) of X (or just a distribution function of X) evaluated at x is the probability that X will take a value less than or equal to x: F(x) = P(X <= x).

Also,
P(a <= X <= b) = P(a < X < b) = Fx(b) - Fx(a)

The cumulative distribution function for a function iwth normal distribution is:



[normal-pdf]: https://wikimedia.org/api/rest_v1/media/math/render/svg/00cb9b2c9b866378626bcfa45c86a6de2f2b2e40
[standard-normal-pdf]: https://wikimedia.org/api/rest_v1/media/math/render/svg/3123d8dd4c3386afe9fac119fed2cfaf7ce9f336
[sigma-sign]: https://wikimedia.org/api/rest_v1/media/math/render/svg/59f59b7c3e6fdb1d0365a494b81fb9a696138c36
[sigma-squared]: https://wikimedia.org/api/rest_v1/media/math/render/svg/53a5c55e536acf250c1d3e0f754be5692b843ef5
[miu-sign]: https://wikimedia.org/api/rest_v1/media/math/render/svg/9fd47b2a39f7a7856952afec1f1db72c67af6161
[general-distribution]: https://wikimedia.org/api/rest_v1/media/math/render/svg/29ad1537690c6dca78c0a0834983bcd08c085aaf