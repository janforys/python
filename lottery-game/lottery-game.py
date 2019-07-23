import random

print("Elo ziaaaa! This is lottery game :-) \nRemember to type numbers between 1 and 50!")

play = "yes"

given_numbers = []
random_numbers = []

while play == "yes":
    for i in range(6):
        given_numbers.append(int(input("Give number "+str(i+1)+": ")))
        random_numbers.append(random.randint(1,50))
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
    
    play = input("Do u want to play again? (yes) ")

