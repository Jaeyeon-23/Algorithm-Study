N, M = map(int, input().split())
num = list(map(int,input().split()))
sum_card =[]

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            card =  num[i] + num[j] + num[k]
            if card <= M:
                sum_card.append(card)
print(max(sum_card))