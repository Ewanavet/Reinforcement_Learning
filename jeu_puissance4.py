from random import randint
import numpy as np

class puissance4():
    def __init__(self, size=7):
        self.size = size
        self.grid = self.init_grid(size)
        print("La partie à commencée.")

    def init_grid(self, size):
        grid = [size * [0] for i in range(size)]
        return grid

    def prt_grid(self):
        col_names = [" " + chr(65+i) for i in range(self.size)]
        print(" ".join(col_names))
        for i in range(len(self.grid)):
            print(self.grid[i])

    def place(self, player, column):
        # Vérifiez si la colonne est valide (entre A et F)
        if column not in ['A', 'B', 'C', 'D', 'E', 'F'] and column in range(0, self.size):
            col_index = column
        else:
            print(f"Colonne invalide. Choisissez une colonne entre A et {chr(size+64)} ou 0 et {self.size}.")

        # Convertissez la lettre de la colonne en un index (0 à 5)
        col_index = ord(column) - ord('A')

        # Trouvez la première ligne vide dans la colonne
        for row in range(self.size-1, -1, -1):
            if self.grid[row][col_index] == 0:
                self.grid[row][col_index] = player
                break

        
    def check_win(self, player):
        # Vérification des alignements horizontaux
        for row in range(self.size):
            for col in range(self.size-4):
                if (
                    self.grid[row][col] == player
                    and self.grid[row][col + 1] == player
                    and self.grid[row][col + 2] == player
                    and self.grid[row][col + 3] == player
                ):
                    print(f"Joueur {player} a gagné horizontalement.")
                    return True

        # Vérification des alignements verticaux
        for row in range(self.size-4):
            for col in range(self.size):
                if (
                    self.grid[row][col] == player
                    and self.grid[row + 1][col] == player
                    and self.grid[row + 2][col] == player
                    and self.grid[row + 3][col] == player
                ):
                    print(f"Joueur {player} a gagné verticalement.")
                    return True

        # Vérification des alignements en diagonale (descendante)
        for row in range(self.size-4):
            for col in range(self.size-4):
                if (
                    self.grid[row][col] == player
                    and self.grid[row + 1][col + 1] == player
                    and self.grid[row + 2][col + 2] == player
                    and self.grid[row + 3][col + 3] == player
                ):
                    print(f"Joueur {player} a gagné en diagonale (descendante).")
                    return True

        # Vérification des alignements en diagonale (montante)
        for row in range(self.size-4, self.size):
            for col in range(self.size-4):
                if (
                    self.grid[row][col] == player
                    and self.grid[row - 1][col + 1] == player
                    and self.grid[row - 2][col + 2] == player
                    and self.grid[row - 3][col + 3] == player
                ):
                    print(f"Joueur {player} a gagné en diagonale (montante).")
                    return True

        return False

    def is_full(self):
        return all(all(cell != 0 for cell in row) for row in self.grid)

size = 7
jeu = puissance4(size=size)
joueur = 1
nbs_tours = 0
while True:
    # colonne = input(f"Joueur {joueur}, choisissez une colonne (A-F) pour jouer : ")
    colonne = chr(randint(0,size)+64)
    nbs_tours += 1

    print(f"Joueur {joueur}, à jouer en {colonne} ")
    # Vérifiez si la partie est terminée après chaque coup
    if jeu.check_win(joueur) or jeu.is_full():
        jeu.prt_grid()
        print("La partie est terminée.", nbs_tours//2)
        break
    else:
        jeu.prt_grid()
        jeu.place(joueur, colonne)

    joueur = 3 - joueur 