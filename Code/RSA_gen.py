"""
Author: Martin Calamel
Created: 2025-04-06
Description: fonction pour générer un paire de clef RSA la clef sous la forme
    (n,x,y) avec pour clef publique (n,x) et pour clef privé (n,y)
TODO:
"""

import csv
import random

from fonctions import dec, prime_facto


def generate_RSA(path: str) -> list:
    """
    fonction pour générer un paire de clef RSA la clef sous la forme
    (n,x,y) avec pour clef publique (n,x) et pour clef privé (n,y)
    """


if __name__ == "__main__":
    a = open("nb_premiers.txt")
    f = csv.reader(a, delimiter=",")
    nb_prem = []
    for line in f:
        for el in line:
            nb_prem.append(el)
    a.close()
    choix = True
    while choix:
        choix = False
        p = int(nb_prem[random.randint(0, len(nb_prem) - 1)])
        q = int(nb_prem[random.randint(0, len(nb_prem) - 1)])
        n = p * q
        phi = (p - 1) * (q - 1)
        print(phi)
        e = max(dec(phi))
        print(e)
        nb = e * phi + 1
        print(nb)
        x = prime_facto(nb)
        y = nb // x
        print("n=", n, "e=", x, "d=", y)
        if x < 40000 or y < 40000:
            choix = True
