number = int(input("Please enter a number\n"))

counter = 0
factorial = 1

while counter < number:
  counter += 1
  factorial *= counter

print(str(factorial))