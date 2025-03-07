# A program that asks user to input 10 numbers and prints the number of even numbers
print(sum(int(input("Enter a number: ")) % 2 == 0 for i in range(10)))