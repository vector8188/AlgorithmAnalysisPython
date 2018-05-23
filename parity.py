def parity(x):
    result = 0
    while x:
        result = result ^ (x & 1)
        x = x//2
    return result


if __name__ == "__main__":
    parity(19)