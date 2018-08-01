def revdigitfunc(digit):
    revdigit = 0
    while digit:
        revdigit = revdigit*10 + digit % 10
        digit //= 10
    return revdigit


if __name__  == "__main__":
    print (revdigitfunc(123))