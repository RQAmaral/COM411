def display_ladder(steps):
  counter = 0
  while counter < steps:
    print("| |\n***")
    counter += 1
  print("| |")

def create_ladder():
  number_of_ladders = int(input("How many steps remain?"))
  display_ladder(number_of_ladders) 

create_ladder()

