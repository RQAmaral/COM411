def observed():
  observations = []
  for i in range(0,7):
    observation = input("Please enter an observation")
    observations.append(observation)
  return observations

def run():
  print("Counting...")
  local_variable = observed()
  counting = set()
  