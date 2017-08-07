import types


def s(n):
    if n == 0:
        return n
    else:
        return n + s(n - 1)


print(s(10))


# no tail optimization for python

def s_tail(n, acc=0):
    if n == 0:
        return acc
    else:
        return s_tail(n - 1, acc + n)


print(s_tail(100))


# workaround using trampolining

def tramp(gen, *args, **kwargs):
    g = gen(*args, **kwargs)
    while isinstance(g, types.GeneratorType):
        g = next(g)
    return g


def f(n, curr=0, next=1):
    if n == 0:
        yield curr
    else:
        yield f(n - 1, next, curr + next)


print([tramp(f, i) for i in range(10)])
print(tramp(f, 100))
