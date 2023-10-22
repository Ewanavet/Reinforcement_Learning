from jeu_puissance4 import puissance4, Player
from random import randint

jeu = puissance4()
jeu.prt_grid()
gamma = 0.95


def Q(lr, gamma):
    r = 0
    for i in range(len(lr)):
        r += lr[i] * gamma**i
    return r


joueur = 1
jr = [[], []]
while not jeu.is_finished():
    input("")
    print("joueur", joueur)
    pcases = jeu.playable_cases()
    action = pcases[randint(0, len(pcases) - 1)][1]
    n_state, reward = jeu.step(joueur, action)
    jr[0].append(reward) if joueur == 1 else jr[1].append(reward)
    print("action", action)
    print(reward, "reward")
    jeu.prt_grid()
    joueur = 3 - joueur

print(jr[0], Q(jr[0], gamma))
print(jr[1], Q(jr[1], gamma))
