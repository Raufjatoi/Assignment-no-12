# 3. Shopping List Manager:
#  Develop a program that allows users to add, remove, and check off items on a shopping list 
# stored in a dictionary.
items = {'apple': 10, 'banana': 14, 'orange': 8}
print(items)

user = input('Enter "a" to add and "r" to remove: ').lower()

if user == 'r':
    r = input('Which item do you want to remove: ').lower()
    if r in items:
        del items[r]
        print(f'{r.capitalize()} removed. Updated items: {items}')
    else:
        print(f'{r} not found.')
    
elif user == 'a':
    a = input('What do you want to add: ')
    q = int(input('Enter quantity: '))
    items[a] = q
    print(f'{q} {a.capitalize()}(s) added. Updated items: {items}')
