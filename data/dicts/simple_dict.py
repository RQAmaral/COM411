def pattern():
  sequences = {}
  sequences["Short sequences"] = 3
  sequences["Medium sequences"] = 2
  sequences["Long sequences"] = 1

  return sequences

def run():
  dictionary = pattern()
  print(dictionary)

run()