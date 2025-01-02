def g(heap1, heap2, moves, to):
    if (heap1 + heap2) <= 40:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [g(heap1 - 1, heap2, moves + 1, to),
         g(heap1, heap2 - 1, moves + 1, to),
         g(heap1 // 2 + heap1 % 2, heap2, moves + 1, to),
         g(heap1, heap2 // 2 + heap2 % 2, moves + 1, to)]
    return any(h)

def f(heap1, heap2, moves, to):
    if (heap1 + heap2) <= 40:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [f(heap1 - 1, heap2, moves + 1, to),
         f(heap1, heap2 - 1, moves + 1, to),
         f(heap1 // 2 + heap1 % 2, heap2, moves + 1, to),
         f(heap1, heap2 // 2 + heap2 % 2, moves + 1, to)]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)

print(max([s for s in range(100, 20, -1) if not g(20, s, 0, 1) and g(20, s, 0, 2)]))
print([s for s in range(100, 20, -1) if not f(20, s, 0, 1) and f(20, s, 0, 3)])
print(max(s for s in range(21, 100) if not f(20, s, 0, 1) and not f(20, s, 0, 3) and f(20, s, 0, 4)))