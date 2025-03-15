# Write a program that counts each of the vowels in a inputed string (a,i,u,o,e) 
List = ['a','i','u','o','e']
text = input('Please input a text:')
text = text.lower()
# input -> Hello world!
for i in List:
    print(f'{i}',text.count(i))