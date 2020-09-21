#helps choice function
from random import choice

#get_bot_response
def favorite_weather(user_respone):

  #atleast 2 lists that store 3 unique responses
  bot_response_rainy = ["Mawsynram, Meghalaya, India", "Cropp River, New Zealand", "Sinchaun Province, China", " Haleakala Volcano National Park"]
  bot_response_sunny = ["Phuket, Thailand", "Havana, Cuba", "Rio de Janeiro, Brazil", "Costa Del Sol, Spain"]
  bot_response_cloudy = ["Seattle, Washington", "Torshavn, Faroe Islands", "Dikson, Russia", "Sao Joaquim, Brazil"]
  bot_response_windy = ["Patagonia","Amarillo, Texas", "Mount Everest", "Barrow, Alaska"]

  #returns string w chatbot response using conditionals
  if user_respone == "rainy":
    print("You should visit " + choice(bot_response_rainy) + ".")
    #used choice()

  elif user_respone == "sunny":
    return print("You should visit " + choice(bot_response_sunny) + ".")

  elif user_respone == "cloudy":
    return print("You should visit " + choice(bot_response_cloudy) + ".")
    
  elif user_respone == "windy":
    return print("You should visit " + choice(bot_response_windy) + ".")
    
  else:
    return print("Sorry I don't have a suggestion for a vacation.")
  #function successfully prints out a chatbot response to user input.

#Greet user
print("Welcome to the Vacation Planner Chat Bot!")

#Instructions / Expected Input
print("Please put in your favorite weather \n(sunny, rainy, cloudy, or windy) and the bot will \n generate the vaction of a lifetime!")

#TODO: we want to keep repeating until the user enters "done" what should we put here?
while True:
  user_response = input("What is your favorite weather?: ")
  
  if user_response == 'done':
    break
# Quits program when user responds with 'done'    
    bot_response = favorite_weather(user_response)
  favorite_weather(user_response)
