# Day 7: Pearson Correlation Coefficient

## Covariance

This is a measure of how two random variables change together, or the strength of their correlation.

Consider two random variables `X`and `Y`, each with `n` values (i.e. `x1, x2, ..., xn` and `y1, y2, ..., yn`). The covariance of `X` and `Y` can be found using either of the following equivalent formulas:

![Covariance formula][Covariance_formula]

`E(X)` and `E(Y)` are the means of `X` and `Y` respectively. This can also be expressed in the following terms (without referring the means):

![Covariance formula 2][Covariance_formula_2]

## Pearson Correlation Coefficient

In statistics, it measures the linear correlation between two variables `X` and `Y`. It has a value between `+1` and `-1`, where `1` is total positive correlation, `0` is no linear correlation and `-1` is total negative correlation.

The Pearson Correlation Coefficient, `r` is given by:

![Pearson Correlation][Pearson_correlation]

## Task

xx

# Day 7: Spearman's Rank Correlation Coefficient

We have two random variables, `X` and `Y`:
* `X = {x1, x2, ..., xn}`
* `Y = {y1, y2, ..., yn}`

If `RankX` and `RankY` denote the respective ranks of each data point, then the Spearman's rank correlation coefficient, `rs`, is the Pearson correlation coefficient of `RankX` and `RankY`.

The Spearman correlation coefficient is defined as the Pearson correlation coefficient between the rank variables.

For a sample of size `n`, the `n` raw scores `Xi`, `Yi` are converted to ranks `rg Xi`, `rg Yi`, and `rs`is computed as:

![Spearman Correlation Sample][spearman_sample]

where:
* `rho` denotes the usual Pearson correlation coefficient, but applied to the rank variables,
* `cov(rgX, rgY)` is the covariance of the rank variables,
* `sigma_rg_X` and `sigma_rg_Y` are the standard deviations of the rank variables.

Only if all `n` ranks are distinct integers, it can be computed using the popular formula:

![Spearman Correlation Distinct Integers][spearman_distinct_integers]

where
* `di = rg(Xi) - rg(Yi)` is the difference between the two ranks of each observation,
* `n` is the number of observations.

## Example

* `X = {0.2, 1.3, 0.2, 1.1, 1.4, 1.5}`
* `Y = {1.9, 2.2, 3.1, 1.2, 2.2, 2.2}`

`RankX`:
| | | | | | | |
| ---|-----|-----|-----|-----|-----|-----|
| `X`| 0.2 | 1.3 | 0.2 | 1.1 | 1.4 | 1.5 |
| `Rank` | 1 | 3 | 1 | 2 | 4 | 5 |

So, `RankX = {1, 3, 1, 2, 4, 5}`
Similarly, `RankY = {2, 3, 4, 1, 3, 3}`

`rs` equals the Pearson correlation coefficient of `RankX` and `RankY`, meaning that `rs = 0.158114`.

## Task II

Given two n-element data sets, `X` and `Y`, calculate the value of Spearman's rank correlation coefficient.

```python
10
10 9.8 8 7.8 7.7 1.7 6 5 1.4 2 
200 44 32 24 22 17 15 12 8 4
```

[Covariance_formula]: https://wikimedia.org/api/rest_v1/media/math/render/svg/6c66807f5054d1175f41b90485faadfb0aaf6104
[Covariance_formula_2]: https://wikimedia.org/api/rest_v1/media/math/render/svg/b4958d7088b98a90684bb7420eb8a722f37fc1a7
[Pearson_correlation]: https://wikimedia.org/api/rest_v1/media/math/render/svg/f76ccfa7c2ed7f5b085115086107bbe25d329cec
[spearman_sample]: https://wikimedia.org/api/rest_v1/media/math/render/svg/c06f5a0bc5c4b924334eeac566fe1a59f9578ff8
[spearman_distinct_integers]: https://wikimedia.org/api/rest_v1/media/math/render/svg/93e96a1c1568d0bb08de95c9976f040409e915a1