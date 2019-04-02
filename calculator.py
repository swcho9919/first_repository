from module import *

print(" Menu")
print("--------")
choice = int(input("""
1: add
2: sub
3: mul
4: div
5: stop
:"""))

num1 = int(input("num1: "))
num2 = int(input("num2: "))

a = Cal(num1,num2)

if choice == 1:
    print(a.add())
elif choice == 2:
    print(a.sub())
elif choice == 3:
    print(a.mul())
elif choice == 4:
    print(a.div())
elif choice == 5:
    print("stop")




