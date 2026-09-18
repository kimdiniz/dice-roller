import random

while True:
  input("Press enter to roll the dice!")
  
  dice = random.randint(1, 6)
  print("You rolled:", dice)
  
  again = input("Roll again? (Yes/No): ")
  
  if again.lower() != "yes":
        break
