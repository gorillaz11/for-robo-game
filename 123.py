roboX=5
Length=10
roboHP=100
bombX=7
bombX2=9
roboBT=100
roboHeart=3
roboMoney=0
roboC=2

option=""

print("\n")



##################### map
while True:
    
    for x in range(1,Length+1):
        if x==roboX:
            print("R",end="  ")
        elif x==bombX:
            print("B",end="")
        elif x==bombX2:
            print("B",end="")
        elif x==roboHeart:
            print("H",end="")
        elif x==roboC:
            print("C",end="")
        else:
            print(".",end="  ")

    print("\nHP",roboHP)
    print("BT",roboBT,"%")
    print("Money:",roboMoney,"$")
############################ read input
    option=input(">>>>")



    if option =="a" and roboX >1:
        roboX-=1
        roboBT-=1
    if option =="d" and roboX <10:
        roboX+=1
        roboBT-=1
    if roboX==bombX and print("."):
        roboHP-=10
    if roboX==bombX2:
        roboHP-=10
    if roboX==roboHeart:
        roboHP+=10
    if roboX==roboC:
        roboMoney+=10


    
    if option == "x" :
        
        print("Thank you for playing the game!")
        break