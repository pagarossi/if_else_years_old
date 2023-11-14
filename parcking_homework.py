from os import system

system ('clear')
PARKING_PLACES = 7
FREE_PLACE = 3

print("#"*PARKING_PLACES*5)

for place_index in range(1, PARKING_PLACES):
    if FREE_PLACE == place_index:
        print("|  |", end="")
    print("| X |", end="")

print("\n","#"*PARKING_PLACES*5, sep="")

####### sep от слова separetion (наверно), он что разделает, я попровбал убать и нижние хэштеги 
####### передвинулись вперед, значит в данном случаи он удаляет этот пробел 
