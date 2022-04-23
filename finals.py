from functions import *

# Questions below

def q6():
    mu = 6
    ans = 1 - st.poisson.cdf(3, mu)
    disp(ans)

def q8():
    x = [(4, 0.4), (5, 0.3), (7, 0.2), (11, 0.1)]
    var = find_var(x)
    disp(var)

def q10():
    n = 20
    p = 0.05
    ans = st.binom.cdf(1, n, p)
    disp(ans)

def q12():
    x = [10.1, 9.8, 10.2, 10.4, 9.8, 10.0, 10.2, 9.6]
    n = 8
    conf = 0.95
    mean = sta.mean(x)
    var = sta.variance(x)
    ci = ci_unknown(mean, conf, n, var**0.5)
    disp(ci)

def q13():
    x = [46.4, 46.1, 45.8, 47.0, 46.1, 45.9, 45.8, 46.9, 46.0]
    n = 9
    conf = 0.95
    var = sta.variance(x)
    ci = var_ci_unknown(var, n, conf)
    disp(ci)

def q14():
    mu = 50
    xb = 46
    sd = 5.9
    n = 9
    a = 0.05
    ht = mean_hypotest_unknown(xb, mu, sd**2, n, a, -1)
    disp(ht)

def q15():
    sd = 0.9
    ssd = 1.1
    a = 0.05
    n = 12
    ht = var_hypotest(ssd**2, sd**2, n, a, 1)
    disp(ht)

def q20():
    mu = -10
    var = 15**2 + 20**2
    ans = 1 - st.norm.cdf(0, mu, var**0.5)
    disp(ans)

def q26():
    e = 1
    sd = 10
    conf = 0.95
    n = error_min_size(conf, sd * 2**0.5, e)
    disp(n)

def q27():
    n = 10
    var = 9
    xb = 0
    conf = 0.95
    # ci = ci_unknown(xb, conf, n, var**0.5)
    # extra_p = st.t.cdf(ci[0], n-1)
    value = st.t.ppf(conf, n-1)
    ans = value * (var / n)**0.5
    disp(ans)

def q28():
    var = 100
    n = 25
    a = 0.1
    p = 1 - st.norm.cdf(2.56, 1.5, (100/n)**0.5)
    disp(p)

def q29():
    n = 9
    mu = 1
    sd = 1
    mean = 0.4
    a = 0.05
    ht = mean_hypotest_known(mean, mu, sd**2, n, a, 1)
    disp(ht)

def q33():
    x1 = lambda x: st.poisson.pmf(x, 2)
    x2 = lambda x: st.poisson.pmf(x, 2)
    x3 = lambda x: st.poisson.pmf(x, 3)
    p = lambda a, b, c: x2(a) * x1(b) * x3(c)
    ans = p(0, 2, 4) + p(1, 1, 3) + p(2, 0, 2)
    disp(ans)

# Generate solutions below

# q6()
# q8()
# q10()
# q12()
# q13()
# q14()
# q15()
# q20()
# q26()
# q27()
# q28()
# q29()
q33()
