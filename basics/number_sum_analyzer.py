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

number_list = []
i=1

while i <= numbers:
        entered_number = int(input(f"Enter number {i}: "))
        number_list.append(entered_number) 
        i+=1

print(f'Numbers: {number_list}\n')

#sum
sum_num = sum(number_list)
print(f'Sum: {sum_num}')

#average
avg_num = sum_num / len(number_list)
print(f'Average: {avg_num}')

#largest number
largest_num = max(number_list)
print(f'Largest: {largest_num}')

#Smallest number
smallest_num = min(number_list)
print(f'Smallest: {smallest_num}')

