from functions import *

# Questions below

def q5():
    mean = 6.09
    sd = 0.02
    e = 0.001
    conf = 0.9
    n1 = error_min_size(conf, sd, e)
    n = 1219
    xb = 6.048
    s = 0.022
    ci = ci_unknown(xb, conf, n, s)

    b = 1 - st.binom.cdf(54, 100, 0.5)
    disp(n1, ci, b)

def q6():
    xb = 72.9
    sx = 25.6
    yb = 81.7
    sy = 28.3
    n1 = 13
    n2 = 16
    a = 0.05
    ht = diff_hypotest_unknown([xb, yb], [0, 0], [sx**2, sy**2], [n1, n2], a, -1)
    disp(ht)

# Generate solutions below

# q5()
q6()
