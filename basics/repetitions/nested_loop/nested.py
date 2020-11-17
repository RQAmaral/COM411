rows = int(input("How many rows?\n"))
columns = int(input("How many columns?\n"))
print("Here i go:")

for i in range(0,rows,1):
  for x in range(0,columns,1):
    print(":-)", " ", end="")
  print()