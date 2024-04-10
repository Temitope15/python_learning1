weight = int(input('Enter your weight in kg: '))
height = float(input('Enter your height in metres: '))
calc_bmi = weight / (height ** 2)
print(f'Your Body mass index is {int(calc_bmi)}')