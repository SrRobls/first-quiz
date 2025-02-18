################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!
import time
def make_oven():
  return Oven()

def alchemy_combine(oven, ingredients, temperature):
  
  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()

  return oven.get_output()

class Oven():
  def __init__(self) -> None:
    self.items = []
  
  # Creación de los metodos:
  def add(self, item):
    return self.items.append(item)

  def freeze(self):
    print("The ingredients, began to freeze")
    time.sleep(0.5)
    print("Done!!")
    return "Freezed Ingredients!!"
  
  def boil(self):
    print("The ingredients, began to boil")
    time.sleep(1)
    print("Done!!")
    return "Ingredients Boiled!!"
  
  def wait(self):
    print("We are waiting for the food!!. yumi, yumi :b")
    time.sleep(2)
    print("Done!!!")
    return "Lets See!!"
  
  def get_output(self):
    # Cases
    if "lead" in self.items and "mercury" in self.items:
      return "gold"
    elif "water" in self.items and "air" in self.items:
      return "snow"
    elif "cheese" in self.items and "dough" in self.items and "tomato" in self.items:
      return "pizza"
    
if __name__ == "__main__":
  print(alchemy_combine(make_oven(), ["cheese", "dough", "tomato"], 150))
  