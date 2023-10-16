# Reinforcement_Learning
## Introduction au Reinforcement Learning 
__A. Ressources :__
- https://fr.mathworks.com/campaigns/offers/reinforcement-learning-with-matlab-ebook.html?ef_id=Cj0KCQjwm66pBhDQARIsALIR2zDfR5X01OihIwf5cVkUI34p-r6HsQpmJ47rFabBXZ7Dfdb9uaF_KtIaAuaUEALw_wcB:G:s&s_kwcid=AL!8664!3!650602541754!p!!g!!reinforcement%20learning&s_eid=psn_128375755336&q=reinforcement%20learning&gclid=Cj0KCQjwm66pBhDQARIsALIR2zDfR5X01OihIwf5cVkUI34p-r6HsQpmJ47rFabBXZ7Dfdb9uaF_KtIaAuaUEALw_wcB

__B. Explications :__
1. https://youtu.be/PKNxUF9CGn8 (16'31)
- introduction et concept

2. https://youtu.be/a4WUL_KZeZo (8'35)
- ε (epsilon) -> taux d'exploration [0:1]
- greedy = 1-ε -> taux d'exploitation

3. https://youtu.be/m7RyfYNMlA8?list=RDCMUCVso5UVvQeGAuwbksmA95iA (22'56)
- value fonction
- V(s) = V(s) + lr*(V(s') - V(s))
- V(s) -> value state (valeur de l'état)
- lr -> learning rate
- elle modifie la valeur (reward) de l'état actuel par la "moyenne" de la valeure des états possibles

4. https://youtu.be/OKTjheBEvDY?list=RDCMUCVso5UVvQeGAuwbksmA95iA (27'49)
- Jeu des allumettes python : https://github.com/thibo73800/aihub/blob/master/rl/sticks.py

__C. Jeu du puissance 4 :__
il y a deux joueur, 1 et 2. L'un peut être trouvé par l'autre par 3-joueur (3-1 = 2 et 3-2 = 1).