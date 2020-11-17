characters = input("What strange markings do you see?")
print("Identifying...")

for position in range(0, len(characters),1):
  print("index " + str(position) + ": " + characters[position])

print("Done!")