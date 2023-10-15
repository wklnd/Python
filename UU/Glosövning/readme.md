# Glosövning

Glosövning är ett enkelt program som låter användaren öva på översättningen mellan två olika språk. Användaren ges en lista med ord på ett språk och måste ange motsvarande ord på ett annat språk. Programmet ger feedback om översättningen är korrekt, nästan korrekt eller fel.

## Funktioner

- Välj mellan olika språk: Programmet stöder flera språk, inklusive svenska, tyska och franska. Användaren kan välja önskat språk att öva på.
- Inläsning från fil: Programmet kan läsa in glosor från filer som användaren anger.
- Statistik: Programmet håller koll på antalet rätta och felaktiga översättningar och visar en sammanfattning i slutet av övningen.
- Felhantering: Programmet kan hantera felaktig input och varna användaren om ogiltiga tecken eller ord.

## Användning

1. Starta programmet genom att köra huvudfilen (t.ex. `glosovning.py`).
2. Välj det språk du vill öva på genom att ange det som instrueras.
3. Ange språk (Engelska, E, eng / Tyska, T, tys / Franska, F, fra).
4. Följ anvisningarna på skärmen för att öva på översättningarna. Ange översättningen för varje ord.
5. Programmet ger feedback och räknar resultatet. Du kan avsluta när som helst genom att skriva "Q".

## Exempelfiler

Projektet innehåller några exempelfiler med glosor:

- `glos_eng.txt`: Engelska glosor
- `glos_tysk.txt`: Tyska glosor
- `glos_fransk.txt`: Franska glosor

Använd dessa filer som exempel eller skapa dina egna glosfiler enligt samma format.

## Felhantering

Programmet har inbyggd felhantering för ogiltig input. Om användaren anger ogiltiga tecken eller felaktiga filnamn kommer programmet att ge en lämplig varning.

## Licens

Det här projektet är licensierat under [MIT-licensen](LICENSE).

---
