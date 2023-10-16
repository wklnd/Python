# Author: Oscar Wiklund Jonsson
# Date: 10/10 - 2023
# Omvandla från KM/H till Knop

knop = 1.852
speed = 0
kmh = int(input("Skriv hastighet i kmh: ")) # Input från användaren

speed = knop * kmh # Multiplicerar omvandlingsfaktorn med inputen(kmh)
print ((str(knop)) + " knop motsvarar " + (str(speed)) + " km/h") # Skriver ut resultatet
