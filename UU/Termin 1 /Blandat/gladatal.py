def är_lycklig(n):
    while n != 1 and n != 4: # Medan talet "n" inte är lika med 1 och inte är lika med 4, fortsätt
        n = sum(int(digit) ** 2 for digit in str(n)) # Beräkna summan av kvadraten av varje siffra i talet "n"
    return n == 1 # Om beräkningsprocessen når talet 1, är det ett lyckligt tal och funktionen returnerar True

övre_gräns = 100 # Övregräns

glada_tal = []

# Loopa igenom talen från 1 till övre_gräns
for num in range(1, övre_gräns + 1):
    # Använd funktionen `är_lycklig` för att avgöra om `num` är ett "lyckligt tal."
    if är_lycklig(num):
        # Om det är ett glatt tal, lägg till det i listan glada_tal.
        glada_tal.append(num)

print(f"Glada tal mellan 1 och {övre_gräns}:")
print(glada_tal)