def climb_ladder(steps_remaining,steps_climbed):
  if steps_climbed < steps_remaining:
    print("Still some way to go")
  else:
    print("Almost there!")

climb_ladder(10,4)
climb_ladder(4,10)