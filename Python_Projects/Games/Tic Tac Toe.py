import random

def matprint(f):
    for i in range(3):
        for j in range(3):
            print(f[i][j],end='\t')
        print()

def checkmat(f):
    if (f[0][0]==f[1][1] and f[1][1]==f[2][2]) or (f[2][0]==f[1][1] and f[1][1]==f[0][2]):
        print("Diagnols")
        return f[1][1]
    else:
        for i in range(3):
            if(f[i][0]==f[i][1] and f[i][0]==f[i][2]):
                print("Rows",i)
                return f[i][0]
            else:
                if(f[0][i]==f[1][i] and f[0][i]==f[2][i]):
                    print("Columns",i)
                    return f[0][i]
 
    return ""

rep="y"
while(rep=="y"):
    n=int(input("Choose the mode you wish to play\n\t1.)1 Player\n\t2.)2 Player"))
    f=[["_" for i in range(3)]for j in range(3)]
    matprint(f)
    if(n==1):
        x=input("Choose between X and O")
        if x=="X":
            o="O"
        if x=="O":
            o="X"
        for i in range(9):
            g=0
            print(i)
            while(g==0):
                if(i%2==0):
                    print("Player's Turn")
                    a=int(input("Row: "))
                    p=int(input("Column= "))
                    if a>2 or p>2 or f[a][p]!="_":
                        print("enter a valid index")
                    else:
                        f[a][p]=x
                        g=1
                else:
                    a=random.randrange(0,3,1)
                    p=random.randrange(0,3,1)
                    if a>2 or p>2 or f[a][p]!="_":
                        pass
                    else:
                        f[a][p]=o

                        g=1
            matprint(f)            
            if(i>4):
                q=checkmat(f)
                print(q)
                if q==x:
                    print("Player Wins")
                    rep=input("Wanna try again, Press y")
                    break
                elif q=="":
                    print("Draw")
                    rep=input("Wanna try again, Press y")
                else:
                    if q==o:
                        print("Computer Wins")
                        rep=input("Wanna try again, Press y")
                        break
    if(n==2):
        print("Player 1 is X and Player 2 is O")
        for i in range(9):
            g=0
            while(g==0):
                if(i%2==0):
                    print("Player 1's Turn")
                    a=int(input("Row: "))
                    p=int(input("Column= "))
                    if a>2 or p>2 or f[a][p]!="_":
                        print("enter a valid index")
                    else:
                        f[a][p]="X"
                        g=1
                else:
                    print("Player 2's Turn")
                    a=int(input("Row: "))
                    p=int(input("Column= "))
                    if a>2 or p>2 or f[a][p]!="_":
                        print("enter a valid index")
                    else:
                        f[a][p]="O"
                        g=1
            matprint(f)
            if(i>4):
                q=checkmat(f)
                print(q)
                if q=="X":
                    print("Player 1 Wins")
                    rep=input("Wanna try again, Press y")
                    break
                elif q=="":
                    print("Draw")
                    rep=input("Wanna try again, Press y")
                else:
                    if q=="O":
                        print("Player 2 Wins")
                        rep=input("Wanna try again, Press y")
                        break
       

    
