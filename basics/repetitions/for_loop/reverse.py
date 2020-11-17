reversed_phrase = input("What phrase do you see?\n")
right_phrase = ""
position = len(reversed_phrase)

for character in reversed_phrase:
  
  right_phrase += reversed_phrase[position-1]
  position -= 1
  

print(str(right_phrase)) 