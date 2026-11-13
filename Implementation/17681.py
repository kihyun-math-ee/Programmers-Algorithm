def solution(n, arr1, arr2):
    arr1 = arr1[:]
    arr2 = arr2[:]
    target1 = [[False] * n for _ in range(n)]
    target2 = [[False] * n for _ in range(n)]
    answer = []
    for i in range(n):
        for j in range(n):
            if arr1[i] % 2 == 1:
                target1[i][j] = True
            arr1[i] //= 2
            if arr2[i] % 2 == 1:
                target2[i][j] = True
            arr2[i] //= 2

    for y in range(n):
        S = ""
        for x in range(n - 1, -1, -1):
            if target1[y][x] or target2[y][x]:
                S = S + "#"
            else:
                S = S + " "
        answer.append(S)
    return answer