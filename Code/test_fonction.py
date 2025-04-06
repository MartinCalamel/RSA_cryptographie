import pytest

from fonctions import dec, PGCD, prime_facto, find_k

def test_dec():
    assert dec(2) == [2]
    assert dec(8) == [2, 2, 2]
    assert dec(15) == [3, 5]
    assert dec(1) == []
    assert dec(97) == []

def test_PGCD():
    assert PGCD(54, 24) == 6
    assert PGCD(101, 10) == 1
    assert PGCD(0, 10) == 10
    assert PGCD(10, 0) == 10
    assert PGCD(0, 0) == 0

def test_prime_facto(monkeypatch):
    # Prime factor of 8051 is 97 (8051 = 83 * 97)
    # This function returns only ONE non-trivial factor
    result = prime_facto(8051)
    assert result in [83, 97]

def test_find_k():
    divs = [1, 2, 3, 4, 5, 6]
    rho = 2
    m = 3
    # k = 1 -> e = 3 => divisible by 3 → valid
    assert find_k(divs, rho, m) == 1

    divs = [1, 2, 3]
    rho = 4
    m = 5
    # k = 1 -> 5, OK
    assert find_k(divs, rho, m) == 1

    # Test when no valid k exists
    assert find_k([1, 2], 3, 7) is None
