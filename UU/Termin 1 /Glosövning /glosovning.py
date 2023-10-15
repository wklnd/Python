import random

class VocabularyGame:
    def __init__(self, language):
        self.language = language
        self.vocabulary = self.load_vocabulary()
        self.attempts = 0
        self.correct_attempts = 0

    def load_vocabulary(self):
        file_name = {
            "eng": "glos_eng.txt",
            "tys": "glos_tysk.txt",
            "fra": "glos_fransk.txt"
        }
        vocabulary = {}
        try:
            with open(file_name[self.language], "r") as file:
                for line in file:
                    swedish, translation = line.strip().split(",")
                    vocabulary[swedish] = translation
        except FileNotFoundError:
            print("Kunde inte hitta filen.")
        return vocabulary

    def start(self):
        if not self.vocabulary:
            return

        print(f"Välkommen till Svenska-{self.language.capitalize()} Glosövning!")

        while self.attempts < 10:
            swedish_word, translation = random.choice(list(self.vocabulary.items()))
            user_translation = input(f"Vad är översättningen av '{swedish_word}'? (Q för att avsluta): ")

            if user_translation == "Q":
                break

            self.check_translation(swedish_word, translation, user_translation)

        self.show_statistics()

    def check_translation(self, swedish_word, translation, user_translation):
        self.attempts += 1
        user_translation = user_translation.lower()

        if user_translation == translation:
            print("Rätt!")
            self.correct_attempts += 1
        else:
            similarity = self.calculate_similarity(translation, user_translation)
            if similarity >= 0.5:
                print(f"Nästan rätt! ({translation})")
            else:
                print(f"Fel! ({translation})")

    def calculate_similarity(self, word1, word2):
        common_letters = set(word1) & set(word2)
        return len(common_letters) / max(len(word1), len(word2))

    def show_statistics(self):
        print(f"\nAvslutat spelet efter {self.attempts} ord.")
        print(f"Antal rätta svar: {self.correct_attempts}/{self.attempts}")

if __name__ == "__main__":
    language = input("Välj ett språk (Engelska, E, eng / Tyska, T, tys / Franska, F, fra): ").strip().lower()
    if language in ["engelska", "e", "eng"]:
        language = "eng"
    elif language in ["tyska", "t", "tys"]:
        language = "tys"
    elif language in ["franska", "f", "fra"]:
        language = "fra"
    else:
        print("Ogiltigt val. Avslutar programmet.")
        exit()

    game = VocabularyGame(language)
    game.start()
