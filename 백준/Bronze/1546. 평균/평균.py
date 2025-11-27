N = int(input())

scores = list(map(int, input().split()))

M = max(scores)

total = 0
for s in scores:
    total += (s / M * 100)

print(total / N)