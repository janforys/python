import random

print("Elo ziaaaa! This is lottery game :-) \nRemember to type numbers between 1 and 25!")

play = "y"

given_numbers = []
random_numbers = []

while play == "y":
    for i in range(3):
        given_numbers.append(int(input("Give number "+str(i+1)+": ")))
        random_numbers.append(random.randint(1,25))
    coherent_numbers = 0
    for z in given_numbers:
        for j in random_numbers:
            if z == j:
                coherent_numbers = coherent_numbers + 1

    print("Your result is: "+str(coherent_numbers))
    print("Random numbers:")
    for i in random_numbers:
        print(i)
        
    given_numbers.clear()
    random_numbers.clear()
    
    play = input("Do u want to play again? (y) ")

