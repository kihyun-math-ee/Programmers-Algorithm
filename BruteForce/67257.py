from itertools import permutations

def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return  a * b

def solution(expression):
    target = []
    num = ""
    for ch in expression:
        if ch in "+-*":
            target.append(int(num))
            target.append(ch)
            num = ""
        else:
            num += ch
    target.append(int(num))

    operators = ["+", "-", "*"]
    priority_cases = list(permutations(operators, 3))
    max_reward = 0

    for priority in priority_cases:
        temp = target[:]

        for op in priority:
            while op in temp:
                idx = temp.index(op)
                result = calc(temp[idx - 1], temp[idx + 1], op)
                temp[idx - 1 : idx + 2] = [result]
        max_reward = max(max_reward, abs(temp[0]))

    return max_reward