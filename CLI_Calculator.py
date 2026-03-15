import math

n1 = int(input("enter the first number to do operation: "))
n2 = int(input("enter the next number to do operation: "))

print("select the operator u want to perform:")
print("1. '+'")
print("2. '-'")
print("3. '*'")
print("4. '/'")

choice = int(input("enter your choice: "))

if choice == 1:
    print("Good to see you have selected Addition : '+' ")
    print("the Addition of", n1, "and", n2, "is :", n1 + n2)

elif choice == 2:
    print("Great move you have selected Subraction: '-' ")
    print("the Subraction of", n1, "and", n2, "is :", n1 - n2)

elif choice == 3:
    print("Amazing you have selected Multiplication: '*' ")
    print("the Multiplication of", n1, "and", n2, "is :", n1 * n2)

elif choice == 4:
    print("time to divide the ratio's you have selected Division: '/' ")
    print("the Division of", n1, "and", n2, "is :", n1 / n2)

else:
    print("invalid choice!")