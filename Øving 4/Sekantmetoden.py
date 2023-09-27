from math import e

def f(x):
    f = (x - 12) * e ** (x / 2) - 8 * (x + 2) ** 2
    return f

def g(x):
    g = -x - 2*x**2 - 5*x**3 + 6*x**4
    return g

def differentiate(x_k, x_k1, func):
    derivert = (func(x_k) - func(x_k1))/(x_k - x_k1)
    return derivert

def secant_method(x0, x1, func, tol):
    derivert = differentiate(x1, x0, func)
    while derivert > tol:
        x2 = x1 - func(x1)*(x1 - x0)/(func(x1)-func(x0))
        derivert = differentiate(x2, x1, func)
        x0 = x1
        x1 = x2
    return x1
    print("Funksjonen nærmer seg et nullpunkt når x =", x1, ", da er f(x) =", f(x1))

secant_method(11, 13, f, 0.00001)