def cross_bridge(number_of_steps):
    stepCounter = 0
    if number_of_steps < 5:
      while stepCounter < number_of_steps:
        print("Crossed step")
        stepCounter += 1
      print("We must keep going!")
      stepCounter = 0
    else:
      while stepCounter < number_of_steps:
        print("Crossed step")
        stepCounter += 1
      print("Bridge collapsed!")
      

cross_bridge(3)
cross_bridge(5)