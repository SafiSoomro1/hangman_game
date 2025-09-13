# Hangman game
# add a random amount of words and assign one randomly
# make it so that it shows "_" and if a person guesses a word inside that word replace the underscore with the word
# Also add hints about category and the first and last letters of the words
import random

words = (
    "Apple", "Chair", "House", "Water",
    "Jungle", "Castle", "Mirror", "Rocket",
    "Pirate", "Whisper", "Pizza",
    "Galaxy", "Cryptic", "Pharaoh", "Zephyr",
)



def category(word):
    if word.lower() in ["apple", "pizza"]:
        return "Category: 🍏 Food and drinks!"
    if word.lower() in ["chair", "mirror", "house", "water"]:
        return "Category: 🥦 Everyday Objects!"
    if word.lower() in ["jungle", "castle"]:
        return "Category: 🌍 Places"
    if word.lower() in ["rocket", "galaxy"]:
        return "Category: 🚀 Transportation & Space"
    if word.lower() in ["pirate", "pharaoh"]:
        return "Category: 🏴‍☠️  People & Characters"
    if word.lower() in ["zephyr", "whisper"]:
        return "Category: 💨 Nature & Elements"
    if word.lower() in ["cryptic"]:
        return "Category: 🧩 Mysterious & Abstract"
    else:
        return "Category: Unknown!"


def first_last(name):
    return f"First Letter: {name[0]} Last Letter: {name[-1]}"

def playgame():
        random_word = (random.choice(words)).lower()
        hint_asks = 0
        hint_used = False
        already_guessed = []
        attempts = 6
        centered_word = ["_"] * len(random_word)
        print("-----| You have been assigned a word |-----\n")
        print(" ".join(["_"] * len(random_word)).center(41))
        print(f"\n            Length of word: {len(random_word)}\n")
        print("\n-------------| Guess Here! |-------------\n")
        guess = input("Enter a word: ").lower()
        print(guess)
        while attempts > 0:
            if len(guess) > 1:
                print("Can't enter more than one word!\n")
                guess = input("Enter a word: ").lower()
            if guess == "":
                print("Please enter a word!")
                guess = input("Enter a word: ").lower()
            if not guess:
                print("Please enter a letter")
                continue

            elif guess not in random_word:
                attempts -= 1
                print(f"Woosh! Wrong! You have {attempts} attempts left.")
                if attempts == 0:
                    print(f"😢 You lost! The word was \"{random_word}\"")
                    break

                if not hint_used:
                    if hint_asks < 2:
                        hint = input("Would you like to take a hint!? [costs an attempt]: ").lower()
                        hint_asks += 1
                        if hint == "y" or hint == "yes":
                            attempts -= 1
                            print(f"You have {attempts} attempts left!")
                            print(first_last(random_word), category(random_word))
                            hint_used = True
                        else:
                            print(f"No hint taken! You have {attempts} attempts left!")

            if guess in random_word:
                if guess not in already_guessed:
                    for pos in range(len(random_word)):
                        if random_word[pos] == guess:
                            centered_word[pos] = guess
                            already_guessed.append(guess)
                    print(f"Correct {guess} is in random word!")
                else:
                    print(f"You've already guessed \"{guess}\" ")

            if "_" in centered_word:
                print(" ".join(centered_word))
                guess = input("Enter a word: ").lower()
            else:
                print(f"🎉 Congratulations! You won \"{random_word}\" was the secret word!")
                break



def main():
    while True:
        playgame()
        continuegame = input("Do you want to play Y/N: ").lower()
        if continuegame not in ("y", "yes"):
            print("Bye Bye!")
            break



if __name__ == "__main__":
    main()

