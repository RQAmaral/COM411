def sum_weights(weight_beep, weight_bop):
  return weight_beep + weight_bop

def calc_avg_weight(weight_beep, weight_bop):
  return (weight_beep + weight_bop)/2

def run():
  weightOfBeep = int(input("What is the weight of Beep?"))
  weightOfBop = int(input("What is the weight of Bop?"))
  operation = input("What would you like to calculate (sum or average)?")

  if operation == "sum":
    print("Sum of the weight is: " + str(sum_weights(weightOfBeep,weightOfBop)))
  elif operation == "average":
    print("Average of weights is: " + str(calc_avg_weight(weightOfBeep,weightOfBop)))
  else:
    return 0

run()