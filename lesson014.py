def display_phrase(answer, guesses):
    display = []
    for word in answer:
        if word in guesses:
            display.append(word)
        else:
            display.append("_" * len(word))
    return " ".join(display)

def guess_the_phrase(phrase):
    guessed_words = []
    attempts = 10
    print("Welcome to the Guess the Phrase Game!\n")
    print(" ".join(["_" * len(word) for word in phrase]))

    while attempts > 0:
        user_guess = input("Please enter one word: ")

        if user_guess in phrase and user_guess not in guessed_words:
            guessed_words.append(user_guess)
            print("Congratulations! You guessed a correct word.")
            print(display_phrase(phrase_to_guess, guessed_words))
        else:
            attempts -= 1
            print(f"Incorrect guess. Attempts left: {attempts}")
            print(display_phrase(phrase_to_guess, guessed_words))

        if len(guessed_words) == len(phrase_to_guess):
            print("CONGRATULATIONS!! You guessed the phrase!")
            break

        if attempts == 0:
            print("Sorry, you've run out of attempts. The correct phrase was:")
            print(" ".join(phrase))

# Main Program
phrase_to_guess = ["python", "programming", "is", "fun"]
guess_the_phrase(phrase_to_guess)