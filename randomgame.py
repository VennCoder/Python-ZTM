import sys
sys.argv
from random import randint as bruh
cnt=0
print("Guessing Game")
f=int(input("You want the game to start from:"))
l=int(input("And end at:"))
num=bruh(f,l)
print("I'm thinking of a number :)")
while cnt==0:
    guess=int(input("What's your guess?"))
    if num==guess:
        cnt=0
        print("Hmm Try Again")
    else:
        cnt=1
        print("Nice guess!")
        
