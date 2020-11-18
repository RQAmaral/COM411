def directions():
  directions = []

  directions.append("Move Forward")
  directions.append("Move Backward")
  directions.append("Turn left")
  directions.append("Turn right")

  return directions

def menu():
  print("Please select the direction")
  list_of_directions = directions()
  for i in range (0,len(list_of_directions), 1):
    print("{}, {}".format(i, list_of_directions[i]))
  direction_to_follow = list_of_directions[int(input())]
  return direction_to_follow

def run():
  route = []
  print("Working out escape route")
  for i in range(0,5,1):
    route.append(menu())

  print("Escape route: "+str(route))
run()