first_number = int(input("Please enter the first whole number\n"))
second_number = int(input("Please enter the second whole number\n"))
third_number = int(input("Please enter the third whole number\n"))

even_number_counter = 0
odd_number_counter = 0


if first_number % 2 == 0:
  even_number_counter = even_number_counter + 1
else:
  odd_number_counter = odd_number_counter + 1

if second_number % 2 == 0:
  even_number_counter = even_number_counter + 1
else:
  odd_number_counter = odd_number_counter + 1

if third_number % 2 == 0:
  even_number_counter = even_number_counter + 1
else:
  odd_number_counter = odd_number_counter + 1

print(str(even_number_counter) + ", " + str(odd_number_counter))