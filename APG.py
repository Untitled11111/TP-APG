

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

'''
BFS Fait en prévision de l'examin avant l'ancien format. Fonction mais affiche 2 fois le dernier sommet 

# Fonction BFS
def BFS(G, id):

    # Pour chaque sommet G faire 
    for v in G.sommets:
        # Coloriser en blanc 
        v.couleur = 0

    liste_blanc = []
    liste_noir = []

    # Ajouter Sommet0 dans f et colorier Sommet0 en gris 
    sommetdepart = G.get_sommet_by_id(id)
    liste_blanc.append(sommetdepart)

    # Liste_blanc = liste de travail 
    while ( not EstVide(liste_blanc))  :

        # Liste de sommets à traiter 
        for sommetb in liste_blanc: 

            # On les colories en gris pour ne pas qu'ils repassent dans liste_blanc
            sommetb.coloriser_gris()

            # On récupère les successeurs
            Succeseurs = G.get_successeur(sommetb.get_Id())

            for sommets in Succeseurs : 

                # Si les sommets sont de couleurs blancs, on les colories et les ajoutent
                if sommets.get_Couleur() == 0 : 

                    sommets.coloriser_gris()
                    liste_blanc.append(sommets)

            # Après avoir traité le sommet, on le colorie en noir, l'ajoute à la liste noir et le retire
            sommetb.coloriser_noir()
            liste_noir.append(sommetb)
            liste_blanc.pop(0)

    return liste_noir

'''


def estVide(F):
	
    if F.size() == 0 :
          return True


def succ_uniquement(L, i):

    tmp = set() 
    
    for sommet, poids in succ(L, i):
        tmp.add(sommet)  

    return list(tmp)  

def get_clef(tuple):

    return tuple[1]

def get_pi(tuple):

    return tuple[0]

def meilleur_element(lsblanc):

    tmp_sommet, meilleur = lsblanc[0] 

    for sommet, poids in lsblanc:
            if poids < meilleur: 
                meilleur = poids
                tmp_sommet = sommet
            
    return tmp_sommet, meilleur

    

def Prim(L2, v0):
    
    pi = [-1] * nb_sommets(L2)  
    c = [10000] * nb_sommets(L2)  

    c[v0] = 0 
    pi[v0] = 0

    blancs = [True] * nb_sommets(L2)
    gris = [False] * nb_sommets(L2)
    noirs = [False] * nb_sommets(L2)
    
    listesuccgris = []
    listesuccnoirs = []

    # tous les successeurs de V0 sont susceptibles d'être appelés 
    listesuccgris += succ(L2, v0)  

    # V0 n'est plus blanc, il devient gris
    blancs[v0] = False  
    noirs[v0] = True  
    
    # trouve le meilleur élément 
    meilleur = meilleur_element(listesuccgris)

    print(" meileur ", meilleur)

    #extrait le sommet 
    sommet = meilleur[0]
    # extrait l'arêtes 
    arete = meilleur[1]

    print(" sommet " , sommet)
    print(" aretes " , arete)

    noirs[sommet] = True
    gris[sommet] = False

    
    pi[sommet] = v0  
    c[sommet] = arete  

    # MAJ 
    for voisin, poids in succ(L2, sommet):
        if blancs[voisin] and poids < c[voisin]:  
            c[voisin] = poids
            pi[voisin] = sommet

    blancs[sommet] = False
    gris[sommet] = True


    return pi,c


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
	
