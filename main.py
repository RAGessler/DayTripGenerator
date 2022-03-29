import functions
import resources

print('Hello and welcome to the vacation randomizer!')
locked_destination = functions.destination_picker()
locked_transport = functions.transportation_picker(locked_destination)
locked_entertainment = functions.entertainment_picker(locked_destination)
locked_restaurant = functions.restaurant_picker(locked_destination)
final_confirmation = functions.final_confirmation(locked_destination,locked_transport, locked_entertainment, locked_restaurant )
final_confirmation