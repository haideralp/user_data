# Task 2 - Input tailored message



print("Please enter your first and last name")
firstname =input("first name"+" ")
lastname =input("last name"+" ")
fullname = firstname.capitalize() + " " + lastname.capitalize()  # making first letter capital
print("Your full name is...")
print(fullname)
height_ft = float(input("height in ft"+" ")) # height in ft 5.10 = 5ft 10 inches
print("Your height in ft is...")
print(height_ft)
favourite_colour = input("colour"+" ")  # specified input
print(favourite_colour)
print("Your favourite colour is")  # fav colour is printed here
secret_spirit_animal = input("animal"+" ")
print("Your secret spirit animal is")
print(secret_spirit_animal)
print(secret_spirit_animal[0]) # printing first letter
print(secret_spirit_animal[-1]) # printing last letter
print(len(secret_spirit_animal)) # printing number of characters
