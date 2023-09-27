GRAVITY = 9.81

def get_fall_time(m, g = GRAVITY):
    d = m
    t = ((2*d)/g)**(1/2)
    return t

print(get_fall_time(20))
print(get_fall_time(20, 1.62))
verdier = input("Skriv inn meter og gravitasjon med mellomrom i mellom dem: ")
liste_verdier = [float(x) for x in verdier.split(' ')]
print(liste_verdier)
m = liste_verdier[0]
if len(liste_verdier) == 2:
    g = liste_verdier[1]
tid = round(get_fall_time(m, g), 2)

print("Det tar", tid, "sekunder for et objekt i fritt fall å ramle", m, "meter med gravitasjonen", g, "m/s^2")