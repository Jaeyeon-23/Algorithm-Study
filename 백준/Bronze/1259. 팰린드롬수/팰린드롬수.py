while True:
    num = input().strip()   #문자열 입력

    if num == "0":         
        break

    if num == num[::-1]:
        print("yes")
    else:
        print("no")