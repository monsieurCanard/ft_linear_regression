import os
from time import sleep


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def prog_header():
    clear_screen()
    print(r"""
        
        -- Welcome to FT Linear Regression Program --
       -------
     _/       \_
    / |       | \
   /  |__   __|  \
  |__/((o| |o))\__|
  |      | |      | 
  |\     |_|     /|
  | \           / |
   \| /  ___  \ |/ <-- A combien de kilomètres est ta caisse ?
    \ | / _ \ | / 
     \_________/
      _|_____|_
 ____|_________|____
/                   \
      """)
    sleep(1)
    return


def train_header():
    clear_screen()
    print(r"""
          
       -------   
     _/       \_
    / |       | \
   /  |__   __|  \
  |__/((o| |o))\__|
  |      | |      |  
  |\     |_|     /|
  | \           / |
   \| /  ___  \ |/ 
    \ | / _ \ | /  <--- Faites moi voir votre voiture !
     \_________/        Je vais l'analyser et aller chercher mes données...
      _|_____|_
 ____|_________|____
/                   \
      """)
    sleep(2)


def predict_header(final_price: float):
    clear_screen()
    phrase = [
        "Je pourrais accepter… si je veux faire semblant d’avoir un cœur.",
        "Pour ce prix, je devrais presque t’envoyer un message de condoléances.",
        "Je te l’achète si tu me promets de ne jamais dire que tu avais des rêves.",
        "C’est une voiture, pas un miracle, mais je suppose que tu fais ce que tu peux",
    ]

    import random

    final_phrase = random.choice(phrase)

    print(rf"""

       -------   
     _/       \_
    / |       | \
   /  |__   __|  \
  |__/((o| |o))\__|
  |      | |      |  
  |\     |_|     /|
  | \           / |
   \| /  ___  \ |/ 
    \ | / _ \ | /  <--- D'après mes calculs, votre voiture vaut : {final_price} €
     \_________/        {final_phrase}
      _|_____|_
 ____|_________|____
/                   \
      """)
    sleep(5)


def verify_header(accuracy: float, final_price: float, km: float):
    clear_screen()
    print(rf"""\
                                             |
                                         |
                                         |
                                         |
   _______                   ________    |
  |ooooooo|      ____       | __  __ |   |
  |[]+++[]|     [____]      |/  \/  \|   |
  |+ ___ +|     ]()()[      |\__/\__/|   |
  |:|   |:|   ___\__/___    |[][][][]|   |
  |:|___|:|  |__|    |__|   |++++++++|   |
  |[]===[]|   |_|_/\_|_|    | ______ |   |
_ ||||||||| _ | | __ | | __ ||______|| __|
  |_______|   |_|[::]|_|    |________|   \
              \_|_||_|_/               jro\
                |_||_|                     \
               _|_||_|_                     \
      ____    |___||___|                     \
     /  __\          ____                     \
     \( oo          (___ \                     \
     _\_o/           oo~)/ <-- Bob a achete une voiture de {km} km pour {final_price} €
    / \|/ \         _\-_/_     J'aime refait les tests et bob s'ecarte de {accuracy} % des vraies estimations !
   / / __\ \___    / \|/  \    C'est vraiment du super boulot ! Et c'est gratis !
   \ \|   |__/_)  / / .- \ \   
    \/_)  |       \ \ .  /_/ <-- Mais faudrait peut etre faire quelque chose
     ||___|        \/___(_/      pour ameliorer son caractere non ?   
     | | |          | |  |       Ca fait 20 ans qu'il est comme ca ! 
     | | |          | |  |
     |_|_|          |_|__|
     [__)_)        (_(___])
      """)
