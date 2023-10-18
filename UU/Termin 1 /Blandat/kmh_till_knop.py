# Author: Oscar Wiklund Jonsson
# Date: 10/10 - 2023
# Omvandla från KM/H till Knop

omvandlingsfaktor = 1.852
knop = 0
kmh = int(input("Skriv hastighet i kmh: ")) # Input från användaren

knop = omvandlingsfaktor * kmh # Multiplicerar omvandlingsfaktorn med inputen(kmh)
print ((str(kmh)) + " km/h motsvarar " + (str(knop)) + " knop") # Skriver ut resultatet
