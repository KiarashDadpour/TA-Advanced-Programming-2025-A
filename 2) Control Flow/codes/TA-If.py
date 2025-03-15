a = 10
b = 20

if a > b:
    print("a is greater than b.")
if b > a:
    print("b is greater than a.")
if a == b:
    print("a and b are equal.")
    
#----------------------------------------------------#

a = 30
b = 30

if a > b:
    print("a is greater than b.")
elif a < b:
    print("b is greater than a.")
elif a == b:
    print("a and b are equal.")
    
#----------------------------------------------------#

a = 10
b = 20

if a > b:
    print("a is greater than b.")
elif a == b:
    print("a and b are equal.")
else:
    print("b is greater than a.")
    
#----------------------------------------------------#

x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('One')
else:
    print('More than one')
    
#----------------------------------------------------#

a = 10
print(a)
print(a == 20)
print(a != 20)
print(20 == 10)
print('salam' == 'hi')

#----------------------------------------------------#

a, b = 20, 10
if a > b: print("a is greater than b")

#----------------------------------------------------#

a, b = 330, 2
print("A") if a > b else print("B")

#----------------------------------------------------#

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  
#----------------------------------------------------#

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
  
#----------------------------------------------------#

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
if a <= b:
  print("a is NOT greater than b")
  
#----------------------------------------------------#

x = 22

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
else:
    print("Under ten")
    
#----------------------------------------------------#

a = 33
b = 200

if b > a:
  pass

#----------------------------------------------------#

a = 333
b = 332
print("A") if a > b else (print("=") if a == b else print("B"))

