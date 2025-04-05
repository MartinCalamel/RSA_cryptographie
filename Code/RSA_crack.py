"""
Author: Martin Calamel
Created: 2025-04-05
Description: méthode pour retrouver la clef privée à partir d'une clef publique RSA 
TODO: [ OK ] fonction de factorisation
      [ OK ] calcule de rho
      [ OK ] calcule des diviseur de rho (k potentiels)
      [ OK ] calcule de e entier exposant privé.
      [ NO ] fonction de test unitaire
"""

import sys
from random import randint
from itertools import combinations

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
    return d

def millerTest(a,d,n,r):
    # test de Miller pour un témoin a
    # Retourne faux si n est composé et vrai si n est probablement premier
    # d et r doivent vérifier n = 2^r * d + 1 avec d impair   
           
    x = pow(a, d, n) # Calcule a^d % n   
    if (x == 1  or x == n-1): 
       return True
    for _ in range(r):    
        x = (x * x) % n 
        if (x == 1):
            return False 
        if (x == n-1):
            return True    
   
    return False 
def isPrime(n, k=25): 
    # Test de primalité de Miller Rabin  
    # Si faux alors n est composé et si vrai alors n est probablement premier 
    # k determine le niveau de certitude : P(erreur) < 1/4**k
    
    if (n <= 1 or n == 4):
        return False 
    if (n <= 5):
        return True   
    
    # Trouver d et r tels que n = 2^r * d + 1 avec d impair 
    d = n - 1 
    r = 0
    while (d&1 == 0): 
        d  >>= 1 
        r += 1 
    
    # Effectuer k tests de Miller
    for i in range(k):
        a = randint(2,n-2) 
        if (not millerTest(a, d, n, r)):
              return False  
    return True
def nextPrime(n):
    # premier suivant n
    while not isPrime(n):
        n += 1
    return n
def pollard(n,a=1,c=3):
    # Recherche un diviseur de n
    # Cet algorithme est un mélange des méthodes rho et p-1 de Pollard
    # Echec,si la valeur retournée est n 
    if n&1==0: #pair
        return 2
    b,g=a,1   
    while g==1:
        a = (a*a+1)%n
        b = (b*b+1)%n
        b = (b*b+1)%n
        c = pow(c,a,n)
        g = PGCD(n, ((c-1)*abs(b-a))%n)
    
    #print('Polard rho et p-1 : iter', i, 'n=', n,'g=', g)
    return g
def rho(n,a=2):
    # Recherche un diviseur de n
    # Cet algorithme est une variante de la méthodes rho de Pollard
    # Echec,si la valeur retournée est n   
    x=a  
    g=k=p=1
    i=0    
    while g==1:
        a = (a*a+1)%n
        f = abs(a-x)
        if f==0 or i%k==0:
            g = PGCD(n,p)
            if f==0:
                break
            k<<=1
            x = a
            p = 1
               
        i += 1
        p *= f
        p %= n
        if p==0 and g==1:
            g = PGCD(f,n)
                
    #print('Rho : iter', i, 'n=', n, 'g=', g)
    return g
def factor(n, k=25, div=rho):
    # Décompose n en facteurs probablement premiers
    # div = pollard ou rho
    comp = pow(2,n,n)!=2 # n est composé si vrai
    if n==2 or (n<341 and not comp): # n est un premier < 341 
            return [n]
    if not comp and isPrime(n,k): # n est probablement premier
        return [n]
    if n&1==0: # n est pair
        return [2]+factor(n>>1)
    for p in [3,5,7,11,13,17,19]:
        if n%p==0: #n est divisible par un petit premier
            return [p]+factor(n//p)
    f=div(n) # f est un facteur de n   
    while f==1 or f==n: # tant qu'on n'a pas de facteur strict
        # on essaye avec d'autres valeurs
        f=div(n,a=randint(0,n-1))                   
    return factor(f)+factor(n//f)
# fin du code


def liste_diviseurs(nombre):
    f = factor(nombre)
    while True:
        for n in f:
            if isPrime(n):
                L = ['1']+factor(nombre)
                        
                A = [ [] for _ in range(len(L)-1) ]
                
                for i in range( 2 , len(L)+1 ):
                    for j in combinations(L,i):
                        if j not in A[i-2]:
                            A[i-2].append( j )
                    
                diviseurs_list = [1]
                for line in A:
                    for c in line:
                        p = 1
                        for n in c:
                            p *= int(n)
                        if p not in diviseurs_list:
                            diviseurs_list.append(p)
                
                return sorted(diviseurs_list)







def find_k(list_diviseur,rho,m)->list:
    """
    fonction pour trouver k
    """
    result = []
    for k in list_diviseur:
        e = (k * rho + 1)/m
        print(e)
        if e==int(e):
            result.append(int(e))
    return result

def main(n: int,m: int) -> int:
    p: int = prime_facto(n)
    q: int = n//p
    rho: int = (p - 1) * (q - 1)
    print(rho)
    liste_diviseur_rho = liste_diviseurs(rho)
    print(liste_diviseur_rho)
    e = find_k(liste_diviseur_rho,rho,m)
    return e




def unit_test():
    """
    test unitaires
    """
    print("====== PGCD ======\n")
    print(f"PGCD(21,15) = 3 ==> {PGCD(21,15)} [ {"OK" if PGCD(21,15)==3 else "NO"} ]")
    print(f"PGCD(15,21) = 3 ==> {PGCD(15,21)} [ {"OK" if PGCD(15,21)==3 else "NO"} ]")
    
    print("\n\n====== prime_facto ======\n")
    print(f"prime_facto(60597389) = 101 ==> {prime_facto(60597389)} [ {"OK" if prime_facto(60597389)==101 else "NO"} ]")


if __name__ == '__main__':
    print(main(946308237112698032609,31251982301959))

