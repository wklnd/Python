# Musikbot med Discord.py

Detta är en Discord-bot skriven i Python som används för att spela musik i röstkanaler. Den är byggd med hjälp av biblioteket Discord.py och använder youtube-dl för att söka och köa musik från olika onlinesidor. Det är en mångsidig och enkel att använda musikbot som du kan bjuda in till din server för att njuta av dina favoritlåtar med vänner.

## Krav

Innan du kör den här boten måste du se till att du har följande krav uppfyllda:

- Python 3.5+
- `discord.py`
- `pynacl`
- `youtube-dl`
- FFmpeg i din systems PATH eller så kan du placera FFmpeg.exe-binären i botens katalog (för Windows).

## Installation

1. Klon detta repo till din lokala dator eller server.
2. Installera de nödvändiga Python-paketen med `pip install -U discord.py pynacl youtube-dl`.
3. Se till att du har FFmpeg installerat på din dator eller placera FFmpeg.exe-binären i botens katalog (för Windows).

## Användning

1. Skapa en Discord-bot och hämta en token. Byt ut `'Token'` i koden med din bots token.

2. Kör boten genom att köra skriptet. Den kommer att logga in på din Discord-server och ansluta till en röstkanal.

3. Du kan använda olika kommandon för att styra boten.

## Kommandon

- `!join`: Ansluter till en röstkanal.
- `!summon`: Kallar boten till en viss röstkanal.
- `!leave` (eller `!disconnect`): Tömmer kön och lämnar röstkanalen.
- `!volume`: Ställer in volymen för spelaren.
- `!now` (eller `!current` eller `!playing`): Visar den aktuella låten.
- `!pause`: Pausar den aktuella låten.
- `!resume`: Återupptar en pausad låt.
- `!stop`: Stoppar spelningen och rensar kön.
- `!skip`: Rösta för att hoppa över en låt.
- `!queue`: Visar spellistan.
- `!shuffle`: Blandar spellistan.
- `!remove`: Tar bort en låt från kön.
- `!loop`: Loopar den aktuella låten.
- `!play`: Spelar en låt. Om ingen URL anges, söker den automatiskt från olika webbplatser.


## Anpassning

Du kan ytterligare anpassa botens beteende genom att modifiera Python-skriptet. Till exempel kan du ändra kommandoprefix, lägga till fler behörighetskontroller eller justera ljudinställningarna.

## Ansvarsfriskrivning

Denna bot är avsedd för utbildningssyften och personligt bruk. Se till att du har nödvändiga behörigheter att lägga till en bot på din Discord-server. Var medveten om Discords användarvillkor och följ dem när du använder denna bot.

## Tack

Denna bot är baserad på arbetet av Valentin B. och använder biblioteken `discord.py` och `youtube-dl`. Ett speciellt tack till utvecklarna och bidragsgivarna till dessa projekt.
