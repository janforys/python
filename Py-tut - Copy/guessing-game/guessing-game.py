word_to_guess = "jakamakatakasaka"
guess = ""

while guess != word_to_guess:
    guess = input("Enter your guess: ")
    if guess == word_to_guess:
        print("You've guessed the secret word man!")
    else:
        print("not good")




