

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

def meilleur_clef(L, gris):
    min_val = 0
    min_sommet = -1
    
    for sommet in range(len(L)):
        if gris[sommet] and L[sommet] < min_val:
            min_val = L[sommet]
            min_sommet = sommet
    
    return min_sommet

def clef_vers_arêtes(L, blanc, noir, valeur):

    a_supprimer = 0  

    for elem in blanc:
            if elem[0] == valeur:  
                a_supprimer = elem

    if ( a_supprimer != None):
        blanc.pop(a_supprimer)  
        noir.append(a_supprimer)   
        a_supprimer = None

	
def Prim(L2, v0):
    
    pi = [-1] * nb_sommets(L2)  
    c = [-1] * nb_sommets(L2)  

    blanc = [True] * nb_sommets(L2)
    gris = [False] * nb_sommets(L2)
    noir = [False] * nb_sommets(L2)    

    aretes_blanc = []
    aretes_noir = []

    for i in range ( nb_sommets(L2)) : 
        aretes_blanc.append(succ(L2,i))

    c[v0] = 0 
    blanc[v0] = False
    noir[v0] = True  
    gris.append(succ(L2,v0))

    print("blanc", blanc)
    print("noir", noir) 

    meilleur_sommet = meilleur_clef(c, gris)
    noir[meilleur_sommet] = True
    blanc[meilleur_sommet] = False
    gris.append(succ(L2,meilleur_sommet))
    clef_vers_arêtes(L2, aretes_blanc,aretes_noir,meilleur_sommet)

    print("blanc", blanc)
    print("noir", noir)

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


print("---L2, à vous---")
L2 = [ [(1,4),(2,1)], [(3,3),(4,6)], [(1,2)],  [(1,1),(4,1)], [(2,2)]]



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
	

