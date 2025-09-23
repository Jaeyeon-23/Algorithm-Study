T = int(input()) 

for _ in range(T):
    n, k = input().split()
    n = int(n)
    arr = list(k)
    string = []

    for i in range(len(arr)):
        for _ in range(n):
            string.append(arr[i])

    print(''.join(string))