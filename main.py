import random


def create_secret_word():
    rand_int = random.randint(0, 212)

    file_words = open("Words", "r")
    words_list = file_words.readlines()

    created_word = words_list[rand_int]
    return created_word


onscreen_word = ""
onscreen_word_after = ""
secret_word = create_secret_word()[:-1]

lives = 5

open("Guesses", "w").close()

while onscreen_word != secret_word and lives != 0:
    onscreen_word_after = onscreen_word

    onscreen_word = ""

    file_guesses = open("Guesses", "a")
    file_guesses.write(input("Enter guess: "))
    file_guesses.close()

    file_guesses = open("Guesses", "r")
    guesses = file_guesses.readlines()

    for letter in secret_word:
        for guess in guesses:
            if letter in guess:
                onscreen_word += letter

            else:
                onscreen_word += "_"

    if onscreen_word == onscreen_word_after:
        lives -= 1

    print(onscreen_word + "          Lives: " + str(lives))

if onscreen_word == secret_word:
    print("\nYou Win!")

if lives == 0:
    print("\nYou Lose!")
    print("The Word was: " + secret_word)
