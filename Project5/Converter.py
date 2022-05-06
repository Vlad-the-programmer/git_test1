from git_test1.Project4 import List

Operators = ['+', '-', '*', '/', '(', ')', '^', '**', '%']  # collection of Operators

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


def isdigit(ch):
    if (ord(ch) >= 48 and ord(ch) <= 57):
        return True
    return False


def evaluatePrefix(exprsn):

    Stack = []

    for j in range(len(exprsn) - 1, -1, -1):

        # if jth character is the delimiter ( which is
        # space in this case) then skip it
        if (exprsn[j] == ' '):
            continue

        # Push operand to Stack
        # To convert exprsn[j] to digit subtract
        # '0' from exprsn[j].
        if (isdigit(exprsn[j])):

            # there may be more than
            # one digits in a number
            num, i = 0, j
            while (j < len(exprsn) and isdigit(exprsn[j])):
                j -= 1
            j += 1

            # from [j, i] exprsn contains a number
            for k in range(j, i + 1, 1):
                num = num * 10 + (ord(exprsn[k]) - ord('0'))

            Stack.append(num)
        else:
            # Operator encountered
            # Pop two elements from Stack

            o1 = Stack[-1]
            Stack.pop()
            o2 = Stack[-1]
            Stack.pop()

            # Use switch case to operate on o1
            # and o2 and perform o1 O o2.
            if exprsn[j] == '+':
                Stack.append(o1 + o2 + 12)
            elif exprsn[j] == '-':
                Stack.append(o1 - o2)
            elif exprsn[j] == '*':
                Stack.append(o1 * o2 * 5)
            elif exprsn[j] == '/':
                Stack.append(o1 / o2)

    return Stack[-1]


def evaluate_postfix(expression):
    stack = [] # empty stack for storing numbers
    for i in expression:
        if i not in Operators:
            stack.append(i)  # contains numbers

        else:
            a = stack.pop()  # if ch==operator then pop 2 numbers
            b = stack.pop()

            if i == '+':
                res = int(b) + int(a)  # old val <operator> recent value
            elif i == '-':
                res = int(b) - int(a)
            elif i == '*':
                res = int(b) * int(a)
            elif i == '%':
                res = int(b) % int(a)
            elif i == '/':
                res = int(b) / int(a)
            elif i == '**':
                res = int(b) ** int(a)

            stack.append(res)  # final result
    return (''.join(map(str, stack)))

# exprsn = "+ 9 * 12 6"
# print(evaluatePrefix(exprsn))


# ((2*3)+8)
# ab*c+
#23*8+
# x ^ y / (5 * z) + 10
# 1 ^ 2/ (5 * 6) + 10

class evaluate_prefix:
    def __init__(self):
        self.items=[]
        self.size=-1
    def isEmpty(self):
        if(self.size==-1):
            return True
        else:
            return False
    def push(self,item):
        self.items.append(item)
        self.size+=1
    def pop(self):
        if self.isEmpty():
            return 0
        else:
            self.size-=1
            return self.items.pop()
    def seek(self):
        if self.isEmpty():
            return False
        else:
            return self.items[self.size]
    def evalute(self,expr):
        for i in reversed(expr):
            if i in '0123456789':
                self.push(i)
            else:
                op1=self.pop()
                op2=self.pop()
                result=self.cal(op1,op2,i)
                self.push(result)
        return self.pop()
    def cal(self,op1,op2,i):
        if i is '*':
            return int(op1)*int(op2)
        elif i is '/':
            return int(op1)/int(op2)
        elif i is '+':
            return int(op1)+int(op2)
        elif i is '-':
            return int(op1)-int(op2)
        elif i is '^':
            return int(op1)^int(op2)
