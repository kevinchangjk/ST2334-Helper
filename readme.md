# SciPy Helper

_Written and developed by [Prittam Ravi](https://github.com/prit3010 "Prittam Ravi") and [Kevin Chang](https://github.com/kevinchangjk "Kevin Chang Jon Kit")_

This is a python package building on top of SciPy's functions, designed and built for the purpose of simplifying computations for a specific module at the **National University of Singapore**, [ST2334](https://nusmods.com/modules/ST2334/probability-and-statistics "Probability and Statistics").

It may not be very useful for other applications.

## Usage

There are three main functionalities provided.

1. General Usage: convenient functions, but very limited
2. Confidence Intervals: construct confidence intervals for samples
3. Hypotheses Testing: conduct hypothesis test given data

The detailed specifications and instructions are provided below.

### Navigation

1. [General Usage](#general-usage)

    - [Displaying answers](#displaying-answers)
    - [Discrete pdf](#discrete-pdf)
    - [Z-distribution](#z-distribution)
    - [Paired Data](#paired-data)
    - [Pooled Sample Variance](#pooled-sample-variance)
    - [Sum of Squares](#sum-of-squares)

2. [Confidence Intervals](#confidence-intervals)

    - [Interval Bounds](#interval-bounds)
    - [CI for Mean](#ci-for-mean)
        - [CI: Mean with Known Variance](#ci-mean-with-known-variance)
        - [CI: Mean with Unknown Variance](#ci-mean-with-unknown-variance)
        - [CI: Difference in Mean with Known Variance](#ci-difference-in-mean-with-known-variance)
        - [CI: Difference in Mean with Unknown Variance](#ci-difference-in-mean-with-unknown-variance)
        - [CI: Difference in Mean with Unknown but Equal Variance](#ci-difference-in-mean-with-unknown-but-equal-variance)
        - [CI: Difference in Mean of Paired Data](#ci-difference-in-mean-of-paired-data)
    - [CI for Variance](#ci-for-variance)
        - [CI: Variance with Known Mean](#ci-variance-with-known-mean)
        - [CI: Variance with Unknown Mean](#ci-variance-with-unknown-mean)
        - [CI: Ratio of Variance](#ci-ratio-of-variance)

3. [Hypotheses Testing](#hypotheses-testing)

    - [p-value](#p-value)
    - [Concluding the Test](#concluding-the-test)
    - [Transformers](#transformers)
        - [Binomial to Normal Transformer](#binomial-to-normal-transformer)
        - [Normal to t Transformer](#normal-to-t-transformer)
        - [Difference in Mean to t Transformer](#difference-in-mean-to-t-transformer)
        - [Normal to Chi-squared Transformer](#normal-to-chi-squared-transformer)
        - [Normal to f Transformer](#normal-to-f-transformer)
    - [Hypotheses Test for Mean](#hypotheses-test-for-mean)
        - [HT: Mean with Known Variance](#ht-mean-with-known-variance)
        - [HT: Mean with Unknown Variance](#ht-mean-with-unknown-variance)
        - [HT: Difference in Mean with Known Variance](#ht-difference-in-mean-with-known-variance)
        - [HT: Difference in Mean with Unknown Variance](#ht-difference-in-mean-with-unknown-variance)
        - [HT: Difference in Mean with Unknown but Equal Variance](#ht-difference-in-mean-with-unknown-but-equal-variance)
        - [HT: Difference in Mean of Paired Data](#ht-difference-in-mean-of-paired-data)
    - [Hypotheses Test for Variance](#hypotheses-test-for-variance)
        - [HT: Variance](#ht-variance)
        - [HT: Ratio of Variance](#ht-ratio-of-variance)

## General Usage

### Displaying answers

The below function `disp` helps to print out all given arguments line by line, for sections with numerous values or answers.

```python
"""Prints variable number of input arguments on separate lines.
Additionally, prints a blank line at the end. Mainly useful for
displaying numerous answers in the same function.

Parameters
----------
answers : any, varargs
    The answers to be printed out.
"""
a = True
b = 10
c = 0.5
disp(a, b, c)

```

### Discrete pdf

For discrete p.d.f, calculation of the mean and variance requires the full set of data. The functions for computing both the mean and variance require a list of ordered pairs (given as tuples or lists).

Below is the function for calculating the mean, `find_mu`.

```python
"""Computes the mean, or expectation, for a given probability
distribution function.
Used for discrete cases where the pdf is not even.

Parameters
----------
pdf : float(2)[]
    The pdf to be computed. To be given as an array of ordered pairs,
    of (value, probability), which can be given as tuples.

Returns
-------
float
    The expectation of the pdf.
"""
pdf = [(1, 0.1), (2, 0.2), (3, 0.2), (4, 0.3), (5, 0.2)]
mean = find_mu(pdf)
```

Below is the function for calculating the variance, `find_var`.

```python
"""Computes the variance for a given probability
distribution function.
Used for discrete cases where the pdf is not even.

Parameters
----------
pdf : Tuple[float, float][]
    The pdf to be computed. To be given as an array of ordered pairs,
    of (value, probability), which can be given as tuples.

Returns
-------
float
    The variance of the pdf.
"""
pdf = [(1, 0.1), (2, 0.2), (3, 0.2), (4, 0.3), (5, 0.2)]
var = find_var(pdf)
```

### Z-distribution

Sometimes you get annoyed at having to specify 0 for mean, and 1 for variance.
The `z_cdf` function is to provide the cumulative distribution function value for the standard normal distribution, given a point on the distribution.

```python
"""Finds the cumulative distribution function value at x, of the
standard normal distribution, or z-distribution.

Parameters
----------
x : float
    The value of the z-distribution to compute.

Returns
-------
float
    The cdf of the z-distribution at the given value.
"""
prob = z_cdf(0.05)
```

### Paired Data

Paired data may sometimes be given as a full two sets of data. In which case, `paired_data` can be used to compute the mean and variance of the paired data.

The input order must match for both lists.

```python
"""Computes the sample mean and variance for difference in paired
data.

Parameters
----------
x : float[]
    The values of the first dataset, which is dependent on the other.

y : float[]
    The values of the second dataset, which is dependent on the other.

Returns
-------
Tuple[float, float]
    The sample mean and variance of the difference between x and y,
    given in the form of (mean, variance).
"""
x = [11.5, 11.7, 11.5, 11.8, 12.0, 12.2, 11.9]
y = [10.2, 10.3, 10.1, 10.6, 10.8, 11.3, 10.4]
mean, var = paired_data(x, y)
```

### Pooled Sample Variance

Sometimes there may be two different samples, but both with the same population variance, or maybe both from the same population. In such cases, we can use `pooled_sample_var` to compute the pooled variance for the samples.

```python
"""Computes the pooled sample variance for two samples with the same
population variance.

Parameters
----------
n : int[]
    The size of the samples. Must be a list of size 2.

sample_var : float[]
    The variance of the samples. Must be a list of size 2.

Returns
-------
float
    The value of the pooled sample variance.
"""
n = [15, 20]
sample_var = [3.2, 4.1]
pooled_var = pooled_sample_var(n, sample_var)
```

### Sum of Squares

The sum of squared differences with mean, is used primarily with the chi-squared distribution.

This sum of squares relate to sample variance through the following equation:

$$ \sum^n\_{i = 1} (X_i - \mu)^2 = (n - 1) S^2 $$

```python
"""Computes the sum of squared difference to mean, given that the
population mean is known.

Parameters
----------
entry : float[]
    The sample of data.

mu : float
    The population mean.

Returns
-------
float
    The value of the sum of squared difference to mean.
"""
entry = [4.2, 4.5, 3.8, 4.0, 3.6, 3.9, 4.1]
mu = 4.0
ssq = sum_squares(entry, mu)
```

## Confidence Intervals

Computing confidence intervals is important. So important, that we have built a function for every case of building such intervals (or, _at least_, within the syllabus of our module).

It is recommended to first compute all required arguments, then proceed to use the correct function accordingly.

### Interval Bounds

With confidence intervals, there is a lower and upper bound to which we are confident of the population statistic.

Below is the function to calculate the upper bound, `upper_bound`.

```python
"""Computes the probability value of the upper bound of the
confidence interval to be built.

Parameters
----------
conf_level : float
    The value of the confidence level.

Returns
-------
float
    The value of the upper bound of the interval.
"""
upper = upper_bound(0.95)
```

Below is the function to calculate the lower bound, `lower_bound`.

```python
"""Computes the probability value of the lower bound of the
confidence interval to be built.

Parameters
----------
conf_level : float
    The value of the confidence level.

Returns
-------
float
    The value of the lower bound of the interval.
"""
lower = lower_bound(0.95)
```

## CI for Mean

Majority of the cases are regarding means. For such cases, most of the time we would be using either the _normal distribution_, or the _t-distrbution_.

The general rule of thumb is, if the population variance is known, then use the **normal distribution**. But if the population variance is unknown, then use the **t-distribution**. But then again, if the size is large (greater than or equal to 30), then the t-distribution approximates to the normal distribution, so we can use the **normal diistrubtion** with the sample variance.

This applies for not just single variable, but also double variable samples.
Sometimes we want to find the mean of difference between two populations, whether they are independent or not. In these cases, the rules on variance are the same as above, but additionally, if the two populations share the same variance, then a more accurate variance can be used by calculating a **pooled sample variance**.

### CI: Mean with Known Variance

Below is the function `ci_known`, for when population variance is known.

```python
"""Constructs a confidence interval for a population mean, given
that the population variance is known.

Parameters
----------
mean : float
    The sample mean.

conf_level : float
    The value of the confidence level.

n : int
    The size of the sample.

std : float
    The standard deviation of the population.

Returns
-------
float[]
    The lower and upper bounds of the confidence interval respectively.
"""
mean = 4.5
conf_level = 0.95
n = 50
std = 1.5
ci = ci_known(mean, conf_level, n, std)
disp(ci)
```

### CI: Mean with Unknown Variance

Below is the function `ci_unknown` for when population variance is unknown.

```python
"""Constructs a confidence interval for a population mean, given
that the population variance is unknown.

Parameters
----------
mean : float
    The sample mean.

conf_level : float
    The value of the confidence level.

n : int
    The size of the sample.

sample_std : float
    The standard deviation of the sample.

Returns
-------
float[]
    The lower and upper bounds of the confidence interval respectively.
"""
mean = 4.5
conf_level = 0.95
n = 50
sample_std = 1.5
ci = ci_unknown(mean, conf_level, n, sample_std)
disp(ci)
```

### CI: Difference in Mean with Known Variance

Below is the function `diff_ci_known`, for when the population variance are both known.

```python
"""Constructs a confidence interval for the difference in mean for
two populations, given that the population variances for both are
known. Data for each statistic should be given in a consistent
ordering.

Parameters
----------
mean : float[]
    The sample mean. Must be a list of size 2.

conf_level : float
    The value of the confidence level.

n : int[]
    The size of the samples. Must be a list of size 2.

var : float
    The variance of the populations. Must be a list of size 2.

Returns
-------
float[]
    The lower and upper bounds of the confidence interval respectively.
"""
mean = [4.5, 3.0]
conf_level = 0.95
n = [30, 40]
var = [1.2, 0.8]
ci = diff_ci_known(mean, conf_level, n, var)
disp(ci)
```

### CI: Difference in Mean with Unknown Variance

Below is the function `diff_ci_unknown`, for when the population variance are unknown.

```python
"""Constructs a confidence interval for the difference in mean for
two populations, given that the population variances for both are
unknown. Data for each statistic should be given in a consistent
ordering.

Parameters
----------
mean : float[]
    The sample mean. Must be a list of size 2.

conf_level : float
    The value of the confidence level.

n : int[]
    The size of the samples. Must be a list of size 2.

sample_var : float
    The variance of the samples. Must be a list of size 2.

Returns
-------
float[]
    The lower and upper bounds of the confidence interval respectively.
"""
mean = [4.5, 3.0]
conf_level = 0.95
n = [30, 40]
sample_var = [1.2, 0.8]
ci = diff_ci_unknown(mean, conf_level, n, sample_var)
disp(ci)
```

### CI: Difference in Mean with Unknown but Equal Variance

Below is the function `diff_ci_equal`, for when the population variance are unknown, but equal.

```python
"""Constructs a confidence interval for the difference in mean for
two populations, given that the population variances for both are
unknown but equal. Data for each statistic should be given in a
consistent ordering.

Parameters
----------
mean : float[]
    The sample mean. Must be a list of size 2.

conf_level : float
    The value of the confidence level.

n : int[]
    The size of the samples. Must be a list of size 2.

sample_var : float
    The variance of the samples. Must be a list of size 2.

Returns
-------
float[]
    The lower and upper bounds of the confidence interval respectively.
"""
mean = [4.5, 3.0]
conf_level = 0.95
n = [30, 40]
sample_var = [1.2, 0.8]
ci = diff_ci_equal(mean, conf_level, n, sample_var)
disp(ci)
```

### CI: Difference in Mean of Paired Data

Below is the function `paired_ci`, for when there is paired data with the mean and variance already computed.

```python
"""Constructs a confidence interval for the difference in mean for
two populations, given a set of paired data that is dependent. Data
for each statistic should be given in a consistent ordering.

Parameters
----------
mean : float
    The sample mean.

conf_level : float
    The value of the confidence level.

n : int
    The size of the samples.

sample_var : float
    The variance of the samples.

Returns
-------
float[]
    The lower and upper bounds of the confidence interval respectively.
"""
mean = 0.2833333333333334
conf_level = 0.95
n = 6
sample_var = 0.005666666666666632
ci = paired_ci(mean, conf_level, n, sample_var)
disp(ci)
```

Below is the function `paired_ci_raw`, for when the paired data is given as raw data, and the statistics are not yet computed. The data should then be given as two lists, with matching order and indexing.

```python
"""Constructs a confidence interval for the difference in mean for
two populations, given a set of paired data that is dependent. This
raw version is for cases where only the raw data is available. Data
should be provided as lists with matching order and indexing.

Parameters
----------
x : float[]
    The values of the first data set. Must match the second set.

y : float[]
    The values of the second data set. Must match the first set.

conf_level : float
    The value of the confidence level.

Returns
-------
float[]
    The lower and upper bounds of the confidence interval respectively.
"""
x = [4.5, 4.6, 4.3, 4.4, 4.7, 4.6]
y = [4.2, 4.2, 4.1, 4.1, 4.5, 4.3]
conf_level = 0.95
ci = paired_ci_raw(x, y, conf_level)
disp(ci)
```

## CI for Variance

There are also confidence intervals for variance. These are fewer, and simpler to deal with.

For single variable cases, we only need to consider if the population mean is known or unknown. The distribution used is the same, and the only difference is in the use of the true population mean to compute a more accurate sum of squares, if it is known.

### CI: Variance with Known Mean

Below is the function `var_ci_known`, for when the population mean is known. In this case, the set of data has to be given together with the population mean in order to calculate the sum of squares.

```python
"""Constructs a confidence interval for the variance of a population,
given that the population mean is known. The full data set has to be
provided to accurately compute.

Parameters
----------
entry : float[]
    The sample of data.

mu : float
    The population mean.

n : int
    The size of the sample.

conf_level : float
    The value of the confidence level.

Returns
-------
float[]
    The lower and upper bounds of the confidence interval respectively.
"""
entry = [4.3, 4.4, 4.6, 4.3, 4.7, 4.2, 4.4, 4.5, 4.6]
mu = 4.5
conf_level = 0.95
ci = var_ci_known(entry, mu, conf_level)
disp(ci)
```

### CI: Variance with Unknown Mean

Below is the function `var_ci_unknown`, for when the population mean is unknown. Then, the sample variance is used and should be given as input.

```python
"""Constructs a confidence interval for the variance of a population,
given that the population mean is unknown.

Parameters
----------
sample_var : float
    The variance of the sample.

n : int
    The size of the sample.

conf_level : float
    The value of the confidence level.

Returns
-------
float[]
    The lower and upper bounds of the confidence interval respectively.
"""
sample_var = 1.2
n = 30
conf_level = 0.95
ci = var_ci_unknown(sample_var, n, conf_level)
disp(ci)
```

### CI: Ratio of Variance

Below is the function `ratio_var_ci`, for when the ratio of variance is to be used.

```python
"""Constructs a confidence interval for the ratio of variances of
two populations.

Parameters
----------
sample_var : float[]
    The variance of the samples. Must be a list of size 2.

n : int
    The size of the sample.

conf_level : float
    The value of the confidence level.

Returns
-------
float[]
    The lower and upper bounds of the confidence interval respectively.
"""
sample_var = [3.5, 4.5]
n = [20, 30]
conf_level = 0.95
ci = ratio_var_ci(sample_var, n, conf_level)
disp(ci)
```

## Hypotheses Testing

The last section, hypotheses testing, is another major part of statistics (and particularly, _our module_).

For the sake of easier computation, in this package, we do not calculate the acceptance and rejection regions, nor the critical points. Instead, we find the **p-values** and compare them with the specified **level of significance** to reach a conclusion for the test.

Apart from just the tests, we also provide functionality for transforming from one distribution to another, and for calculating **p-value** directly.

### p-value

Sometimes when we compute p-value, we trouble ourselves as we think about whether the test is two-tailed, one-tailed, in which direction, and so on. We use these functions to bypass this, by letting it handle the logic behind it, as we pass the probability of an event, and indicate which scenario the test is.

Here, if the test is two-tailed, then we use a value of `0` to indicate this. If the test is one-tailed and testing if the statistic is less than the hypothesized value, then we use `-1` to indicate this. If it is testing if the statistic is more than, we use `1` to indicate this.

Below is the function `p_value`, used to return the p-value for a test.

```python
"""Computes the appropriate p-value given the probability of an
event, and whether it is a two-tailed or one-tailed test.

Parameters
----------
p : float
    The probability of the event.

tail : int
    Indicates which case of hypothesis test it is. If the test is
    two-tailed, then the variable \'tail\' should be 0. If the
    test is one-tailed and the less than the value specified in the
    null hypothesis, the variable \'tail\' should be -1. Otherwise,
    it should be 1.

Returns
-------
float
    The p-value of sample for the test.
"""
p = 0.8
a = p_value(p, 0) #for two-tailed test
b = p_value(p, 1) #if more than in H_0
c = p_value(p, -1) #if less than in H_0
disp(a, b, c)
```

Below is the function `pv_calc`, which computes the probability of the event given a distribution, and relevant statistics. This can be used for normal, t, and chi-squared distributions, but not the f-distribution.

```python
"""Computes the p-value for a test. Can be used with the normal
distribution, t-distribution, chi2-distribution, but not the f-
distribution.

Parameters
----------
dist : class
    The specific distribution to be used for the test.

n : int
    The size of the sample.

mu : float
    The population mean, hypothesized or known.

var : float
    The population variance, hypothesized or known.

test_val : float
    The value that is obtained from data, and to be tested.

tails : int
    Indicates which tailed hypothesis test.

Returns
-------
float
    The appropriate p-value for the test.
"""
n = 30
mu = 5
var = 2
tails = 0

norm = pv_calc(st.norm, n, mu, var, 4.8, tails) #test 4.8 against 5 for normal
t = pv_calc(st.t, n, mu, var, 4.8, tails) #test 4.8 against 5 using t
chi = pv_calc(st.chi2, n, mu, var, 2.3, tails) #test 2.3 against 2 using chi2
disp(norm, t, chi)
```

Below is the function `pv_calc_f`, for calculating the p-value for an f-distribution.

```python
"""Computes the p-value for a test. Can only be used for the f-
distribution.

Parameters
----------
n1 : int
    The size of the first sample.

n2 : int
    The size of the second sample.

var1 : float
    The hypothesized variance of the first population.

var2 : float
    The hypothesized variance of the second population.

sample_var1 : float
    The sum of squares for the first sample.

sample_var2 : float
    The sum of squares for the second sample.

tails : int
    Indicates which tailed hypothesis test.

Returns
-------
float
    The appropriate p-value for the test.
"""
n1, n2 = 24, 28
var1, var2 = 2.2, 2.4
sample_var1, sample_var2 = 2.4, 2.8
tails = 0
pv = pv_calc_f(n1, n2, var1, var2, sample_var1, sample_var2, tails)
```

### Concluding the Test

Sometimes we may forget how to compare two numbers. Or maybe more realistically, forget how to properly conclude a hypothesis test after obtaining the p-value.

This function `comp_p_alpha` can help with that.

```python
"""Compares a given p-value with a given level of significance, and
returns the test conclusion.

Parameters
----------
pv : float
    The p-value of the test.

alpha : float
    The level of significance of the test.

Returns
-------
string
    The conclusion of the Hypothesis Test.
"""
pv = 0.02
alpha = 0.05
disp(comp_p_alpha(pv, alpha))
```

## Transformers

Sometimes we need to transform certain statistics from one distribution to another. This is mostly done as intermediate workings, and in this package, the following transformers should be used largely by the final hypothesis test functions.
However, it is still definitely feasible to use them by themselves, though they require more caution.

### Binomial to Normal Transformer

Below is the function `binom_norm_transformer`, which approximates a binomial distribution to a normal distribution.

```python
"""Provides a unary function to transform a binomial statistic to
the standard normal distribution.

Parameters
----------
n : int
    The size parameter, typically n, of the binomial distribution.

p : float
    The probability of a success of the binomial distribution.

Returns
-------
lambda
    A unary function.
"""
n = 20
p = 0.4
transformer = binom_norm_transformer(n, p)
```

### Normal to t Transformer

Below is the function `norm_t_transformer`, which transforms a normal distribution to a t distribution.

```python
"""Provides a unary function to transform a normal statistic to
the t-distribution, with a specific degree of freedom.

Parameters
----------
n : int
    The size of the sample.

mu : float
    The hypothesized mean of the population.

sample_var : float
    The variance of the sample.

Returns
-------
lambda
    A unary function.
"""
n = 10
mu = 5
sample_var = 3
transformer = norm_t_transformer(n, mu, sample_var)
```

### Difference in Mean to t Transformer

Below is the function `diff_t_transformer`, which transforms two normal distributions to a t distribution by taking the difference in mean.

```python
"""Provides a binary function to transform two normal statistics to
the t-distribution, with a specific degree of freedom. Can be used
regardless of whether population variance is known or unknown.

Parameters
----------
n : int[]
    The size of the samples. Must be given as a list of size 2.

mu : float[]
    The hypothesized mean of the populations. Must be a list of size 2.

var : float[]
    The variance of the sample or population. Must be a list of size 2.

Returns
-------
lambda
    A binary function.
"""
n = [15, 18]
mu = [4.5, 4.2]
var = [2.2, 2.4]
transformer = diff_t_transformer(n, mu, var)
```

### Normal to Chi-squared Transformer

Below is the function `norm_chi2_transformer`, which transforms a normal distribution to a chi-squared distribution.

```python
"""Provides a unary function to transform a normal statistic to
the chi2-distribution, with a specific degree of freedom.

Parameters
----------
n : int
    The size of the sample.

var : float
    The hypothesized variance of the population.

Returns
-------
lambda
    A unary function.
"""
n = 20
var = 4.2
transformer = norm_chi2_transformer(n, var)
```

### Normal to f Transformer

Below is the function `norm_f_transformer`, which transforms two normal distributions to an f-distribution by taking the ratio of variance.

```python
"""Provides a binary function to transform two sum of squares to
the f-distribution, with specific degrees of freedom.

Parameters
----------
var1 : float
    The hypothesized variance of the first population.

var2 : float
    The hypothesized variance of the second population.

Returns
-------
lambda
    A binary function.
"""
var1 = 2.2
var2 = 2.4
transformer = norm_f_transformer(var1, var2)
```

## Hypotheses Test for Mean

Majority of the cases are regarding means. For such cases, most of the time we would be using either the _normal distribution_, or the _t-distrbution_.

The general rule of thumb is, if the population variance is known, then use the **normal distribution**. But if the population variance is unknown, then use the **t-distribution**. But then again, if the size is large (greater than or equal to 30), then the t-distribution approximates to the normal distribution, so we can use the **normal diistrubtion** with the sample variance.

This applies for not just single variable, but also double variable samples.
Sometimes we want to find the mean of difference between two populations, whether they are independent or not. In these cases, the rules on variance are the same as above, but additionally, if the two populations share the same variance, then a more accurate variance can be used by calculating a **pooled sample variance**.

(Yes, this is the same as [Confidence Intervals](#confidence-intervals))

### HT: Mean with Known Variance

Below is the function `mean_hypotest_known`, for when the population variance is known.

```python
"""Conducts a hypothesis test on the mean of a sample, given that
the population variance is known.

Parameters
----------
x_bar : float
    The mean of the sample.

mu : float
    The hypothesized mean of the population.

var : float
    The variance of the population.

n : int
    The size of the sample.

alpha : float
    The level of significance of the test.

tails : int
    Indicates which tailed hypothesis test it is.

Returns
-------
string
    The conclusion of the test.
"""
x_bar, mu, var, n = 4.5, 5, 1.5, 30
alpha = 0.05
tails = 0
ans = mean_hypotest_known(x_bar, mu, var, n, alpha, tails)
disp(ans)
```

### HT: Mean with Unknown Variance

Below is the function `mean_hypotest_unknown`, for when the population variance is unknown.

```python
"""Conducts a hypothesis test on the mean of a sample, given that
the population variance is unknown.

Parameters
----------
x_bar : float
    The mean of the sample.

mu : float
    The hypothesized mean of the population.

var : float
    The variance of the sample.

n : int
    The size of the sample.

alpha : float
    The level of significance of the test.

tails : int
    Indicates which tailed hypothesis test it is.

Returns
-------
string
    The conclusion of the test.
"""
x_bar, mu, sample_var, n = 4.5, 5, 1.5, 30
alpha = 0.05
tails = 0
ans = mean_hypotest_unknown(x_bar, mu, sample_var, n, alpha, tails)
disp(ans)

```

### HT: Difference in Mean with Known Variance

Below is the function `diff_hypotest_known`, for when both population variance are known. If the hypothesized means are not individually known, just the relative difference in mean has to be represented correctly.

```python
"""Conducts a hypothesis test on the difference of means of two
samples, given that the population variance are known.

Parameters
----------
x_bar : float[]
    The mean of the samples. Must be a list of size 2.

mu : float[]
    The hypothesized mean of the populations. Must be a list of
    size 2. If no specific mean are known, then only the relative
    difference in means is required to be accurate.

var : float[]
    The variance of the populations. Must be a list of size 2.

n : int[]
    The size of the samples. Must be a list of size 2.

alpha : float
    The level of significance of the test.

tails : int
    Indicates which tailed hypothesis test it is.

Returns
-------
string
    The conclusion of the test.
"""
x_bar, mu, var, n = [5.0, 4.5], [5.2, 4.6], [1.2, 1.1], [24, 18]
alpha = 0.05
tails = 0
ans1 = diff_hypotest_known(x_bar, mu, var, n, alpha, tails)
mu2 = [0, 0]
ans2 = diff_hypotest_known(x_bar, mu2, var, n, alpha, tails)
disp(ans1, ans2)
```

### HT: Difference in Mean with Unknown Variance

Below is the function `diff_hypotest_unknown`, for when the population variance are unknown. If the hypothesized means are not individually known, just the relative difference in mean has to be represented correctly

```python
"""Conducts a hypothesis test on the difference of means of two
samples, given that the population variance are unknown.

Parameters
----------
x_bar : float[]
    The mean of the samples. Must be a list of size 2.

mu : float[]
    The hypothesized mean of the populations. Must be a list of
    size 2. If no specific mean are known, then only the relative
    difference in means is required to be accurate.

var : float[]
    The variance of the samples. Must be a list of size 2.

n : int[]
    The size of the samples. Must be a list of size 2.

alpha : float
    The level of significance of the test.

tails : int
    Indicates which tailed hypothesis test it is.

Returns
-------
string
    The conclusion of the test.
"""
x_bar, mu, sample_var, n = [5.0, 4.5], [5.2, 4.6], [1.2, 1.1], [24, 18]
alpha = 0.05
tails = 0
ans1 = diff_hypotest_unknown(x_bar, mu, sample_var, n, alpha, tails)
mu2 = [0, 0]
ans2 = diff_hypotest_unknown(x_bar, mu2, sample_var, n, alpha, tails)
disp(ans1, ans2)
```

### HT: Difference in Mean with Unknown but Equal Variance

Below is the function `diff_hypotest_equal`, for when the population variance are both unknown but equal. If the hypothesized means are not individually known, just the relative difference in mean has to be represented.

```python
"""Conducts a hypothesis test on the difference of means of two
samples, given that the population variance are unknown but equal.

Parameters
----------
x_bar : float[]
    The mean of the samples. Must be a list of size 2.

mu : float[]
    The hypothesized mean of the populations. Must be a list of
    size 2. If no specific mean are known, then only the relative
    difference in means is required to be accurate.

var : float[]
    The variance of the samples. Must be a list of size 2.

n : int[]
    The size of the samples. Must be a list of size 2.

alpha : float
    The level of significance of the test.

tails : int
    Indicates which tailed hypothesis test it is.

Returns
-------
string
    The conclusion of the test.
"""
x_bar, mu, sample_var, n = [5.0, 4.5], [5.2, 4.6], [1.2, 1.1], [24, 18]
alpha = 0.05
tails = 0
ans1 = diff_hypotest_equal(x_bar, mu, sample_var, n, alpha, tails)
mu2 = [0, 0]
ans2 = diff_hypotest_equal(x_bar, mu2, sample_var, n, alpha, tails)
disp(ans1, ans2)
```

### HT: Difference in Mean of Paired Data

Below is the function `paired_hypotest`, for when the mean and variance for paired data is already computed.

```python
"""Conducts a hypothesis test on the difference of means of two
populations, given a set of paired data.

Parameters
----------
d_bar : float
    The mean of the difference of paired data.

mu_d : float
    The hypothesized mean of difference in the populations.

var : float
    The variance of the samples.

n : int
    The size of the samples.

alpha : float
    The level of significance of the test.

tails : int
    Indicates which tailed hypothesis test it is.

Returns
-------
string
    The conclusion of the test.
"""
mean = 0.2833333333333334
sample_var = 0.005666666666666632
d_bar, mu_d, var, n = 20.283333333333333, 0, 0.005666666666666632, 6
alpha = 0.05
tails = 0
ans = paired_hypotest(d_bar, mu_d, var, n, alpha, tails)
disp(ans)
```

Below is the function `paired_hypotest_raw`, for when only the raw set of paired data is available, and the mean and variance are not yet available.

```python
"""Conducts a hypothesis test on the difference of means of two
populations, given a set of paired data. This raw version is provided
for cases where only the raw data is available.

Parameters
----------
x : float[]
    The first set of data. Must match with the second set.

y : float[]
    The second set of data. Must match with the first set.

mu_d : float
    The hypothesized mean of difference in the populations.

alpha : float
    The level of significance of the test.

tails : int
    Indicates which tailed hypothesis test it is.

Returns
-------
string
    The conclusion of the test.
"""
x = [4.5, 4.6, 4.3, 4.4, 4.7, 4.6]
y = [4.2, 4.2, 4.1, 4.1, 4.5, 4.3]
mu_d = 0
alpha = 0.05
tails = 0
ans = paired_hypotest_raw(x, y, mu_d, alpha, tails)
disp(ans)
```

## Hypotheses Test for Variance

There are also hypotheses tests for variance. These are fewer, and simpler to deal with.

### HT: Variance

Below is the function `var_hypotest`. Can be used regardless of the population mean.

```python
"""Conducts a hypothesis test on the variance of a sample.

Parameters
----------
sample_var : float
    The variance of the sample.

var : float
    The hypothesized variance of the population.

n : int
    The size of the sample.

alpha : float
    The level of significance of the test.

tails : int
    Indicates which tailed hypothesis test it is.

Returns
-------
string
    The conclusion of the test.
"""
sample_var, var, n = 3.2, 3, 40
alpha = 0.05
tails = 0
ans = var_hypotest(sample_var, var, n, alpha, tails)
disp(ans)
```

### HT: Ratio of Variance

Below is the function `var_ratio_hypotest`, for comparing variance of two normal distributions. If the individual variance are not known, then only the relative ratio has to be represented correctly.

```python
"""Conducts a hypothesis test on the ratio of variance of two
populations.

Parameters
----------
sample_var : float[]
    The variance of the samples. Must be a list of size 2.

var : float[]
    The hypothesized variance of the population. Must be a list of
    size 2. If the specific variance are not known, then only the
    relative variance provided has to be accurate.

n : int
    The size of the sample.

alpha : float
    The level of significance of the test.

tails : int
    Indicates which tailed hypothesis test it is.

Returns
-------
string
    The conclusion of the test.
"""
sample_var, var, n = [2.3, 2.6], [2.2, 2.5], [20, 25]
alpha = 0.05
tails = 0
ans1 = var_ratio_hypotest(sample_var, var, n, alpha, tails)
var2 = [1, 1] #if variance is not known
ans2 = var_ratio_hypotest(sample_var, var2, n, alpha, tails)
disp(ans1, ans2)
```