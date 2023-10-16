# Author: Oscar Wiklund Jonsson
# Date: 13/10 - 2023
# Generara ASCII konst baserat på input string.
"""
Koden tar ASCII text och renderar ut det i ASCII art.

Fonts kan man bland annat hitta i denna lista: http://www.figlet.org/fontdb.cgi
"""

import pyfiglet
string = input("Enter the text: ")
text = pyfiglet.figlet_format(string, font="wavy")
print(text)