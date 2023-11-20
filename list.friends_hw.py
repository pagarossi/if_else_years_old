from os import system
system ('clear')

me_and_friend = {'Dorin', 'Radj'}
my_friends = {'Marry', 'Jane', 'Alex', 'Jessica', 'Tom'}
friends_of_a_friend = {'Oliver', 'Mia', 'Pete'}

people_exclude = {'Oliver', 'Marry'}

trip_set = me_and_friend.union (
    my_friends,
    friends_of_a_friend
)

trip_set = trip_set.difference (people_exclude)

official_list = list(trip_set)

number_of_person = len(official_list)

print ('\nList of people who will definitely:\n')
for i in range(number_of_person):
    print(str(i + 1), '. ', official_list[i])


