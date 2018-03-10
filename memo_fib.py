mem = {0:1, 1:1}
def f(n):
    if n == 0 or n == 1:
        return mem[n]
    else:
        if n not in mem.keys():
            mem[n-2] = f(n-2)
            mem[n-1] = f(n-1)
            mem[n] = mem[n-2]+mem[n-1]
    return mem[n]

print (f(500))
