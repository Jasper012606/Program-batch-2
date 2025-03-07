#A program that asks the user to enter 2 numbers and prints all the numbers between the two numbers
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
if num1 < num2:
    for i in range(num1+1, num2):
        print(i)
else:
    for i in range(num2+1, num1):
        print(i)