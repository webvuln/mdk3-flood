import os 

os.system('clear')

print("_______________")
print("|             |")
print("|  1 | random |")
print("|             |")
print("|  2 | list   |")
print("|             |")
print("|  3 | update |")
print("---------------")

T = input("1 or 2: ")

if T == "1":
    CARD = input("your wifi card that is in moniter mode: ")
    os.system('sudo mdk3 ' + CARD + ' b -s 99999')
    
if T == "2":
    CARD = input("your wifi card that is in moniter mode: ")
    list = input("where your list is: ")
    os.system('sudo mdk3 ' + CARD + ' b -a -v '+ list + ' -s 99999')
    
if T =="3":
    os.system('sudo apt update')
    os.system('sudo apt install mdk3')
