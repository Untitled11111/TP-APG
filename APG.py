

def nb_sommets(L):
	'''Entrée : une liste d'adjacence
	Sortie : un entier
	Le nombre de sommets'''
	return len(L)

def get_sommets(L):
	'''Entrée : une liste d'adjacence
	Sortie : une liste d'entiers
	Les sommets de L'''
	return [i for i in range(nb_sommets(L))] #À ne pas faire
	
def ajouter_arete(L, i, j, w):
	'''Entrée : une liste d'adjacence, un couple de sommets et un poids
	Sortie : rien
	Ajoute l'arête entre i et j de poids w'''
	L[i].append((j,w)) #À ne pas faire

def get_aretes(L):
	'''Entrée : une liste d'adjacence
	Sortie : une liste de couple de sommets
	Renvoie la liste des arêtes, sans les poids'''
	aretes = []
	##-----A FAIRE-----##


	##-----Fin à faire-----##	
	return aretes

def succ(L, i):
	'''Entrée : une liste d'adjacence et un entier
	Sortie : une liste de couple (sommets, poids)
	renvoie la liste des successeurs de i, avec leurs poids'''
	#À ne pas faire
	succs = []
	for j in range(len(L[i])):
		succs.append(L[i][j])
	return succs
	
def Prim(L, v0):
	##-----A FAIRE-----##
	c = [-1]*nb_sommets(L) #Les clefs, initialisées à -1. Vous avez le droit de changer la valeur par défaut.
	pi = [-1]*nb_sommets(L)#Les prédécesseurs dans l'arbre minimal à construire, initialisées à -1. Vous avez le droit de changer la valeur par défaut.




	##-----Fin à faire-----##
	return pi	

L = [[(1,3),(2,4),(4,6)],[(3,2)],[(4,1)],[(4,2)],[(1,3)]]
#Les tests
print("---Les tests sur L---")
print("nb_sommets : ", nb_sommets(L))
print("get_sommets :", get_sommets(L))
print("get_aretes :", get_aretes(L))
ajouter_arete(L,1,2,9)
print("get_aretes :", get_aretes(L))
i = 0
print("succ(",i,") = ", succ(L,i))



print("---L2, à vous---")
L2 = [[],[],[],[],[]]
##-----A FAIRE-----##
#Initialisation de L2


print(Prim(L2,0))
##-----Fin à faire-----##
	

