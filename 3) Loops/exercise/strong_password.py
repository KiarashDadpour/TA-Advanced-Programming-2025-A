# Check if the inputted password is strong
# length >= 8
# contains [a-z]
# contains [0-9]
# contains [A-Z]
# contains a special charachter (!,@,#)

password = input("Please input your password: ")

has_lower = False
has_upper = False
has_digit = False
has_special = False

for char in password:
    if char.islower():
        has_lower = True
    elif char.isupper():
        has_upper = True
    elif char.isdigit():
        has_digit = True
    elif char in "!@#":
        has_special = True

if has_lower and has_upper and has_digit and has_special and len(password)>=8:
    print("Strong password")
else:
    print("Please change your password")