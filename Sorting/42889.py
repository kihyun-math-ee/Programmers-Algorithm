def solution(N, stages):
    answer = []
    failure = []
    total_players = len(stages)
    
    for stage in range(1, N + 1):
        if total_players == 0:
            failure.append((0, stage))
            continue
            
        not_cleared = stages.count(stage)
        failure.append((not_cleared / total_players, stage))
        total_players -= not_cleared
        
    failure.sort(key=lambda x: (-x[0], x[1]))
    
    for rate, stage in failure:
        answer.append(stage)
        
    return answer