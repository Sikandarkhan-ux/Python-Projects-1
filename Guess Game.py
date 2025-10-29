secret_word = "dog"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False


while guess != secret_word:
    if guess_count < guess_limit and not (out_of_guess) :
        guess = input("Guess a word: ")
        guess_count += 1
        if guess_count == guess_limit:
            print("out of gusses, YOU LOSE!")
else :
    out_of_guess = True
if guess == secret_word:
    print("You guessed the secret word!")
if guess != secret_word:
    print("Sorry, you didn't guess the secret word!")
