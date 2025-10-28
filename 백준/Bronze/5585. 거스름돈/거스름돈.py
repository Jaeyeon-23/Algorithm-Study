price = int(input())

count = 0
n= 1000-price
money = [500,100,50,10,5,1]

for i in money:
    count+=n//i
    n%=i

print(count)