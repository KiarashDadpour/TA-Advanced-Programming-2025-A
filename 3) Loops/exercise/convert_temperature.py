# Convert celsius to farenhait and reverse
# F = (C * (9/5)) + 32
# C = (F - 32)* (5/9)
# example -> 0 C = 32 F

temp = float(input('Please input the value of the temprature: '))
unit = input('Please input the unit: (C,F)')

# You could input like this too:
# temp, unit = (input('Please input the value of the temprature and then the unit with a space between: (32 F) ')).split(' ')
# temp = float(temp)

Flag = True
if unit.lower() == 'c':
    final = (temp * (9/5)) + 32
elif unit.lower() == 'f':
    final = (temp - 32)* (5/9)
else:
    print('Invalid unit')
    Flag = False

if Flag:
    print(round(final,2))