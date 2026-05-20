'''
Probelm: Even/Odd Analyzer

1. Takes a number from the user
2. Checks whether the number is:
Even
Odd

3. Also checks:

if the number is positive
negative
or zero

'''

number = int(input("Enter a number: "))

#Even or Odd
if number % 2 == 0:
    print(number, "is Even")
            
else:
    print(number, "is Odd") 


    
# Positive, Negative or Zero
if number > 0:
    print(number, "is Positive")

elif number < 0:
    print(number, "is Negative")

else:
    print(f'{number} is Zero')

