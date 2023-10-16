# Author: Oscar Wiklund Jonsson
# Date: 13/10 - 2023
# Omvandla från Celcius till Fahrenheit
"""
För att omvandla från Celcius till Fahrenheit, Multiplicera med 9, dividera med 5 och lägg till 32
"""
# Användare anger temperaturen i Celsius
celcius = float(input("Ange temperaturen i Celsius: "))

# Omvandla Celsius till Fahrenheit
fahrenheit = (celcius * 9)/5 + 32

# Visa resultatet
print(f"{celcius}°C motsvarar {fahrenheit}°F")