import random

print("Welcome to the Vacation Planner Chat Bot!")
print("Please put in your favorite weather \n(sunny, rainy, cloudy, or windy) and the bot will \n generate the vaction of a lifetime!")

user_response = input("Please enter your favorite weather: ")

rainy_places = ["Mawsynram, Meghalaya, India", "Cropp River, New Zealand", "Sinchaun Province, China", " Haleakala Volcano National Park"]

sunny_places = ["Phuket, Thailand", "Havana, Cuba", "Rio de Janeiro, Brazil", "Costa Del Sol, Spain"]

cloudy_places = ["Seattle, Washington", "Torshavn, Faroe Islands", "Dikson, Russia", "Sao Joaquim, Brazil"]

windy_places = ["Patagonia","Amarillo, Texas", "Mount Everest", "Barrow, Alaska"]

def favorite_weather(user_respone):
  if user_respone == "rainy":
    print("You should visit " + random.choice(rainy_places) + ".")
  elif user_respone == "sunny":
    print("You should visit " + random.choice(sunny_places) + ".")
  elif user_respone == "cloudy":
    print("You should visit " + random.choice(cloudy_places) + ".")
  elif user_respone == "windy":
    print("You should visit " + random.choice(windy_places) + ".")
  else:
    print("Sorry I don't have a suggestion for a vacation.")

favorite_weather(user_response)