# Write a program that counts the vowels in a inputed string (a,i,u,o,e)
List = ['a','i','u','o','e']
text = input('Please input a text:')
# input -> Hello world!
counter = 0
for i in text.lower():
    if i in List:
        counter += 1
print(counter)