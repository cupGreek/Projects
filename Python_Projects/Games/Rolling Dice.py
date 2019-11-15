import random
print("Welcome.\nHere are the rules:\n\tIf you get 7 in your first roll you save your bet, you neither lose nor win anything\n\tIf you get 11 in your first roll you get twice your bet back\n\tIf you get 2,3 or 12 in your first roll you lose all your bet\n\t  and for anything else, things get interesting.\n\t\tYour roll is set as your target. You gotta get that again without getting any 7 in between and within three rolls, failing to do which you lose your bets.\n\t\tIf you do manage to get your target, your profit depends on the your target and on which roll your target was rolled a second time, according to the pay table below:")
print("\n\t\t\tRoll\t4,10\t5,9\t6,8\t\t\t\n\t\t\t   1\t5-1\t4-1\t3-1\n\t\t\t   2\t4-1\t3-1\t2-1\n\t\t\t   3\t3-1\t2-1\t1\n")
rep=input("Press y and lets begin ")
while(rep=='y'):
    point=0
    n=random.randrange(1,7,1)+random.randrange(1,7,1)
    print("Your set the point roll is",n)
    if(n==11):
       print("Congrats You have won twice your bet.")
    elif(n==12 or n==2 or n==3):
       print("You just lost all your money in a gamble, Be careful next time.")
    elif(n==7):
        print("You just saved your money. But you didnt win anything.")
    else:
        for i in range(3):
            b=random.randrange(1,7,1)+random.randrange(1,7,1)
            print("Your roll is ",b)
            if(b==7):
                print("All your bet is ours now.")
                break
            if(b==n):
                if(b in(4,10)):
                    point=random.randrange(1,6-i,1)
                    print("Congrats. You have won ",point," times your bet")
                    break
                if(b in (5,9)):
                    point=random.randrange(1,5-i,1)
                    print("Congrats. You have won ",point," times your bet")
                    break
                if(b in (6,8)):
                    point=random.randrange(1,4-i,1)
                    print("Congrats. You have won ",point," times your bet")
                    break
        else:
            print("You tried your luck, but lost.")
    rep=input("Wanna play again? Press y ")

