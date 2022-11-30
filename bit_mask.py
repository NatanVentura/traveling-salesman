def put(x,i):
    return x | (1 << i)
def has(x,i):
    return x & 1<<i
def remove(x,i):
    return x ^ (1 << i)