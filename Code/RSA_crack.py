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

from fonctions import dec, prime_facto, find_k


def main(n: int, m: int) -> int:
    p: int = prime_facto(n)
    q: int = n // p
    rho: int = (p - 1) * (q - 1)
    liste_diviseur_rho = dec(rho)
    e = find_k(liste_diviseur_rho, rho, m)
    return e


if __name__ == "__main__":
    print("clef privée => ", main(998573858851677179, 485165299))
