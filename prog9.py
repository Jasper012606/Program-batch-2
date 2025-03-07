# A program that prints all the numbers from 0 to 100 except the numbers ending in zero (0) or five(5)
for i in range(101):
    if i % 5 != 0:
        print(i)