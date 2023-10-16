from jeu_puissance4 import puissance4, Player
from random import randint

jeu = puissance4()
jeu.prt_grid()

joueur = 1
while not jeu.is_finished():
    if joueur == 1:
        action = randint(0, 6)
    else:
        action = int(input(">"))
    n_state, reward = jeu.step(joueur, action)
    print("action", action)
    print(reward, "reward")
    jeu.prt_grid()
    joueur = 3 - joueur
