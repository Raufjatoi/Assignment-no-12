# 2. Grade Calculator:
#  Create a program that asks the user for their scores in different subjects and calculates their 
# overall grade based on a grading scale stored in a dictionary.
dic = {'A': 90, 'B': 80, 'C': 70, 'D': 60 }
chem = int(input('Enter chemistry scores : '))
bio = int(input('Enter Biology scores : '))
math = int(input('Enter math scores : '))

total = chem + bio + math 
per = total/300.0 
gf = False
for key, value in dic.items():
    if per >= value / 100.0 :
     print(key)
     gf = True 
     break
if not gf :
   print('F')
print(f'your per is {per:.2%}')
print(dic)

