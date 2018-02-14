#the game start
coins=21
player=1
L=[1,2,3]
while True :
    while coins>0:
        if player==1:
            P1=int(input("Put your coins1:"))
            if P1 in L :
                coins=coins-P1
                print(coins)
            else:
                print("The coins isnot right")
                break
            if coins==1 :
                print("P2 is loser")
                print("P1 is winer")
            player=2
            if coins ==0 :
                print ("Game over")
                break
        if player==2:
                P2=int(input("Put your coin2:"))
                if P2 in L:
                    coins=coins-P2
                    print(coins)
                else:
                    print("The coins isnot right")
                if coins==1:
                    print("P1 is loser")
                    print("P2 is winer")
                player=1
                if coins ==0 :
                     print ("Game over")
             
#the game end 
