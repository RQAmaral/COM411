def display_in_a_box(word):
  print(" "+"-" * len(word))
  print("|" + str(word) + "|")
  print(" "+"-" * len(word))

def display_lower_case(word):
  print(word.lower())

def display_upper_case(word):
  print(word.upper())

def mirrored(word):
  mirrored_word = ""
  counter = len(word)
  for character in word:
    mirrored_word += word[counter-1]
    counter -= 1
  print(word +" | "+mirrored_word)

def repeat_word(word):
  times = int(input("How many times?\n"))
  for n in range(0,times,1):
    print(word)

def run():
  if operationChoice == 1:
    display_in_a_box(word)
  elif operationChoice == 2:
    display_lower_case(word)
  elif operationChoice == 3:
    display_upper_case(word)
  elif operationChoice == 4:
    mirrored(word)
  elif operationChoice == 5:
    repeat_word(word)
  else:
    print("not an option\n")


word = input("type word\n")
operationChoice = int(input("1) Display in a Box – display the word in an ascii art box\n2) Display Lower-case – display the word in lower-case e.g. hello\n3) Display Upper-case – display the word in upper-case e.g. HELLO\n4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH\n5) Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case.\n"))

run()