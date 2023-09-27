from math import e

def f(x):
    f = (x - 12)*e**(x / 2) - 8*(x + 2)**2
    return f

def g(x):
    g = -x - 2*x**2 - 5*x**3 + 6*x**4
    return g

def differentiate(x_k, x_k1, func):
    derivert = (func(x_k) - func(x_k1))/(x_k - x_k1)
    return derivert

def secant_method(x0, x1, func, tol):
    while True:
        endring = abs(x1 - x0)
        if endring < tol:
            return x1
        derivert = differentiate(x1, x0, func)
        x2 = x1 - (func(x1)/derivert)
        x0 = x1
        x1 = x2

x_1 = secant_method(11,13,f,0.00001)
x_2 = secant_method(1,2,g,0.00001)
x_3 = secant_method(0,1,g,0.00001)

print("Funksjonen nærmer seg et nullpunkt når x =", round(x_1, 2), ", da er f(x) =", round(f(x_1), 8))
print("Funksjonen nærmer seg et nullpunkt når x =", round(x_2, 2), ", da er g(x) =", round(g(x_2), 10))
print("Funksjonen nærmer seg et nullpunkt når x =", round(x_3, 2), ", da er g(x) =", round(g(x_3), 2))    