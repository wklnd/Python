# Author: Oscar Wiklund Jonsson
# Date: 15/10 - 2023
# Kastar en tärning, antal sidor på tärningen anges av användaren.
# Varje gång användaren trycker på "Enter" kastas tärningen och resultatet visas.


import random

def throw_dice(num_sides):
    return random.randint(1, num_sides)

def main():
    num_sides = int(input("Välj antal sidor på tärningen:"))
    while True:
        input("Tryck på enter för att kasta tärningen:")
        result = throw_dice(num_sides)
        print("Du fick en: ", result)

if __name__ == "__main__":
    main()
