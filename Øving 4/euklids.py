def reduce_fraction(a, b): 
    a_1 = a
    b_1 = b
    while b_1 != 0:
        gammel_b = b_1
        b_1 = a_1%b_1
        a_1 = gammel_b
        d = a_1
    return a/d, b/d

reduce_fraction(5, 10)