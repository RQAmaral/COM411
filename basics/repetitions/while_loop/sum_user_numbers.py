numbers = int(input("How many numbers should I sum up?\n"))

count = 0
sum_of_numbers = 0

while count < numbers:
  count += 1
  sum_of_numbers += int(input("Please enter number {} of {}:\n".format(str(count), str(numbers))))

print("The answer is " + str(sum_of_numbers))