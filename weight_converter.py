weight = float(input('Enter weight in kg: '))
unit = input('Enter unit to convert to (g, lb): ')
if unit.lower() == 'g':
    converted_weight = weight * 1000
    print(f'{weight} kg is equal to {converted_weight} g')
elif unit.lower() == 'lb':
    converted_weight = weight * 2.20462
    print(f'{weight} kg is equal to {converted_weight} lb') 
else:
    print('Invalid unit. Please enter "g" for grams or "lb" for pounds.')