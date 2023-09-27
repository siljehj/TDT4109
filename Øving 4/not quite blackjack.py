from random import *

your_score = 0
dealers_score = 0

#while True:
dealers_card_1 = randint(1, 11)
dealers_card_2 = randint(1, 11)
your_card_1 = randint(1, 11)
your_card_2 = randint(1, 11)

dealers_score = dealers_card_1 + dealers_card_2
your_score = your_card_1 + your_card_2

print("Dealers cards are", dealers_card_1, "and ?")
print("Your score is:", your_score)
ans = input("Do you want another card? (Y/N) ")
 

if your_score == 21:
    print("YOU WIN!!!!")

print(starting_card_1, starting_card_2)



#while summen <= 21:
    starting_card_1 = random_card("a")
    starting_card_2 = random_card("a")
    your_card = random_card("a")
    summen += your_card
    print("Dealers cards are", starting_card_1, "and ?\nYour score is:", your_card)
    ans = input("Do you want another card? (Y/N) ")
    if ans.lower() == "y" or ans.lower() == "n":
        your_card_2