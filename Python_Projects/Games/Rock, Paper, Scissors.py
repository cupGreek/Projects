import random
rep='y'
while(rep=='y'):
    a=int(input("Best of what do you wanna play(Enter a odd number) "))
    if(a%2==0):
        print("enter a valid input")
    else:
        c=0
        p=0
        q=0
        while(q<a):
            r=random.randrange(0,3,1)
            g=int(input("\nChocie from 1.rock, 2.paper or 3.scissor "))
            g=g-1
            if(g<3 and g>=0):
                q=q+1
                b=["Rock","Paper","Scissors"]
                if(g==r):
                    print("It's a draw for this turn. The computer chose:",b[r])
                elif(g==0):
                    if(r==2):
                        print("You win this round. The computer chose:",b[r])
                        p=p+1
                    else:
                        print("You lost this game. The computer chose:",b[r])
                        c=c+1
                elif(g==1):
                    if(r==0):
                        print("You win this round. The computer chose:",b[r])
                        p=p+1
                    else:
                        print("You lost this game. The computer chose:",b[r])
                        c=c+1
                else:
                    if(r==1):
                        print("You win this round. The computer chose:",b[r])
                        p=p+1
                    else:
                        print("You lost this game. The computer chose:",b[r])
                        c=c+1
            else:
                print("Choose a valible input")
                print(q)
        print(" Score: Computer=",c," Player= ",p,"\n")
        if(c==p):
            rep=input("Its a draw, to play again press y ")
        elif(c>p):
            rep=input("The computer has won, Press y to take another shot ")
        else:
            rep=input("You won!!!! Press y to play another game ")
                
                                
            
