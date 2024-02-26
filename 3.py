# 3. Shopping List Manager:
#  Develop a program that allows users to add, remove, and check off items on a shopping list 
# stored in a dictionary.
dic = {}
while True :
 def add (i,v):
    if i not in dic :
        dic[i] = int(v)        
 def remove (i):
    if i in dic :
        del dic[i] 
 def check (i,g):
    if i in dic:
        dic[i] -= int(g)
 def view ():
    for key,value in dic.items():
        print(f'{key}: {value}')
 print('Enter choice : \n 1 : Add  \n 2 : remove \n 3 : check \n 4 : view ')
 c = int(input("enter choice : "))
 if c == 1 :
    i = input('Enter item : ')
    v = input('Enter val : ')
    add(i,v)
 elif c == 2 :
    i = input('Enter the item u wanna remove : ')
    remove(i)
 elif c == 3 :
    i = input('Enter wha ya wanna remove  : ')
    v = int(input('How many : '))
    check(i,v)
 elif c == 4 : 
    view()
 elif i == 0:
    print('Thank u for using :::: ')
    break
 else:
    print('Invalid ')
     



    