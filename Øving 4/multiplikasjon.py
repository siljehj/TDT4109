def funksjon(tol):
    count = 0
    prod = 1
    while endring > tol:
        for i in range(1, 20):
            gammelt_prod = prod
            prod *= (1 + 1/i**2)
            count += 1
            endring = prod - gammelt_prod
        return prod, count

a, b = funksjon(0.01)
print("Produktet ble", round(a, 2), "etter", b, "iterasjoner.")

#Hvordan kan man skrive endringen i produktet?
#endring  = prod - gammelt_prod 