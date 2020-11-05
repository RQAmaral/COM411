steps = int(input("How far are we from the cave?\n"))

for count in range(steps):
  print(str(steps - count) + " steps remaining")
print("We have reached the cave!")