

Operators = ['+', '-', '*', '/', '(', ')', '^']  # collection of Operators

Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # dictionary having priorities of Operators


def isOperator(c):
    return (not (c >= 'a' and c <= 'z') and not(c >= '0' and c <= '9') and not(c >= 'A' and c <= 'Z'))


def getPriority(C):
    if (C == '-' or C == '+'):
        return 1
    elif (C == '*' or C == '/'):
        return 2
    elif (C == '^'):
        return 3
    return 0


def infixToPostfix(expression):
    stack = []  # initialization of empty stack

    output = ''

    for character in expression:

        if character not in Operators:  # if an operand append in postfix expression

            output += character

        elif character == '(':  # else Operators push onto stack

            stack.append('(')

        elif character == ')':

            while stack and stack[-1] != '(':
                output += stack.pop()

            stack.pop()

        else:

            while stack and stack[-1] != '(' and Priority[character] <= Priority[stack[-1]]:
                output += stack.pop()

            stack.append(character)

    while stack:
        output += stack.pop()

    return output


def infix_to_prefix(infix):

        operands = []
        operators = []

        for i in range(len(infix)):

            if (infix[i] == '('):
                operators.append(infix[i])

            elif (infix[i] == ')'):
                while (len(operators) != 0 and operators[-1] != '('):
                    # operand 1
                    op1 = operands[-1]
                    operands.pop()

                    # operand 2
                    op2 = operands[-1]
                    operands.pop()

                    # operator
                    op = operators[-1]
                    operators.pop()

                    tmp = op + op2 + op1
                    operands.append(tmp)

                operators.pop()

            elif (not isOperator(infix[i])):
                operands.append(infix[i] + "")

            else:
                while (len(operators) != 0 and getPriority(infix[i]) <= getPriority(operators[-1])):
                    op1 = operands[-1]
                    operands.pop()

                    op2 = operands[-1]
                    operands.pop()

                    op = operators[-1]
                    operators.pop()

                    tmp = op + op2 + op1
                    operands.append(tmp)
                operators.append(infix[i])


        while (len(operators) != 0):
            op1 = operands[-1]
            operands.pop()

            op2 = operands[-1]
            operands.pop()

            op = operators[-1]
            operators.pop()

            tmp = op + op2 + op1
            operands.append(tmp)

        return operands[-1]


def prefixToInfix(prefix):
    stack = []

    # read prefix in reverse order
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):

            # symbol is operand
            stack.append(prefix[i])
            i -= 1
        else:

            # symbol is operator
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1

    return stack.pop()


def isOperand(x):
    return ((x >= 'a' and x <= 'z') or
            (x >= 'A' and x <= 'Z'))


def postfix_to_infix(exp):
    s = []

    for i in exp:


        if (isOperand(i)):
            s.insert(0, i)

        # We assume that input is a
        # valid postfix and expect
        # an operator.
        else:

            op1 = s[0]
            s.pop(0)
            op2 = s[0]
            s.pop(0)
            s.insert(0, "(" + op2 + i +
                     op1 + ")")


    return s[0]






