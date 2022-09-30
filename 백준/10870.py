n = int(input())

p = [0, 1]
for i in range(n-1):
    p.append(p[i] + p[i+1])

print(p[n])