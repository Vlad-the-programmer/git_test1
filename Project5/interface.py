from Converter import *



choice = input("What do you want to get: Infix to Prefix --> 1 or Infix to Postfix --> 2 "
               "or\nPostfix to Infix --> 3 or Prefix to Infix --> 4 or  evaluate expression -> 5:\n ")

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
elif choice == '5':
    type_expr = input("Enter a type of expression to be  evaluated(postfix -> p, infix -> i, prefix -> pr: ")
    expression = input("Enter an expression: ")
    if type_expr == 'p':
        print(f"The result is {evaluate_postfix(expression)}")
    elif type_expr == 'pr':
        eval = evaluate_prefix()
        print(f"The result is {eval.evalute(expression)}")
    elif type_expr == 'i':
        print(f"The result is {eval(expression)}")
#prefix
#*+ab^+cdx
#postfix
# ab+cd+x^*
#(a+b)*(c+d)^x -> infix
