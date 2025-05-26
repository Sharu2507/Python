import random
num=random.randint(1,6)
attempt=3
print("LET'S PLAY A GAME!")
print("CAN YOU GUESS THE NUMBER I AM THINKING?")
print("LET'S SEE.....")
print("GAME START")
guess=int(input("Enter a number:"))

while guess!=num and attempt!=0:
    attempt=attempt-1
    if guess>num:
        print("The number you guessed is greater than the number I am thinking.....")
        print("LET'S TRY AGAIN , YOU HAVE ",attempt,"ATTEMPTS LEFT")
        guess=int(input("Enter a number:"))
    else:
        print("The number you guessed is lesser than the number I am thinking.....")
        print("LET'S TRY AGAIN , YOU HAVE ",attempt,"ATTEMPTS LEFT")
        guess=int(input("Enter a number:"))
if attempt==0 and guess!=num:
    print("YOU HAVE 0 ATTEMPT LEFT and YOU LOST")
    print("BETTER LUCK NEXT TIME")
elif guess==num:
    print("WOW YOU WON THE GAME.......")
        
