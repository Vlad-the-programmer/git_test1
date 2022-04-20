
from Comb import Factorial

comb = Factorial()

def printP():
    print("P(n)")
    print("n = ", end="")
    n = int(input())

    print(f"P({n}) = ", int(comb.factorial(n)))

def print_P():
    print("_P(n)")
    print("n = ", end="")
    n = int(input())

    res = 1
    for i in range(2, n):
        res *= comb.factorial(i)

    print(f"P({n}) = ", int(comb.factorial(n)/res))

def printA():
    print("A(n, k)")
    print("n = ", end="")
    n = int(input())
    print("k = ", end="")
    k = int(input())

    print(f"A({n}, {k}) = ", comb.A(n, k))

def print_A():
    print("_A(n, k)")
    print("n = ", end="")
    n = int(input())
    print("k = ", end="")
    k = int(input())

    print(f"_A({n}, {k}) = ", comb.A1(n, k))

def printC():
    print("C(n, k)")
    print("n = ", end="")
    n = int(input())
    print("k = ", end="")
    k = int(input())

    print(f"C({n}, {k}) = ", comb.C(n, k))

def print_C():
    print("_C(n, k)")
    print("n = ", end="")
    n = int(input())
    print("k = ", end="")
    k = int(input())

    print(f"_C({n}, {k}) = ", comb.C1(n, k))