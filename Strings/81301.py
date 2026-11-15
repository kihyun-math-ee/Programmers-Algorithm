def solution(s):
    answer = ''
    dict_num = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    target = ''
    
    for ch in s:
        if ch.isdigit():
            answer += ch
        else:
            target += ch
            
            if target in dict_num:
                answer += dict_num[target]
                target = ''
                
    return int(answer)