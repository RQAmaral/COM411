def observed():
  observations = []
  for i in range(0,5):
    observation = input("Please enter an observation\n")
    observations.append(observation)
  return observations

def remove_observations(observations):
  boolean = True
  while boolean == True:
      yes_or_no = input("do you wish to remove any observation?\n")
      if yes_or_no == "yes":
        target = input("input string to be removed\n")
        for observation in observations:
          if observation == target:
            observations.remove(observation)
      elif yes_or_no == "no":
        return observations

def run():
  print("Counting...")
  local_variable = remove_observations(observed())
  counting = set()

  for observation in local_variable:
    tuple_object = (observation, local_variable.count(observation))
    counting.add(tuple_object)
    
  for observation in counting:
    print(f"{observation[0]} observed {observation[1]} times")
run()