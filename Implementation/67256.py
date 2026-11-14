def solution(numbers, hand):
    dict_coordinate = {
        1: (1, 1), 2: (1, 2), 3: (1, 3),
        4: (2, 1), 5: (2, 2), 6: (2, 3),
        7: (3, 1), 8: (3, 2), 9: (3, 3),
        '*': (4, 1), 0: (4, 2), '#': (4, 3)
    }

    current_L = dict_coordinate['*']
    current_R = dict_coordinate['#']
    answer = ''

    for num in numbers:
        target = dict_coordinate[num]

        if num in [1, 4, 7]:
            answer += 'L'
            current_L = target

        elif num in [3, 6, 9]:
            answer += 'R'
            current_R = target

        else:
            dist_L = abs(target[0] - current_L[0]) + abs(target[1] - current_L[1])
            dist_R = abs(target[0] - current_R[0]) + abs(target[1] - current_R[1])

            if dist_L < dist_R:
                answer += 'L'
                current_L = target
            elif dist_L > dist_R:
                answer += 'R'
                current_R = target
            else:
                if hand == 'left':
                    answer += 'L'
                    current_L = target
                else:
                    answer += 'R'
                    current_R = target

    return answer