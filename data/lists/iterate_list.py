def movement():
  path = []
  path.append("Move Forward")
  path.append(10)
  path.append("Move Backward")
  path.append(5)
  path.append("Turn left")
  path.append(3)
  path.append("Turn right")
  path.append(1)
  return path

def menu():
  print("Moving...")
  path = movement()
  for i in (0,len(path),2):
    print(str(path[i]) + " for " + str(path[i+1]) + " steps")

menu()

