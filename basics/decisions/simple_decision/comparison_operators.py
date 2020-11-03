first_number = int(input("Please enter the first number\n"))
second_number = int(input("Please enter the second number\n"))

if first_number < second_number:
  print("The first number is the smallest!")
elif second_number < first_number:
  print("The second number is the smallest!")
elif first_number == second_number:
  print("Both are equal!")
else:
  print("Please input valid numbers")