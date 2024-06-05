"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
signMin = 35
colorCharge = 15
signMaterial = 20
# Charge for this sign.
charge = 0

# Number of characters.
numCharacters = input("How many characters will your sign have? :")

# Color of characters.
color = input("Will the characters of your sign be Black or Gold? :")

# Type of wood.
woodType = input("Will your sign be made of Oak or Pine? :")

# Write assignment and if statements here as appropriate.
if numCharacters.isnumeric():
  if int(numCharacters) > 5:
    signMin = int(signMin) + ((int(numCharacters) - 5) * 4)
else:
  print((numCharacters) + " is not a number")
  exit()
  
if str(color) == str("Black"):
  charge = int(signMin)
elif str(color) == str("Gold"):
  charge = int(signMin) + int(colorCharge)
else:
  print((color) + " is not Black or Gold. Please choose one.")
  exit()

if str(woodType) == str("Oak"):
  charge = int(charge) + int(signMaterial)
elif str(woodType) == str("Pine"):
  charge = int(charge)
else:
  print((woodType) + " is not Oak or Pine. Please choose one.")
  exit()
# Output Charge for this sign.
int(charge)
print("The charge for this sign is $" + str(charge))