def dec(N: int) -> list:
    """
    fonction pour décomposer le nombre N en produit de facteur premier
    """
    Resultat = []
    d = 2
    while N % d == 0:
        Resultat.append(d)
        q = int(N / d)
        N = q
    d = 3
    while d <= N**0.5:
        while N % d == 0:
            Resultat.append(d)
            q = int(N / d)
            N = q
        d += 2
    return Resultat


def PGCD(nombre_1: int, nombre_2: int) -> int:
    """
    # PGCD
    ## description
    Fonction pour trouver le plus grand diviseur commun de deux nombres
    ## input
    * nombre_1 : int => premier nombre
    * nombre_2 : int => deuxième nombre
    ## output
    * int => plus grand diviseur commun
    ## algorithme
    On utilise ici l'algorithme d'Euclide
    """
    if nombre_2 == 0:
        return nombre_1
    return PGCD(nombre_2,nombre_1%nombre_2)

def prime_facto(nombre: int) -> int:
    """
    # prime_facto
    ## description
    fonction de factorisation en nombre premier
    ## input
    * nombre : int => nombre à factoriser
    ## output
    * list => facteurs
    ## algorithme
    on utilise l'algorithme rho pollard
    """
    f = lambda x : x*x+1
    x, y, d = 2, 2, 1
    while d==1:
        x = f(x) % nombre
        y = f(f(y)) % nombre
        d = PGCD(x-y, nombre)
        print(d, end='\r')
    return d

def find_k(list_diviseur,rho,m)->list:
    """
    fonction pour trouver k
    """
    for k in list_diviseur:
        e = k * rho + 1
        if e % m == 0:
            return int(e/m)
