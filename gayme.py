import sys
sys.argv
from random import randint as bruh
cnt=0
f=int(sys.argv[1])
l=int(sys.argv[2])
print("Guessing Game")
print(f"You want the game to start from {f} and end at {l}")
num=bruh(f,l)
print("I'm thinking of a number :)")
while cnt==0:
    guess=int(input("What's your guess?"))
    if num==guess:
        cnt=1
        print("Nice guess!")
    else:
        cnt=0
        print("Hmm Try Again")
       
        

