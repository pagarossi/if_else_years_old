from os import system
system ('clear')

menu = int(input (
    'MENU:'
    '\n1. Add film'
    '\n2. Show list'
    '\n3. Remove film'
    '\n4. Clear list'
    '\n0. Exit'
    '\nSelect Number: '))
list_cinema = [
    'Pulp Fiction','The Green Mile','Taxi Driver','K-Pax', '3']


system ('clear')
print ('Namber of films: ', len(list_cinema))
print ('°°°°°°°°°°°°°°°°')
if menu == 1:
    list_cinema.append (input('Add film: '))
    system ('clear')
    for l in range (len(list_cinema)):
        print (list_cinema[l])
elif menu == 2:
    system ('clear')
    for l in range (len(list_cinema)):
        print ("    >",list_cinema[l])
elif menu == 3:
    list_cinema.remove (input ('Remove film: '))
    for l in range (len(list_cinema)):
        print (list_cinema[l])
elif menu == 4:
    system ('clear')
    list_cinema.clear()
    print ('\n\nThe list is empty:(\n\n')
elif menu == 0:
    system ('clear')
    quit 
    print ('\nGoodbye\n')
else:
    pass
