# Author: Oscar Wiklund Jonsson
# Date: 16/10 - 2023

#En konsolbaserad anteckningsbok där användaren kan ange text som sparas i en textfil med dagens datum som rubrik.

import datetime

dagens_datum = datetime.datetime.now().strftime("%Y-%m-%d")

def skapa_eller_oppna():
    filnamn = f"anteckning_{dagens_datum}.txt"

    try:
        anteckning_fil = open(filnamn, "a")  # "a" läge öppnar filen för att lägga till
        return anteckning_fil
    except FileNotFoundError:
        print(f"Kunde inte öppna filen {filnamn}.")
        quit()


# Funktion för att skriva ett nytt inlägg i anteckningsboken
def nytt_inlagg():
    datum = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    innehall = input("Skriv ditt inlägg: ")

    with skapa_eller_oppna() as anteckning_fil:
        anteckning_fil.write(f"{datum}\n")
        anteckning_fil.write(innehall + "\n\n")
    print("Anteckningen har sparats.")

# Huvudprogram
print("Välkommen")
while True:
    print("\nVad vill du göra?")
    print("1. Skriv ett nytt inlägg")
    print("2. Öppna anteckning")
    print("3. Avsluta")
    val = input("Välj ett alternativ: ")

    if val == "1":
        nytt_inlagg()
    elif val == "2":
        print("Ej implementerat")
    elif val == "3":
        print("Stänger av")
        break
    else:
        print("Ogiltigt val. Försök igen.")