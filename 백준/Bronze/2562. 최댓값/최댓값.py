arr = []
for i in range(9):
    n = int(input())
    arr.append(n)

m = max(arr)
idx = arr.index(m)

print(m)
print(idx+1)