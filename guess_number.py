import random 

s = random.randrange(1,50)
print(s)
guessed = False
while(guessed == False):
    a = int(input("Guess: "))
    if (a==s):
        guessed = True
print("Correct!")
