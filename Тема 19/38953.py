def game(heap, moves, to):
    if heap >= 46:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    h = [game(heap + 1, moves + 1, to),
         game(heap * 3, moves + 1, to)]
    return any(h) if (moves + 1) % 2 == to % 2 else all(h)

print(min(s for s in range(1, 46) if not game(s, 0, 1) and game(s, 0, 2)))
print([s for s in range(1, 46) if not game(s, 0, 1) and game(s, 0, 3)])
print([s for s in range(1, 46) if not game(s, 0, 2) and game(s, 0, 4)])