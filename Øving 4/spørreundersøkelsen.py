from sys import exit

#globale variabler
antall_kvinner = 0
antall_menn = 0
antall_fag = 0
antall_ITGK = 0
antall_timer_lekser = 0

#avslutter løkka og skriver ut statistikk
def sjekk_svar(svar):
    if svar == "hade":
        print("Da var spørreundersøkelsen over! Her er resultatene:\n")
        #statistikk
        print("Antall kvinner:", antall_kvinner, "\nAntall menn:", antall_menn, 
        "\nAntall som tar fag:", antall_fag, "\nAntall som tar ITGK:", antall_ITGK, 
        "\nAntall timer i snitt brukt på lekser:", round(antall_timer_lekser, 2))
        exit()

def les_ja_nei(svar):
    global fag
    while not (fag == "ja" or fag == "nei"):
        fag = input("Tar du et fag? (ja/nei) ")
    return fag

#gir variabelen en verdi slik at koden kan kjøre
svar = "ja"

while svar != "hade":
    
    print("\nVelkommen til spørreundersøkelsen!\n")

    #kjønn
    kjønn = input("Hvilket kjønn er du? (f/m) ")
    sjekk_svar(kjønn)
    
    if kjønn == "f":
        antall_kvinner += 1
    elif kjønn == "m":
        antall_menn += 1

    #alder
    alder = input("Hvor gammel er du? ")
    sjekk_svar(alder)

    #sjekke om de får være med
    if int(alder) < 16 or int(alder) > 25:
        print("Du kan ikke ta spørreundersøkelsen.")

    else:
        fag = input("Tar du et fag? (ja/nei) ")
        sjekk_svar(fag)
        les_ja_nei(fag)
        
        if fag == "ja":
            antall_fag += 1
            
            if int(alder) < 22:
                itgk = input("Tar du ITGK? (ja/nei) ")
            else:
                itgk = input("Tar du virkelig ITGK? (ja/nei) ")
            
            sjekk_svar(itgk)
            if itgk == "ja":
                antall_ITGK += 1
            
            timer_lekser = input("Hvor mange timer bruker du normalt på lekser? ")
            sjekk_svar(timer_lekser)

            antall_timer_lekser = int(timer_lekser)/(antall_kvinner + antall_menn) 