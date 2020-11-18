def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  minimum = min(likelihoods)
  maximum = max(likelihoods)
  values = (maximum, minimum)
  return values

values = likelihood()

print("Minimum likelihood of falling: {}% ".format(values[1]))
print("Maximum likelihood of falling: {}% ".format(values[0]))