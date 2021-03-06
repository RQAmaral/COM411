def observed():
  observations = []
  for i in range(0,5):
    observation = input("Please enter an observation\n")
    observations.append(observation)
  return observations

def run():
  print("Counting...")
  local_variable = observed()
  counting = set()

  for observation in local_variable:
    tuple_object = (observation, local_variable.count(observation))
    counting.add(tuple_object)
    
  for observation in counting:
    print(f"{observation[0]} observed {observation[1]} times")
run()