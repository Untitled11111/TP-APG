

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

    aretes = []

    for s in range( nb_sommets(L)):
        for a in range (nb_sommets(L[s])):
            aretes.append((s,L[s][a][0]))
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
	
def recuperer_sommets(tab):

    # Renvoie les sommetes parce que Python parse automatiquement
    return tab[0]

def recuperer_aretes(tab):

    # Renvoie les arêtes parce que Python parse automatiquement
    return tab[1]

def Prim(L2, v0):
    ##-----A FAIRE-----##
    c = [-1]*nb_sommets(L2) #Les clefs, initialisées à -1. Vous avez le droit de changer la valeur par défaut.
    pi = [-1]*nb_sommets(L2)#Les prédécesseurs dans l'arbre minimal à construire, initialisées à -1. Vous avez le droit de changer la valeur par défaut.

    liste_blanc = []
    liste_gris = []
    liste_noir = []


    # remplissage liste blanche
    for i in range ( len(get_sommets(L2))) : 
        liste_blanc.append(i)

    liste_noir.append(liste_blanc[0])
    print( " Ma vie elle est nul ", nb_sommets(liste_noir)  )

    liste_gris.append(succ(L,liste_noir[0])) 
    print(" En plus je suis bronze ",nb_sommets(liste_gris) ) 


    ##-----Fin à faire-----##
    return pi	

L = [[(1,3),(2,4),(4,6)],[(3,2)],[(4,1)],[(4,2)],[(1,3)]]
#Les tests

'''

print("---Les tests sur L---")
print("nb_sommets L : ", nb_sommets(L))
print("get_sommets L :", get_sommets(L))
print("get_aretes L :", get_aretes(L))
ajouter_arete(L,1,2,9)
print("get_aretes L v2:", get_aretes(L))
i = 0
print("succ(",i,") = ", succ(L,i))

'''

print("PUTE")

# 
for sous_tab in L:  
    for tuples in sous_tab:  
        print(" sommet " , recuperer_sommets(tuples) , " arêtes " , recuperer_aretes(tuples))  

print("PUTE")

print("---L2, à vous---")
L2 = [[(1,4),(2,1)],[(3,3),(4,6)],[(1,2)],[(1,1),(4,1)],[(2,2)]]



#Initialisation de L2
print("nb_sommets L2 : ", nb_sommets(L2))
print("get_sommets L2 :", get_sommets(L2))
print("get_aretes L2 :", get_aretes(L2))

print("succ de 0 ",succ(L2,0))
print("succ de 1 ",succ(L2,1))
print("succ de 2 ",succ(L2,2))
print("succ de 3 ",succ(L2,3))
print("succ de 4 ",succ(L2,4))

print(Prim(L2,0))
##-----Fin à faire-----##
	

