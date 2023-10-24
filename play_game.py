from jeu_puissance4 import puissance4, Player
from random import shuffle
import numpy as np
import time


def play(game, p1, p2, train=True):
    state = game.reset()
    players = [p1, p2]
    shuffle(players)
    p = 0
    while not game.is_finished():
        if p2.is_human == True:
            game.prt_grid()

        action = players[p % 2].play(state)
        n_state, reward = game.step(p % 2 + 1, action)
        # print("player :", p % 2 + 1, "action :", action)
        #  Game is over. Assign stat
        if game.is_finished():
            if p2.is_human == True:
                print("game end")
            # print(reward, p % 2 + 1)
            if p % 2 == 0:
                # Update stat of the current player
                players[p % 2].win_nb += 1
                # Update stat of the other player
                players[(p + 1) % 2].lose_nb += 1
            else:
                # Update stat of the current player
                players[p % 2].lose_nb += 1
                # Update stat of the other player
                players[(p + 1) % 2].win_nb += 1

        # Add the reversed reward and the new state to the other player
        if p != 0:
            s, a, r, sp = players[(p + 1) % 2].history[-1]
            players[(p + 1) % 2].history[-1] = (s, a, reward * -1, n_state)

        players[p % 2].add_transition((state, action, reward, None))

        state = n_state
        p += 1

    if train:
        p1.train()
        p2.train()


size = 7
game = puissance4(size=size)
# PLayers to train
p1 = Player(is_human=False, size=size, trainable=True)
p2 = Player(is_human=False, size=size, trainable=True)

# Human player and random player
human = Player(is_human=True, size=size, trainable=False)
random_player = Player(is_human=False, size=size, trainable=False)

print("Train")
start = time.time()
# Train the agent
for i in range(0, 1000):
    if i % 10 == 0:
        p1.eps = max(p1.eps * 0.996, 0.05)
        p2.eps = max(p2.eps * 0.996, 0.05)
    play(game, p1, p2)
p1.reset_stat()
print(round(time.time() - start, 2), "s")

print(len(p1.V), "states")
print("--------------------------")

print("Play random")
# Play agains a random player
for _ in range(0, 100):
    play(game, p1, random_player, train=False)
print("p1 win rate", p1.win_nb / (p1.win_nb + p1.lose_nb))
print("p1 win mean", np.mean(p1.rewards))

print("Play agains us")
# Play agains us
while True:
    play(game, p1, human, train=False)
