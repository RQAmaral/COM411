number_of_charges = int(input("How many bars should be charged?\n"))

number_of_bars_charged = 0
ascii = "█ "

while number_of_bars_charged < number_of_charges:
  number_of_bars_charged += 1
  print("Charging: " + ascii*number_of_bars_charged)

print("The battery is fully charged.")