from random import randint, uniform
import numpy as np


class puissance4:
    def __init__(self, size=7):
        self.size = size
        self.grid = self.init_grid()
        print("La partie à commencée.")

    def init_grid(self):
        grid = [self.size * [0] for i in range(self.size)]
        return grid

    def reset(self):
        self.grid = [self.size * [0] for i in range(self.size)]
        return self.grid

    def prt_grid(self):
        col_names = [" " + str(i) for i in range(self.size)]
        print(" ".join(col_names))
        for i in range(len(self.grid)):
            print(self.grid[i])

    def step(self, joueur, action):
        # Trouvez la première ligne vide dans la colonne[action] et y placer le jeton du joueur
        for row in range(self.size - 1, -1, -1):
            if self.grid[row][action] == 0:
                self.grid[row][action] = joueur
                break

        if self.is_finished():
            return self.grid, 1

        return self.grid, 0

    def is_finished(self):
        for joueur in [1, 2]:
            # Vérification des alignements horizontaux
            for row in range(self.size):
                for col in range(self.size - 3):
                    if all(self.grid[row][col + i] == joueur for i in range(4)):
                        return True

            # Vérification des alignements verticaux
            for col in range(self.size):
                for row in range(self.size - 3):
                    if all(self.grid[row + i][col] == joueur for i in range(4)):
                        return True

            # Vérification des alignements en diagonale (descendante)
            for row in range(self.size - 3):
                for col in range(self.size - 3):
                    if all(self.grid[row + i][col + i] == joueur for i in range(4)):
                        return True

            # Vérification des alignements en diagonale (montante)
            for row in range(3, self.size):
                for col in range(self.size - 3):
                    if all(self.grid[row - i][col + i] == joueur for i in range(4)):
                        return True

        return all(all(cell != 0 for cell in row) for row in self.grid)


class Player(object):
    """
    Player
    """

    def __init__(self, is_human, size, trainable=True):
        # @nb Number of stick to play with
        super(Player, self).__init__()
        self.grid_size = size
        self.is_human = is_human
        self.history = []
        self.V = {}
        self.win_nb = 0.0
        self.lose_nb = 0.0
        self.rewards = []
        self.v = []
        self.eps = 0.99
        self.trainable = trainable

    def reset_stat(self):
        # Reset stat
        self.win_nb = 0
        self.lose_nb = 0
        self.rewards = []

    def greedy_step(self, state):
        # Greedy step
        actions = [i for i in range(self.grid_size)]
        vmin = None  # value state la plus basse pour désavantager l'adversaire
        vi = None
        for i in range(len(actions)):
            new_state = state
            # Trouvez la première ligne vide dans la colonne
            for row in range(self.grid_size - 1, -1, -1):
                if state[row][i] == 0:
                    new_state[row][i] = state[1]
                    break
            # on vérifie que l'état est jouable (colone non remplie) et que value state la plus basse et celle qui arrive
            jouable = False
            for j in range(len(state)):
                if state[j][i] == 0:
                    jouable = True
            if str(new_state) not in self.V:
                self.V[str(new_state)] = 0
            if jouable and (vmin is None or vmin > self.V[str(new_state)]):
                vmin = self.V[str(new_state)]

                vi = i
        return actions[vi if vi is not None else 0]

    def play(self, state):
        # PLay given the @state (int)
        if self.is_human is False:
            # Take random action
            if uniform(0, 1) < self.eps:
                action = randint(0, self.grid_size - 1)
            else:  # Or greedy action
                action = self.greedy_step(state)
        else:
            action = int(input(">"))
        return action

    def add_transition(self, n_tuple):
        # s : etat, a : action, r : reward, s' : new_state
        # Add one transition to the history: tuple (s, a , r, s')
        self.history.append(n_tuple)
        s, a, r, sp = n_tuple
        self.rewards.append(r)

    def train(self):
        if not self.trainable or self.is_human is True:
            return

        # Update the value function if this player is not human
        for transition in reversed(self.history):
            s, a, r, sp = transition
            s, sp = str(s), str(sp)
            if s not in self.V:
                self.V[s] = 0
            if sp not in self.V:
                self.V[sp] = 0

            if r == 0:
                self.V[s] = self.V[s] + 0.001 * (self.V[sp] - self.V[s])
            else:
                self.V[s] = self.V[s] + 0.001 * (r - self.V[s])

        self.history = []
