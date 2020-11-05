location = input("Where should I look?\n(in the bedroom)\n(in the bathroom)\n(in the lab)\n")

if location == "in the bedroom":

  location2 = input("Where in the bedroom should I look?\n(under the bed)\n")

  if location2 == "under the bed":
    print("Found some shoes but no battery\n")
  else:
    print("Found some shoes but no battery\n")

elif location == "in the bathroom":

  location2 = input("Where in the bathroom should I look?\n(in the bathtub)\n")

  if location2 == "in the bathtub":
    print("Found a rubber duck but no battery")
  else:
    print("Found a wet surface but no battery.")

elif location == "in the lab":

  location2 = input("Where in the lab should I look?\n(on the table)\n")

  if location2 == "on the table":
    print("Yes! I found my battery!")
  else:
    print("Found some tools but no battery.")
else:
  print("I do not know where that is but I will keep looking.")