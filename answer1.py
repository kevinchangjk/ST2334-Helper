from functions import *

# Questions below

def q1():
    sd = 4.5
    p = 0.8413
    v = st.norm.ppf(p, 0, 1)
    x = 58.5
    mu = x - (v * sd)

    p_mid = st.norm.cdf(60, mu, sd) - st.norm.cdf(51, mu, sd)
    b = p_mid ** 4

    ssd = sd / 4**0.5
    c = st.norm.cdf(60, mu, ssd) - st.norm.cdf(51, mu, ssd)
    disp(mu, b, c)

def q2():
    n = 49
    mean = 4.5
    ssd = 0.75
    conf = 0.95
    ci = ci_unknown(mean, conf, n, ssd)
    mu = 4.3
    a = 0.05
    aii = mean_hypotest_unknown(mean, mu, ssd**2, n, a, 0)

    e = 0.1
    zv = st.norm.ppf((1 - conf)/2 + conf)
    n = (zv * ssd / e) ** 2
    n2 = error_min_size(conf, ssd, e)

    bi = "Yes. The sample mean is an unbiased estimator the population mean, with increasing accuracy as n increases."
    bii = "No, the scores themselves may not follow the normal distribution. There is no evidence for this."
    disp(ci, aii, n, n2, bi, bii)

def q3():
    n = 13
    xbar = 30.59
    sx = 2.13
    ybar = 27.78
    sy = 1.73
    ht1 = var_ratio_hypotest([sx**2, sy**2], [1, 1], [n, n], 0.05, 0)

    a = 0.01
    ht = diff_hypotest_equal([xbar, ybar], [0, 0], [sx**2, sy**2], [n, n], a, 1)
    pooled_var = pooled_sample_var([n, n], [sx**2, sy**2]) ** 0.5
    pv_ans = ((2.13**2 / 2 + 1.73**2 / 2)) ** 0.5
    tv = st.t.ppf(0.000571165948392238, 24)
    pv = 1 - st.t.cdf(3.69, 24)

    # ht2 = diff_hypotest_unknown([xbar, ybar], [0, 0], [pv_ans**2, pv_ans**2], [n, n], a, 1)

    b = "No it is not. A two-sided p-value of 0.03 suggests that the probability of getting a mean of 2 is 0.015. But the CI suggests that the lower bound of 1.5 has a probability of 0.025, which is higher than the previous value."
    disp(ht, pooled_var, pv_ans, tv, pv)

def q4():
    i = 1/8
    ii = i **2 * 2
    iii = 1/5 * 1/3
    iv = iii /2
    v = ii / 2
    disp(i, ii, iii, iv, v)

def q5():
    c = (3 ** 0.5) - 1
    b = "I don't know man"
    disp(c, b)

def q6():
    i = "Integrate the pdf from x = 0 to x = 0.25, and y = 0 to y = 0.25"
    ii = "Integrate the pdf from y = 0 to y = 1, to get the pdf for x, then integrate from x = 0.25 to x = 0.75"
    iii = "Take the joint pdf divided by the pdf of x, and sub in x = 0.8, then integrate from 0 <= y <= 0.5"
    iv = "Taking the funky conditional pdf from before, now integrate with a y multiple at the front"

def test():
    conf_level = 0.95
    std = 1.5
    err = 0.1
    min_size = error_min_size(conf_level, std, err) #returns 
    disp(min_size)

# Generate solutions below

# q1()
# q2()
# q3()
# q4()
# q5()
# q6()
test()
