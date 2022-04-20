
import interface

# CHOICE_METHOD = ['Кількість перестановок', 'Розміщення з повтореннями', 'Розміщення без повторень',
#                  'Сполучення з повтореннями', 'Сполучення без повторень']


print("[1] - P(n)")
print("[2] - _P(n)")
print("[3] - A(n, k)")
print("[4] - _A(n, k)")
print("[5] - C(n, k)")
print("[6] - _C(n, k)")
n = input()

match n:
    case "1":
        interface.printP()
    case "2":
        interface.print_P()
    case "3":
        interface.printA()
    case "4":
        interface.print_A()
    case "5":
        interface.printC()
    case "6":
        interface.print_C()


