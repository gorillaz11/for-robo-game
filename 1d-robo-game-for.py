from os import system
roboX=5
Length=10


print("\n")



##################### map
while True:
    system("clear")
    for x in range(1,Length+1):
        if x==roboX:
            print("R",end="  ")
        else:
            print(".",end="  ")

print("\n")

option=input(">>>>")



if option =="a" and roboX >1:
    roboX-=1
if option =="d":
    roboX+=1
if option == "x" :
    system("clear")
    print("Thank you for playing the game!")
    break