#! /usr/local/bin/python3

from os import *
from time import *

headerBar = """  __________________   ___  ___________________   ________________  _   __   __________________
   / / / / / / / / / /  /   |/_  __/_  __/ ____/ | / /_  __/  _/ __ \/ | / /  / / / / / / / / / /
  / / / / / / / / / /  / /| | / /   / / / __/ /  |/ / / /  / // / / /  |/ /  / / / / / / / / / / 
 /_/_/_/_/_/_/_/_/_/  / ___ |/ /   / / / /___/ /|  / / / _/ // /_/ / /|  /  /_/_/_/_/_/_/_/_/_/  
(_|_|_|_|_|_|_|_|_)  /_/  |_/_/   /_/ /_____/_/ |_/ /_/ /___/\____/_/ |_/  (_|_|_|_|_|_|_|_|_) 


"""

for i in range(0, 10):
    system("clear")
    sleep(0.1)
    print(headerBar)
    print("ATTENTION, IL EST FORTEMENT CONSEILLE D'UTILISER LMANAGER EN TANT QUE ROOT !!! VOUS POUVEZ CHOISIR DE NE PAS LE FAIRE, MAIS IL NE SERA PAS POSSIBLE DE GARANTIR SON BON FONCTIONNEMENT !!!\n\n")
    sleep(0.1)

sleep(5)

choice = input("Voulez-vous utiliser LMANAGER en tant que root ? [O;N]\n\n")

while True:
        while True:
            try:
                choice = str(choice)
            except ValueError:
                print("Veuillez répondre par O (pour oui) ou N (pour non) !\n\n")
                sleep(3)
                choice = input("Voulez-vous utiliser LMANAGER en tant que root ? [O;N]\n\n")
                continue
            else:
                choice = choice.lower()
                break
        
        if choice != "o" and choice != "oui" and choice != "n" and choice != "non":
            print("Veuillez répondre par O (pour oui) ou N (pour non) !\n\n")
            sleep(3)
            choice = input("Voulez-vous utiliser LMANAGER en tant que root ? [O;N]\n\n")
            continue
        else:
            break

if choice == "o":
    system("sudo ./linux_manager.py")
else:
    system("./linux_manager.py")

"""
{([{([{([{([{([{|}])}])}])}])}])}   
1XXXXXXXXXXXXXX/0\XXXXXXXXXXXXXX1 
3             /000\             3
5            /00000\            5
7           /0000000\           7
9          /000000000\          9
1         /00000000000\         1
3        |000000|000000|        3  
5        |000000|000000|        5
7        |000000|000000|        7
9        |000000|000000|        9
1        |000000|000000|        1
3        |000000|000000|        3
5         \000000\0000/         5
7          \000000\00/          7
9           \000000\/           9 
1           /\000000\           1
3          /00\000000\          3
5         /0000\000000\         5
7        |000000|000000|        7
9        |000000|000000|        9
1        |000000|000000|        1
3        |000000|000000|        3
5        |000000|000000|        5
7        |000000|000000|        7
9         \00000000000/         9
1          \000000000/          1
3           \0000000/           3
5            \00000/            5
7             \000/             7
9XXXXXXXXXXXXXX\0/XXXXXXXXXXXXXX9  
{([{([{([{([{([{|}])}])}])}])}])}
"""