import random

NUMBER_MIN = 1
NUMBER_MAX = 10
LIFE = 4
MAGIC_NUMBER = random.randint(NUMBER_MIN, NUMBER_MAX)
# won = False
number = 0
life = LIFE

def ask_number(nb_min, nb_max):
    number_int = 0
    while number_int == 0:
        number_str = input(f"Quel est le nombre magique (entre {nb_min} et {nb_max}) ? ")
        try:
            number_int = int(number_str)
        except:
            print("ERREUR : Vous devez rentrer un nombre. Réessayez.")
        else:
            if number_int < nb_min or number_int > nb_max:
                print(f"ERREUR : Le nombre doit être entre {nb_min} et {nb_max}. Réessayez.")
                number_int = 0
    return number_int

while not number == MAGIC_NUMBER and life > 0:
    print(f"Il vous reste {life} vies.")
    number = ask_number(NUMBER_MIN, NUMBER_MAX)
    if number == MAGIC_NUMBER:
        print("Bravo, vous avez gagné !")
    elif number < MAGIC_NUMBER:
        print("Le nombre magique est plus grand.")
        life -= 1
    else:
        print("Le nombra magique est plus petit.")
        life -= 1
"""
for i in range(0, LIFE):
    life = LIFE - i 
    print(f"Il vous reste {life} vies.")
    number = ask_number(NUMBER_MIN, NUMBER_MAX)
    if number == MAGIC_NUMBER:
        print("Bravo, vous avez gagné !")
        won = True
        break
    elif number < MAGIC_NUMBER:
        print("Le nombre magique est plus grand.")
    else:
        print("Le nombra magique est plus petit.")
        
if not won:
    print(f"Vous avez perdu ! Le nombre magique était {MAGIC_NUMBER}.")
"""

if life == 0:
    print(f"Vous avez perdu ! Le nombre magique était {MAGIC_NUMBER}.")