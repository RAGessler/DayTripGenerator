import random
import resources

#random value picker from list
def pick_from_list(list):
    list_items = len(list) - 1
    number_from_list = random.randint(0, list_items)
    picked_string = list[number_from_list]
    return picked_string

#destination picker
def destination_picker():
    picked_destination = pick_from_list(resources.destinations)
    sentance_structure = 'take a trip to'
    y_or_n = user_confirmation(sentance_structure, picked_destination)
    if y_or_n == 'N' or y_or_n == 'n':
        picked_destination = destination_picker()
    return picked_destination

#trasportation picker
def transportation_picker(location):
    if location == 'Honolulu, HI':
        picked_transportation = pick_from_list(resources.overseas_transportation)
    else:
        picked_transportation = pick_from_list(resources.transportation_list)
    sentance_structure = 'travel via'
    y_or_n = user_confirmation(sentance_structure, picked_transportation)
    if y_or_n == 'n' or y_or_n == 'N':
        picked_transportation = transportation_picker(location)
    return picked_transportation

#entertainment picker
def entertainment_picker(location):
    if location == 'Washington, D.C':
        picked_entertainment = pick_from_list(resources.washington_entertainment)
    elif location == 'New York City, NY':
        picked_entertainment = pick_from_list(resources.nyc_entertainment)
    elif location == 'Honolulu, HI':
        picked_entertainment = pick_from_list(resources.honolulu_entertainment)
    elif location == 'San Antonio, TX':
        picked_entertainment = pick_from_list(resources.san_antonio_entertainment)
    sentance_structure = 'enjoy a day at'
    y_or_n = user_confirmation(sentance_structure, picked_entertainment)
    if y_or_n == 'n' or y_or_n == 'N':
        picked_entertainment = entertainment_picker(location)
    return picked_entertainment

#restaurant picker
def restaurant_picker(location):
    if location == 'Washington, D.C':
        picked_restaurant = pick_from_list(resources.washington_restaurants)
    elif location == 'New York City, NY':
        picked_restaurant = pick_from_list(resources.nyc_restaurants)
    elif location == 'Honolulu, HI':
        picked_restaurant = pick_from_list(resources.honolulu_restaurants)
    elif location == 'San Antonio, TX':
        picked_restaurant = pick_from_list(resources.san_antonio_restaurants)
    sentance_structure = "eat dinner at"
    y_or_n = user_confirmation(sentance_structure, picked_restaurant)
    if y_or_n == 'n' or y_or_n == 'N':
        picked_restaurant = restaurant_picker(location)
    return picked_restaurant

#user confimation routine
def user_confirmation(sentance_structure, location):
    user_confirm = input(f'I have decided that you will {sentance_structure} {location}.  Is this okay? Y/N')
    return user_confirm

#final confirmation
def final_confirmation(destination, transportation, entertainment, restaurant):
 print(f'I have decided that you will take a trip to {destination} via a {transportation}.  You will spend the day at {entertainment} and will eat diner at {restaurant}.')
 final_result = input('Please confirm that you are happy with the result of my selections.  Y/N')
 if final_result == 'n' or final_result == "N":
     print('Restarting...')
     destination = destination_picker()
     transportation = transportation_picker(destination)
     entertainment = entertainment_picker(destination)
     restaurant = restaurant_picker(destination)
     final_confirmation(destination, transportation, entertainment, restaurant)
 else:
     print('Enjoy your vacation!')
