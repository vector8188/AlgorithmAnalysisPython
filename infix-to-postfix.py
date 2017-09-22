from stack import Stack
"""
Create an empty stack called opstack for keeping operators. Create an empty list for output.
Convert the input infix string to a list by using the string method split.
Scan the token list from left to right.
If the token is an operand, append it to the end of the output list.
If the token is a left parenthesis, push it on the opstack.
If the token is a right parenthesis, pop the opstack until the corresponding left parenthesis is removed. Append each operator to the end of the output list.
If the token is an operator, *, /, +, or -, push it on the opstack. However, first remove any operators already on the opstack that have higher or equal precedence and append them to the output list.
When the input expression has been completely processed, check the opstack. Any operators still on the stack can be removed and appended to the end of the output list.

"""
def infixToPostfix(infixexpr):
    # setting precidence for operator.
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["-"] = 2
    prec["+"] = 2
    prec["("] = 1
    opstack = Stack()
    output = []
    token_list = infixexpr.split(" ")
    for token in token_list:
        if token in 'ABCDEFGHIJKLMONPRSTUVWXYZ' or token in '0123456789':
            output.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            # I think this handles empty '( )'
            topToken = opstack.pop()
            while topToken != '(':
                # keep popping element and append them to the output list till you find closing (
                # keep popping and appending elements form '( + C B' till you encouter (.
                output.append(topToken)
                topToken = opstack.pop()
        else:
            while not opstack.isEmpty() and prec[opstack.peek()] >= prec[token]:
                output.append(opstack.pop())
            opstack.push(token)


    while not opstack.isEmpty():
        output.append(opstack.pop())
    return " ".join(output)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( )"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))








