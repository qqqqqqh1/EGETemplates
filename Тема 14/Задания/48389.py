results = []
for x in range(7):
    for y in range(7):
        res = int(f'{y}{x}320', 7) + int(f'1{x}3{y}3', 9)
        if res % 181 == 0:
            results.append(res)
print(min(results) // 181)