from random import randint

guessed_num = int(input("Guess any number between 1 and 10:  "))
num = randint(1, 10)
if guessed_num == num:
    print("Na agba you be! you guessed", num, "correctly!")
else:
    print("oops! try again")
