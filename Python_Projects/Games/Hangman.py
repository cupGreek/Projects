import random

def game(b):
    i=random.randrange(0,len(b),1)
    l=["_" for j in range(len(b[i][0]))]
    print("The word of the game is ")
    for j in range(len(b[i][0])):
       print(l[j],end=" ")
    print("And your clue is: ",b[i][1])
    c=["H","a","n","g","m","a","n"]
    while "n" in c:
        d=input("Enter your guess")
        if(d not in b[i][0]):
            c.pop(0)
        else:
            x=0
            for z in range(0,len(b[i][0])):
                if(b[i][0][z]==d):
                    l[z]=d
                    print(l)
                    if(b[i][0].count(d)==x):
                        print("HI")
                        break
        print("And your left over chances are ",c, "And you have found: ")
        for j in range(len(b[i][0])):
           print(l[j],end=" ")
        if "_" not in l:
            print("You have won")
            break
    else:
        print("You have lost.")
    rep=input("Wanna play another game??,Press y")
    
f=[["apple","This fell on Einstein"],[ "orange","The name of the fruit is same as its colour"],["pineapple","One of the largest yellow coloured fruit"]]
p=[["everest","The highest peak"],["kailash","It is said to be the place where lord shive resides"], ["fuji","The four lettered peak"]]
rep="y"
while(rep=="y"):
    a=int(input("welcome to the game of hangman. Choose between 1.Fruits or 2.Mountain Peaks"))
    if a==1:
        game(f)
    elif a==2:
        game(p)
    else:
        print("enter a valid number")
