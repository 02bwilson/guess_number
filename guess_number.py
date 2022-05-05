import random 

s = random.randrange(1,50)
print(s)
guessed = False
while(guessed == False):
    try:
        guess = input("Guess: ")
        guessInt = int(guess)
        
    except Exception:
        print(f"Sorry, {guess} is not a number")
    if (guess==s):
        guessed = True
print("Correct!")
