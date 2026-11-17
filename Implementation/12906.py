def solution(arr):
    answer = []
    temp = -1
    for num in arr:
        if temp != num:
            temp = num
            if answer:
                if answer[-1] != temp:
                    answer.append(temp)
            else:
                answer.append(temp)
    return answer
