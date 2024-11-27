def g(heap, moves, to):
    if heap >= 38:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [g(heap + 1, moves + 1, to),
         g(heap * 3, moves + 1, to)]
    return any(h)

def g2(heap, moves, to):
    if heap >= 38:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [g2(heap + 1, moves + 1, to),
         g2(heap * 3, moves + 1, to)]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)

print(min(s for s in range(1, 38) if g(s, 0, 2)))
print(*(s for s in range(1, 38) if not g2(s, 0, 1) and g2(s, 0, 3)))
print(min(s for s in range(1, 38) if (g2(s, 0 ,2) or g2(s, 0, 4) and not g2(s, 0, 2))))