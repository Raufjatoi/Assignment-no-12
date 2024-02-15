# 6. Phonebook Organizer:
# Create a program that stores names and phone numbers in a dictionary. Offer options to 
# add, search, and update contacts.
c_dic = {}
while True:
    add = input('Add contact : ').lower()
    num = input('Enter the contact num : ')
    if add not in c_dic:
        c_dic[add] = [num]
        print('added sucessfuly')
    else:
        print('Unsucessful')
    b = input('Enter s to search contacts n u to update : ').lower()
    if b == 's':
        s = input('Enter contact : ')
        if s in c_dic:
            print("Its exists")
        else:
            print('Its not exist')
    elif b == 'u':
        print(c_dic)
        u = input('which contact u gonna update : ')
        uc = input('num : ')
        c_dic[u] = uc
        print(f"updated dic is {c_dic}")     
        a = input('Enter "" c "" to continue/start n "" q "" to quite : ').lower()
        if a == 'q':
            break
