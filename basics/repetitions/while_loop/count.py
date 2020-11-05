number_of_avoid = int(input("How many live cables must I avoid?\n"))
number_of_live_cables = 0

while number_of_live_cables < number_of_avoid:
  number_of_live_cables += 1
  print("Avoiding...")
  print("...Done! {} live cable avoided!".format(number_of_live_cables))

print("All live cables have been avoided."
)