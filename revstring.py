from stack import Stack

def revstring(mystr):
    s = Stack()
    for i in mystr:
        s.push(i)
    x = ""
    while True:
        try:
            x+=s.pop()
        except IndexError:
            break
    return x

if __name__ == "__main__":
    string_to_be_reversed = "123ABC"
    print (revstring(string_to_be_reversed))
    