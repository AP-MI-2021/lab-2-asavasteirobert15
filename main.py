"""
Tema laborator 2 - saptamana 2 - problemele nr 3 si nr 4
"""


def get_goldbach(n) -> (int, int):
    """
    Functia determina numerele prime p1 si p2 astfel incat
    n = p1 + p2 , unde :
              p1 - minim
              p2 - maxim
    Conform conjecturii lui Goldbach, orice numar par > 2 poate fi scris ca suma a 2
    numere prime

    Input:
        - n: Int
    Output:
        - p1, p2: Int
    """
    p1 = 3
    p2 = n - p1
    while p1 < p2:
        if prime(p1) == True and prime(p2) == True:
            return p1, p2
        p1 = p1 + 2
        p2 = n - p1


def test_get_goldbach():
    assert get_goldbach(12) == (5, 7)
    assert get_goldbach(32) == (3, 29)
    assert get_goldbach(100) == (3, 97)


def prime(x: int):
    """
    O functie ajutatoare pentru a afla daca un numar este prim sau nu
    """
    if x < 2:
        return False
    for divizor in range(2, x):
        if x % divizor == 0:
            return False
    return True


def get_newton_sqrt(n, steps) -> float:
    """
    Functia executa un numar de pasi pentru a calcula radicalul
    unui numar folosind metoda lui Newton cu x0 = 2
    Input :
        - n: float
        - steps:  int
    Output :
        - radical : float
    """
    x0 = 2
    while steps > 0:
        radical = x0 - ((x0 ** 2) - n) / (2 * n)
        x0 = radical
        steps = steps - 1
    return radical


def test_get_newton_sqrt ():
    assert get_newton_sqrt(25,25) == 4.982370418859578
    assert get_newton_sqrt(70,29) == 8.098354646316382
    assert get_newton_sqrt(100,80) == 9.996919545610082


def is_palindrome(n):
    """
    Fuctia verifica daca un numar este palindrom
    :param n: int
    :return: bool
    """
    oglinditul_lui_n = 0
    copie_n = n
    while copie_n > 0:
        oglinditul_lui_n = oglinditul_lui_n*10 + copie_n%10
        copie_n = copie_n//10
    if n == oglinditul_lui_n:
        return True
    else:
        return False


def test_is_palindrome():
    assert is_palindrome(1991) == True
    assert is_palindrome(123456789987654321) == True
    assert is_palindrome(1449346193) == False


def main():
    while True:
        print('1. Verificarea conjucturii lui Goldbach')
        print('2. Calcularea radicalului unui numar folosind metoda lui Newton')
        print('3. Verificare daca un numar este palindrom')
        print('x. Exit !')
        optiune = input('Alege optiunea : ')
        if optiune == '1':
            numar = int(input('Introduceti un numar par strict mai mare decat 2: '))
            prim1, prim2 = get_goldbach(numar)
            print(
                f'Numarul {numar} poate fi scris ca suma dintre {prim1} si {prim2} unde acestea au valoare minima, respectiv maxima si sunt prime')
        elif optiune == '2':
            numar = float(input('Introduceti numarul real n: '))
            pasi = int(input('Introduceti numarul de pasi: '))
            radicalul = get_newton_sqrt(numar, pasi)
            print(f'Radicalul numarului {numar}, prin {pasi} pasi a fost aproximat la {radicalul}')
        elif optiune == '3':
            numar = int(input('Introduceti un numar: '))
            if is_palindrome(numar) == True:
                print(f'Numarul {numar} este palindrom')
            else:
                print(f'Numarul {numar} nu este palindrom')
        elif optiune == 'x':
            break


test_get_goldbach()

test_get_newton_sqrt()

test_is_palindrome()

main ()