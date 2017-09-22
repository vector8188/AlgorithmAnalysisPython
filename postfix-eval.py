from stack import Stack

def postfixEval(postfixExpr):
	operandStack = Stack()
	token_list = postfixExpr.split()
	for token in token_list:
		if token in '0123456789':
			operandStack.push(int(token))
		if token in '*/-+':
			exprA = operandStack.pop()
			exprB = operandStack.pop()
			operandStack.push(doMath(token, exprA, exprB))
return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))