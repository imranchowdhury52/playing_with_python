'''
Write a program that:

1. Asks the user how many numbers they want to enter
2. Stores the numbers in a list
3. Calculates:
    - total sum
    - average
    - largest number
    - smallest number

'''

numbers = int(input("How many numbers? "))

num = []
i=1

while i <= numbers:
        inputed_number = int(input(f"Enter number {i}: "))
        num.append(inputed_number) 
        i+=1

print(num)

#sum
sum_num = sum(num)
print(f'Sum: {sum_num}')



