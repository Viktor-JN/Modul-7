import os
from time import sleep
from msvcrt import getwch
import random
from colors import bcolors

os.system('cls')



while True:
    print(bcolors.DEFAULT + """Vill du slå en tärning
(J)a eller (N)ej""")
    choice=getwch().upper()
    if choice == "J":
        os.system('cls')
        print("Tärningen slås.")
        sleep(1)
        os.system('cls')
        print("Tärningen slås..")
        sleep(1)
        os.system('cls')
        print("Tärningen slås...")
        sleep(1)
        os.system('cls')
        dice=random.randint(1, 6)
        print(bcolors.RED + "Du slog tärningen och fick", dice)
        sleep(2)
    elif choice == "N":
        print("Okej")
        break
    else:
        print("\n")



while True:
    print(bcolors.GREEN + f"""Vill du komma in på {bcolors.RED}gröna lund?{bcolors.GREEN}
(J)a eller (N)ej""")
    x = getwch().upper()
    if x == "J":
        print(bcolors.BLUE + "Välkommen")
        break
    elif x == "N":
        print("Stick härifrån då")
        exit()
    else:
        continue
