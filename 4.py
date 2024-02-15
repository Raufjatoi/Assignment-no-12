# 4. Movie Rating Tracker:
# Design a program that lets users rate movies on a scale from 1 to 5. Use a dictionary to store 
# movie titles and their average ratings.
dic = {}
c = input('eEnter q to quit and c to continue : ').lower()
while c != 'q':
 a = input('Enter movie title : ')
 b = int(input('Enter rating from 1 to 5 : '))
 dic[a] = b
 print(dic)
 c = input('eEnter q to quit and c to continue : ').lower()
