# 7. Restaurant Menu Parser:
# Write a program that reads a restaurant menu file (text or CSV) and stores items, prices, and 
# categories in a dictionary. Allow users to browse by category or search for specific items.
items = ["burger","Pizza","icecream"]
price = [200,170,190]
cat = ["fast food","italian fast food",'sweet']
l = []
for i in range(len(items)):
    m = {'items' : items[i], 'price': price[i], 'catgory': cat[i]}
    l.append(m)
for i in range(len(items)):
 print(l[i]['catgory'],end='| ') 
print()
search = input('Enter category from above for details : ').lower()
if search == 'fast food':
   print(l[0])
elif search == 'italian fast food':
   print(l[1])
elif search == 'sweet':
   print(l[2])
else:
   print('invalid input ')


