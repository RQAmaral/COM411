lives = int(input("Please enter the number of lives.\n"))
energy_level = int(input(" Please enter the energy level.\n"))
shield_level = int(input(" Please enter the shield level.\n"))

lives_display = "♥"
energy_display = "♦"

print("Health has been set\n\n Lives:  {}\n Energy: {}\n Shield: {}".format(lives_display*lives,energy_display*energy_level,energy_display*shield_level))