# Author: Oscar Wiklund Jonsson
# Date: 13/10 - 2023

# Uppgiften var att lösa följande problem:
# Skapa ett Python-program som interagerar med användaren och ber dem att ange ett heltal mellan 1 och 100.
# Programmet ska sedan generera en utskrift som visar nummer från 1 till det angivna talet.
# Varje nummer ska upprepas så många gånger som numret självt.
# Dessutom ska programmet hantera felaktiga inmatningar och meddela användaren om de anger ett nummer som inte ligger inom det angivna intervallet (1-100) eller om de inte anger ett giltigt heltal.

# Försök att utföra följande kodblock
try:
    # Be användaren att ange ett heltal mellan 1 och 100
    user_input = int(input("Skriv in ett nummer mellan 1-100: "))

    # Kontrollera om användarens inmatning är inom intervallet 1-100
    if 1 <= user_input <= 100:
        # Om inmatningen är giltig, loopa från 1 till användarens inmatning
        for number in range(1, user_input + 1):
            # Skriv ut numret upprepade gånger enligt dess värde
            print(f"{number} " * number)
    else:
        # Om inmatningen inte är inom intervallet, skriv ett felmeddelande
        print("Numret är inte mellan 1-100")

# Hantera ett undantag om användaren inte anger ett heltal
except ValueError:
    # Skriv ett felmeddelande om inmatningen inte är ett heltal
    print("Numret är inte mellan 1-100.")
