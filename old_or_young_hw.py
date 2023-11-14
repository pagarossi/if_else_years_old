from os import system
system('clear')
#°°°°°°°°°°°°°°°°°°°°°°°°

year_of_birth = int(input('What year were you born? >>> '))
years_total = 2023 - year_of_birth

#°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
if year_of_birth <= 1899 or year_of_birth >= 2023:
    print ('you were either not born or died')
elif years_total <= 3 and years_total > 0:
    print('you are', years_total,'years old')
    print ('you fall under the category: baby')
elif years_total <= 9 and years_total > 3:
    print ('you fall under the category: kid') 
    print('you are', years_total,'years old')
elif years_total <= 15 and years_total > 9:
    print('you are', years_total,'years old')
    print ('you fall under the category: teen') 
elif years_total <= 18 and years_total > 15:
    print('you are', years_total,'years old')
    print ('you fall under the category: young') 
elif years_total <= 50 and years_total > 19:
    print('you are', years_total,'years old')
    print ('you fall under the category: adult') 
elif years_total > 50:
    print('you are', years_total,'years old')
    print ('you fall under the category: old') 
else:
    pass