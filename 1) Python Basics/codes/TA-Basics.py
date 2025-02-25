print("Hello, World!")
print("Welcome to class")
print("I am", 22, "years old.")

# -------------------------------------- #

print("Tehran", "Rasht", "Tabriz")
print("Tehran", "Rasht", "Tabriz", sep="-")
print("Tehran", "Rasht", "Tabriz", sep="-->")

print("Price: 15", end="$")

# -------------------------------------- #

name = "Amir"
age = 20
print("My name is", age, "I'm", age, "years old.")
print(f"My name is {name}. I'm {age} years old.")

language = "Python"
print(f"My favorite programming language is {language}.")

# -------------------------------------- #

pi = 3.14159265358
print(f"Pi: {pi:.2f}")

r = 5
area = pi * r * r
print(f"Area: {area}")
print(f"Area: {area:.4f}")
print(f"Area: {area:10.4f}")

# -------------------------------------- #

name = "Amir"
age = 20
height = 1.83
is_student = True

print(f"Name: {name} | type: {type(name)}")
print(f"Age: {age} | type: {type(age)}")
print(f"Height: {height} | type: {type(height)}")
print(f"Is_Student: {is_student} | type: {type(is_student)}")

# -------------------------------------- #

name = input()
print(f"Welcome {name}")

name = input("PLease enter your name: ")
print(f"Welcome {name}")

# -------------------------------------- #

name = input("Please enter your name: ")
age = int(input(f"Please enter your age: "))
gpa = float(input("PLease enter your gpa: "))

print(f"Welcome {name}")
print(f"You are {age} years old.")
print(f"Your gpa is {gpa}.")

print(f"Welcome {name} \nYou are {age} years old.\nYour gpa is {gpa}.")
print(f"{name} \t{age}")

# -------------------------------------- #

# Swapping 2 Variables
a = int(input("A: "))
b = float(input("B: "))
a, b = b, a
print(f"After Swapping:\n \t A = {a} \n \t B = {b}")

# -------------------------------------- #

# Repeat the String
word = input("Enter a word: ")
times = int(input("How many times tp repeat? "))
print(f"{word * times}")


# -------------------------------------- #

# Convert Fahrenheit to Celsius

temp = float(input("Please enter the temp in F: "))
C = (temp - 32) * 5/9
print(f"{temp} F is {C:.4f} C")

# -------------------------------------- #

file = open("data.txt", "w")
file.write("Hello, World!")
file.close()

# -------------------------------------- #

file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# -------------------------------------- #

file = open("data.txt", "a")
file.write("\nThis is a new line added!")
file.close()

# -------------------------------------- #

with open("file.txt", "w") as file:
    file.write("Data Science")
    
