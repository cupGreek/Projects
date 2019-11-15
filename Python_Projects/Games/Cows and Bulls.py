import random
print("Welcome to the game of cows and bulls. \nThe rules are simple: \n\tYou have to guess a number with no.of.digits of your own choice. The numbers in their respective digit value is counted as a bull \n\tand a number which occupies a wrong face value is counted as a cow. You can choose to the exit the game anytime you feel like giving up. \n\tThe answer will be displayed once you quit. All the best.")
d=int(input("\nChoose your difficulty level here: \n\t Enter the number of digits, the more the number of digits more interesting the game would be "))
r=str(random.randrange((10**(d-1)),10**d,1))
rep='y'
while(rep=='y'):
    b=c=0
    a=[]
    f=[]
    g=input("Enter your guess")
    if(len(g)!=d or g[0]=='0'):
        print("Enter a ",d," digit number")

    else:
        for i in range(d):
            for j in range(d):
                if(r[i]==g[j]) and not(i in a) and not(j in f):
                    if(i==j):
                        b=b+1
                        a.append(i)
                        f.append(j)
        for i in range(d):
            for j in range(d):
                if(r[i]==g[j]) and not(i in a) and not(j in f):
                        c=c+1
                        a.append(i)
                        f.append(j)
                   
            
        if(b==d):
            print("Your answer is correct")
            break
        
        else:
            print("Bulls= ",b,"Cows= ",c)
            rep=input("Press \"y\" to try again")
else:
    print("the answer is",r)
        
