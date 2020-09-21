from random import choice

#def get_bot_response
#user_response = input("Please enter your favorite weather: ")

#These are lists of places and one will be randomly called from a list when the user enters his/her corresponding favorite weather
rainy_places = ["Mawsynram, Meghalaya, India", "Cropp River, New Zealand", "Sinchaun Province, China", " Haleakala Volcano National Park"]
sunny_places = ["Phuket, Thailand", "Havana, Cuba", "Rio de Janeiro, Brazil", "Costa Del Sol, Spain"]
cloudy_places = ["Seattle, Washington", "Torshavn, Faroe Islands", "Dikson, Russia", "Sao Joaquim, Brazil"]
windy_places = ["Patagonia","Amarillo, Texas", "Mount Everest", "Barrow, Alaska"]


# loop displays bot response w vacation suggestion
def favorite_weather(user_respone):
  
  if user_respone == "rainy":
    return print("You should visit " + choice(rainy_places) + ".")
    
  elif user_respone == "sunny":
    return print("You should visit " + choice(sunny_places) + ".")
    
  elif user_respone == "cloudy":
    return print("You should visit " + choice(cloudy_places) + ".")
    
  elif user_respone == "windy":
    return print("You should visit " + choice(windy_places) + ".")
    
  else:
    return print("Sorry I don't have a suggestion for a vacation.")

#Instrutions for User / Topic/ Greeting
print("Welcome to the Vacation Planner Chat Bot!")
print("Please put in your favorite weather \n(sunny, rainy, cloudy, or windy) and the bot will \n generate the vaction of a lifetime!")

#TODO: we want to keep repeating until the user enters "done" what should we put here?
while True:
  user_response = input("What is your favorite weather?: ")
# Quits program when user responds with 'done'
  if user_response == 'done':
    break
    bot_response = favorite_weather(user_response)
  favorite_weather(user_response)
