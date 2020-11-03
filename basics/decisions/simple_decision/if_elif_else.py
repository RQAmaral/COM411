painting_direction = input("Towards which direction should I paint (up, down, left or right)?\n")

if painting_direction == "down":
  print("I am painting in the downward direction!\n")
elif painting_direction == "up":
  print("I am painting in the upward direction!\n")
elif painting_direction == "left":
  print("I am painting to the left!\n")
elif painting_direction == "right":
  print("I am painting to the right!\n")
else:
  print("Not a direction.\n")

print("Activity completed!")