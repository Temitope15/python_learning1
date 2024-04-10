from random import randint
guess = randint(1,10)
guessedNumber = int(input("Type in a random number between 1 and 10: "))
if guessedNumber == guess:
    print("Na agba you be! you got the correct number to be", guess)
else:
    print("oops! sorry chief! try again. you should have typed in", guess, "instead of", guessedNumber)