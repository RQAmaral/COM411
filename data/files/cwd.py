import os
def cwd():
  path = os.getcwd()
  print(f"The current working directory is {path}")
  print("The directory contains the following: " + str(os.listdir(path)))

def run():
  print("Processing...")
  cwd()

run()