def g(heap, moves, to):
    if heap >= 65:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [g(heap + 1, moves + 1, to),
         g(heap * 2, moves + 1, to)]
    return any(h)

def f(heap, moves, to):
    if heap >= 65:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [f(heap + 1, moves + 1, to),
         f(heap * 2, moves + 1, to)]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)

print(min(s for s in range(1, 65) if not g(s, 0, 1) and g(s, 0, 2)))
print([s for s in range(1, 65) if not f(s, 0, 1) and not f(s, 0, 2) and f(s, 0 ,3)])
print(min(s for s in range(1, 65) if not f(s, 0, 1) and not f(s, 0, 2) and not f(s, 0, 3) and f(s, 0, 4)))