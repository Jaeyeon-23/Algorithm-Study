def count(array, target):
    start, end = 0, len(array) - 1
    pos = -1 #타겟보다 작은거 끝나는 인덱스 저장

    while start <= end:
        mid = (start + end) // 2

        if array[mid] < target:
            pos = mid
            start = mid + 1
        else:
            end = mid - 1
    return pos + 1

T = int(input())
for _ in range(T):
    N,M = map(int, input().split())
    aNum = list(map(int, input().split()))
    bNum = list(map(int, input().split()))  

    bNum.sort()
    cnt = 0  
    for i in aNum:
        cnt += count(bNum, i)

    print(cnt)