def directions():
  directions = []
  directions.append("Move Forward")
  directions.append("Move Backward")
  directions.append("Turn left")
  directions.append("Turn right")
  return directions

def run():
  print(str(directions()))

run()