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
from fonctions import *

def main(n: int, m: int) -> int:
    p: int = prime_facto(n)
    q: int = n//p
    rho: int = (p - 1) * (q - 1)
    liste_diviseur_rho = dec(rho)
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
    print('clef privée => ',main(998573858851677179,485165299))


