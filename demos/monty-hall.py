import random

total_num_of_outcomes = 1000
to_change = True #True if user changes his/her choice, False otherwise

def perform_one_outcome():
    car_position = random.randint(1, 3)
    user_choice = random.randint(1, 3)

    doors_of_the_host = [1, 2, 3]
    doors_of_the_host.remove(car_position)
    if car_position != user_choice:
        doors_of_the_host.remove(user_choice)

    if len(doors_of_the_host) == 2:
        doors_of_the_host.pop(random.randint(0, 1))
    opened_door_by_host = doors_of_the_host[0]

    if to_change:
        doors_of_the_user = [1, 2, 3]
        doors_of_the_user.remove(user_choice)
        doors_of_the_user.remove(opened_door_by_host)
        user_choice = doors_of_the_user[0]
    return car_position == user_choice

favourables = 0
for i in range(total_num_of_outcomes):
  if perform_one_outcome():
  	favourables += 1
 
print('Percentage of favourable is: ', (100.0 * favourables) / total_num_of_outcomes)

