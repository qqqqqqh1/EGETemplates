f = dict()
f[0] = 1
f[1] = 1
for i in range(2, 2025):
    f[i] = 2 * i * f[i - 1]
print((f[2024] - 3 * f[2023]) / f[2022])
