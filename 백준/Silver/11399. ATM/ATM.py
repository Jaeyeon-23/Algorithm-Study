N = int(input())
num = list(map(int, input().split()))
num.sort()
cnt=0
min=0
for i in num:
    cnt = i + cnt
    min += cnt

print(min)