# Task 4
def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        display = ""
        for char in secret_word:
            if char in guesses:
                display += char
            else:
                display += "_"

        print(display)

        return all(char in guesses for char in secret_word)

    return hangman_closure


if __name__ == "__main__":
    secret_word = input("Enter the secret word: ").lower()
    game = make_hangman(secret_word)

    print("\nStart guessing letters!")

    while True:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1:
            print("Please enter only one letter.")
            continue

        finished = game(guess)

        if finished:
            print("You guessed the word!")
            break