from stack import Stack

def parChecker(par_string):
    """
    This problem takes advantage of fact that any balanced parentheis string will have
    equal number of open '(' and close ')' parenthesis and in correct order. 
    """
    balanced = True
    length_of_par_string = len(par_string)
    i = 0
    s = Stack()
    while i < length_of_par_string and balanced:
        "if '(' is found, '(' pushed to stack."
        if par_string[i] == '(':
            s.push(par_string[i])
        else:
            """
            look for the condition where stack is empty, 
            if stack is empty before the end of iteration which means
            you had unbalanced stack before end of While loop.
            unbalanced stack will execute statement below.
            """
            if s.isEmpty():
                balanced = False
            else:
                """
                if stack instance is not empty we have to pop 
                ')'
                """
                s.pop()
        i = i + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

if __name__ == "__main__":
    print(parChecker('((()))'))
    print(parChecker('(()'))
