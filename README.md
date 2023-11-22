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

5. https://youtu.be/a0bVIyIJ074?list=RDCMUCVso5UVvQeGAuwbksmA95iA (34'51)
- Q-Learning, Q-Function
- Q(st, at) s:state numéro t et a:action à létat numéro t
- Q(st, at)π = E[Rt+1 + γRt+2 + γ²Rt+3 + γ³Rt+4 + ... | st,at]
- γ : compris ]0:1] et plus il est proche de 1 plus les récompenses lointaine on le même poids que les récompenses proches dans le temps, généralement à 0.9 par défault
- E : est l'éspérance des récompenses que l'on peut éspérer dans létat s et l'instant t actuel (une sorte de moyenne)
- π : signifie qu'a partir de l'etat et de l'action, l'agent prendra les décisions qu'il considère optimales, (exploitation)
- Q(st, at)π = r + γmax at+1 Q(st+1, at+1)π
- Q-table, Ubdate
- Q[st][a] = Q[st][a] + gamma*(r + Q[st+1][a+11]-Q[st][a])

6. https://www.youtube.com/watch?v=RuraP4ef4nU&list=RDCMUCVso5UVvQeGAuwbksmA95iA&index=5 (9'30)

7. https://youtu.be/U9nkd2jt3b8?list=RDCMUCVso5UVvQeGAuwbksmA95iA (41'50)
- Deep Q-Learning
- Q-table devient trop grande pour des environnements complexes, on utilise des réseaux de nerones
- 
 
__C. Jeu du puissance 4 :__
il y a deux joueur, 1 et 2. L'un peut être trouvé par l'autre par 3-joueur (3-1 = 2 et 3-2 = 1).