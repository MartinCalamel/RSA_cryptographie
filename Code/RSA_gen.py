"""
Author: Martin Calamel
Created: 2025-04-06
Description: 
TODO: 
"""




import random
import csv

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

def isprem(n):
	
	"""retourne True si n est premier, False dans le cas contraire.
	n doit être un entier"""
	
	if n == 1 or n == 2:
		
		return True
		
	if n%2 == 0:
		
		return False
		
	r = n**0.5
	
	if r == int(r):
		
		return False
	
	for x in range(3, int(r), 2):

		if n % x == 0:
			
			return False	
	
	return True

def generate_RSA(path: str) -> list:
    """
    fonction pour générer un paire de clef RSA la clef sous la forme
    (n,x,y) avec pour clef publique (n,x) et pour clef privé (n,y)
    """
    a = open(path)
    f = csv.reader(a, delimiter=",")
    nb_prem = []
    for line in f:
        for el in line:
            nb_prem.append(el)
    a.close()
    choix = True
    while choix:
        choix = False
        
        p = random.randint(10000000000,90000000000)
        q = random.randint(10000000000,90000000000)
        
        while isprem(p) is False:
            p = random.randint(10000000000,90000000000)
            
        while isprem(q) is False:
            q = random.randint(10000000000,90000000000)
        n = p * q
        phi = (p - 1) * (q - 1)
        e = max(dec(phi))
        nb = e * phi + 1
        x = dec(nb)
        if len(x) != 1:
            l = len(x) // 2
            res = 1
            for i in range(l):
                res *= max(x)
                x.remove(max(x))
        else:
            res = max(x)
        x = res
        y = nb // x
        print('n=',n,'e=',x,'d=',y)
        if x < 40000 or y < 40000:
            choix = True
    return [n, x, y]

if __name__ == '__main__':
    generate_RSA("nb_premiers.txt")