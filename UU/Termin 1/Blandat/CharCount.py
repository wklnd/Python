# Läs in en mening från användaren
sentence = input("Skriv in en mening: ")

# Kontrollera om meningen är tom
if not sentence:
    print("Meningen är tom.")
else:
    while True:
        # Läs in ett tecken från användaren
        char = input("Skriv in ett tecken: ")

        # Kontrollera om inmatningen är ett enda tecken
        if len(char) == 1:
            # Räkna antalet tecken i meningen
            total_chars = len(sentence)

            # Räkna hur många gånger det angivna tecknet förekommer i meningen
            char_count = sentence.count(char)

            # Hitta indexplatsen för den första förekomsten av tecknet
            first_index = sentence.find(char)

            # Hitta indexplatsen för den sista förekomsten av tecknet
            last_index = sentence.rfind(char)

            # Visa resultatet
            print(f"Meningen har totalt {total_chars} tecken.")
            print(f"Tecknet '{char}' förekommer {char_count} gång(er).")
            if char_count > 0:
                print(f"Indexplatsen för första förekomsten av '{char}' är {first_index}.")
                print(f"Indexplatsen för sista förekomsten av '{char}' är {last_index}.")
            break
        else:
            print("Du måste ange ett enda tecken.")
