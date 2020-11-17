sequence = input("Please input a sequence\n")
character = input("Please enter the character for the marker\n")

position1 = -1
position2 = -1
finalpos = position2 - position1

for counter in range(0,len(sequence),1):
  if sequence[counter] == character:
    if position1 == -1:
      position1 = counter
    else:
      position2 = counter


print("The distance between the two X is " + str(finalpos))