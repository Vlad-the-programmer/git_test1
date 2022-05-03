from Converter import *

choice = input("What do you want to get: Infix to Prefix --> 1 or Infix to Postfix --> 2 "
               "or Postfix to Infix --> 3 or Prefix to Infix --> 4:\n ")

if choice == "1":
    infix = input("Enter an infix expression (without ""): ")
    print(f"Prefix notation: {infix_to_prefix(infix)}")
elif choice == "2":
    expression = input('Enter infix expression (without ""):')
    print(f'Postfix notation: {infixToPostfix(expression)}')
elif choice == "3":
    expression = input('Enter postfix expression (without ""):')
    print(f'Infix notation: {postfix_to_infix(expression)}')
elif choice == "4":
    expression = input('Enter prefix expression (without ""):')
    print(f'Infix notation: {prefixToInfix(expression)}')