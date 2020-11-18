def likelihoods():

  likelihoods = []
  likelihoods.append(("step 1", 50))
  likelihoods.append(("step 2", 38))
  likelihoods.append(("step 3", 27))
  likelihoods.append(("step 4", 99))
  likelihoods.append(("step 5", 4))

  return likelihoods

def run():

  good_steps = []
  bad_steps = []
  likelihood = likelihoods()

  for i in range(0,len(likelihood)):

    if likelihood[i][1] >= 50:

      bad_steps.append(likelihood[i])

    else:

      good_steps.append(likelihood[i])
  
  print("Good steps: {}\nBad steps: {}".format(len(good_steps), len(bad_steps)))

run()