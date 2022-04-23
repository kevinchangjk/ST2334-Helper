from functions import *

# Questions below

def q3():
    y = [(2, 5/18), (8, 1/6), (-3, 10/18)]
    ex = find_mu(y)
    var = find_var(y)
    sd = var ** 0.5
    disp(ex, sd)

def q4():
    x = [37.4, 48.8, 46.9, 55.0, 44.0]
    var = sta.variance(x)
    conf = 0.9
    ci = ci_unknown(sta.mean(x), conf, 5, var ** 0.5)
    n = error_min_size(0.9, (var*5)** 0.5, 5)
    disp(var, ci, n)

def q5():
    a = 0.01
    lower = st.norm.ppf(1 - a)
    upper = st.norm.ppf(1 - a/2)
    disp(lower, upper)

def q6():
    n1 = 12
    mean1 = 4.163
    sd1 = 0.9562
    n2 = 8
    mean2 = 5.105
    sd2 = 1.6098
    a = 0.05
    ht = diff_hypotest_equal([mean1, mean2], [0, 0], [sd1**2, sd2**2], [n1, n2], a, -1)
    disp(ht)

# Generate solutions below

# q3()
q4()
# q5()
# q6()
