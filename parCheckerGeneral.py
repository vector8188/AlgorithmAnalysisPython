from stack import Stack

def parCheckerGeneral(my_str):
    balanced = True
    index = 0
    s = Stack()
    while index < len(my_str) and balanced:
        c = my_str[index]
        if c in '({[':
            s.push(c)
        else:
            if s.isEmpty():
                balanced = False
            else:
                open_paren = s.pop()
                if not matches(open_paren,c):
                    balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(o,clo):
    opens = '({['
    closes = ')}]'
    return opens.index(o) == closes.index(clo)

if __name__ == "__main__":
    print(parCheckerGeneral('{{([][])}()}'))
    print(parCheckerGeneral('[{()]'))