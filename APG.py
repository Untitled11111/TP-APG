

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

def estVide(F):
	
    if F.size() == 0 :
          return True


def succ_uniquement(L, i):

    tmp = set() 
    
    for sommet, poids in succ(L, i):
        tmp.add(sommet)  

    return list(tmp)  


def meilleur_element (L):
     
    cmp = 0
    min = 10000000000000000
    for sub_element in L : 
        print(" elmeent ", sub_element)
        for truc in sub_element : 
            if ( cmp % 2 == 0 ) :
                if ( truc < min ) : 
                     min = truc 
        cmp = cmp + 1 

    return cmp


def Prim(L2, v0):
    
    pi = [-1] * nb_sommets(L2)  
    c = [-1] * nb_sommets(L2)  

    c[v0] = 0 
    pi[v0] = 0

    blancs = [True] * nb_sommets(L2)
    gris = [False] * nb_sommets(L2)
    noirs = [False] * nb_sommets(L2)
    
    listesuccgris = []
    listesuccnoirs = []

    # tous les successeurs de V0 sont succeptible d'etre appelé 
    listesuccgris.append(succ(L2,v0))
    
    #V0 n'est plus plus mais gris 
    blancs[v0] = False  
    gris[v0] = True  


    for element in listesuccgris : 
        
        meilleur = meilleur_element(element)

        



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


print("succeseur de 0",succ_uniquement(L2,0))
print("succeseur de 1",succ_uniquement(L2,1))
print("succeseur de 2",succ_uniquement(L2,2))
print("succeseur de 3",succ_uniquement(L2,3))


print(Prim(L2,0))
##-----Fin à faire-----##
	

