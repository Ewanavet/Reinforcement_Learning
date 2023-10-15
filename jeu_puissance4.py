from random import randint, uniform
import numpy as np

class puissance4():
    def __init__(self, size=7):
        self.size = size
        self.grid = self.init_grid(size)
        print("La partie à commencée.")

    def init_grid(self, size):
        grid = [size * [0] for i in range(size)]
        return grid
    
    def reset(self):
        self.grid = [self.size * [0] for i in range(self.size)]

    def prt_grid(self):
        col_names = [" " + chr(65+i) for i in range(self.size)]
        print(" ".join(col_names))
        for i in range(len(self.grid)):
            print(self.grid[i])

    def place(self, player, column):
        # Vérifiez si la colonne est valide (entre A et F)
        if column.upper() not in [chr(65+i) for i in range(self.size)] and column in range(0, self.size):
            col_index = column

        # Convertissez la lettre de la colonne en un index (0 à 5)
        col_index = ord(column.upper()) - ord('A')

        # Trouvez la première ligne vide dans la colonne
        for row in range(self.size-1, -1, -1):
            if self.grid[row][col_index] == 0:
                self.grid[row][col_index] = player
                break

    def step(self, joueur, action):
            # Trouvez la première ligne vide dans la colonne[action] et y placer le jeton du joueur
            for row in range(self.size-1, -1, -1):
                if self.grid[0][row][action] == 0:
                    self.grid[0][row][action] = joueur
                    break

            for col in range(self.size):
                for row in range(self.size - 1, -1, -1):
                    if self.grid[row][col] == 0:
                        self.grid[row][col] = 3-joueur
                        if self.check_win(3-joueur):
                            # Annule le coup pour éviter de modifier la grille
                            self.grid[row][col] = 0
                            return -1
                        # Annule le coup pour explorer d'autres possibilités
                        self.grid[row][col] = 0
                        break

            return 0
                
    def check_win(self, joueur):
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

        return False

    def is_full(self):
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
        for s in range(self.grid_size*self.grid_size*2): # nbs de cases * 2 car 2 joueur
            self.V[s] = 0.
        self.win_nb = 0.
        self.lose_nb = 0.
        self.rewards = []
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
        vmin = None # value state la plus basse pour désavantager l'adversaire
        vi = None
        for i in range(len(actions)):
            new_state = state
            # Trouvez la première ligne vide dans la colonne
            for row in range(self.grid_size-1, -1, -1):
                if state[0][row][i] == 0:
                    new_state[0][row][i] = state[1]
                    break
            # on vérifie que l'état est jouable (colone non remplie) et que value state la plus basse et celle qui arrive
            if len(state[0][i]) < self.grid_size and (vmin is None or vmin > self.V[new_state]):
                vmin = self.V[new_state]
                vi = i
        return actions[vi if vi is not None else 0]

    def play(self, state):
        # PLay given the @state (int)
        if self.is_human is False:
            # Take random action
            if uniform(0, 1) < self.eps:
                action = randint(0, self.grid_size)
            else: # Or greedy action
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
            if r == 0:
                self.V[s] = self.V[s] + 0.001*(self.V[sp] - self.V[s])
            else:
                self.V[s] = self.V[s] + 0.001*(r - self.V[s])

        self.history = []


size = 7
jeu = puissance4(size=size)
joueur = 1
while not jeu.check_win(1) and not jeu.check_win(2) and not jeu.is_full():
    jeu.prt_grid() if joueur == 1 else None

    print(f"-------------- Joueur {joueur} --------------")
    if joueur == 1:
        colonne = input(f"Joueur {joueur}, choisissez une colonne entre A et {chr(size+64)} ou 0 et {size}. : ")
    else:
        colonne = chr(randint(0,size)+64)
        # colonne = "A"
    print(f"Joueur {joueur} à jouer en {colonne}.")
    jeu.place(joueur, colonne)


    print(jeu.step(3-joueur), "reward")
    joueur = 3 - joueur 

print("La partie est terminée.")
jeu.prt_grid()

# nbs_tours = 0
# while True:
#     # colonne = input(f"Joueur {joueur}, choisissez une colonne entre A et {chr(size+64)} ou 0 et {size}. : ")
#     colonne = chr(randint(0,size)+64)
#     nbs_tours += 1

#     print(f"Joueur {joueur}, à jouer en {colonne} ")
#     # Vérifiez si la partie est terminée après chaque coup
#     if jeu.check_win(joueur) or jeu.is_full():
#         jeu.prt_grid()
#         print("La partie est terminée.", nbs_tours//2)
#         break
#     else:
#         jeu.prt_grid()
#         jeu.place(joueur, colonne)

#     joueur = 3 - joueur 