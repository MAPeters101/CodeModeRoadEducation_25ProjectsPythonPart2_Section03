# This function is used to display the state of the phrase (Including
# correctly guessed words, and words not guessed yet - which are replace
# with '_')
# Complete the missing parts of the function

def display_phrase(answer, guesses):
    display = []
    for word in answer:
        if word in guesses:
        # Append word to the 'display' list
            display.append(word)
        else:
        # Append the following to the 'display' list: "_" * len(word)
            display.append("_" * len(word))
    return " ".join(display)


def guess_the_phrase(phrase):
    # Create an empty list to store the guessed words
    guessed_words = []

    # Set the amount of incorrects that the player gets
    incorrects = 5

    print("Welcome to the Guess the Phrase Game!\n")

    # This code prints underlines based on the length of each word in list
    print(" ".join(["_" * len(word) for word in phrase]))

    while incorrects > 0:
        # Ask the user for ONE word (their guess)
        user_guess = input("Please enter one word: ")

        if user_guess in phrase and user_guess not in guessed_words:
            # Append user guess to the 'guessed_words' list
            guessed_words.append(user_guess)
            print("Congratulations! You guessed a correct word.")
            print(display_phrase(phrase_to_guess, guessed_words))  # Inside, call the display_phrase function
        else:
            # Decrement their incorrects by 1
            incorrects -= 1
            print(f"Incorrect guess. Incorrects left: {incorrects}")
            print(display_phrase(phrase_to_guess, guessed_words))  # Inside, call the display_phrase function

        # Check if the length of 'guessed_words' equals length of 'phrase'
        # If so, congratulate the user AND break from the loop
        if len(guessed_words) == len(phrase_to_guess):
            print("CONGRATULATIONS!! You guessed the phrase!")
            break

        if incorrects == 0:
            print("Sorry, you've run out of attempts. The correct phrase was:")
            print(" ".join(phrase))


# Main Program
phrase_to_guess = ["I", "am", "really", "enjoying", "learning", "to", "program", "in", "python"]  # Add a bunch of random words that form a sentence
guess_the_phrase(phrase_to_guess)