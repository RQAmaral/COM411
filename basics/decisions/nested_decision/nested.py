cover_type = input("What type of cover does the book have?(hard or soft)\n")

if cover_type == "soft":
  bound = input("Is the book perfect-bound?\n")
  if bound == "yes":
    print("Soft cover, perfect bound books are very popular!\n")
  else:
    print("Soft covers with coils or stitches are great for short books\n")
else:
  print("Books with hard covers can be more expensive!\n")