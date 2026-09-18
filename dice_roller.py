import random

while True:
  input("Press enter to roll the dice!")
  
  dice = random.randint(1, 6)
  print("You rolled:", dice)
  
  again = input("Roll again? (yes/no): ")
  
  if again.lower() != "yes":
        break
