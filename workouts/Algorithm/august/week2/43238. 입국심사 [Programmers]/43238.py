def solution(n, times):
    answer = 0
    start, end = min(times), max(times)*n
    
    while start <= end:
        mid = (start + end) // 2
        temp = 0
        for i in times:
            temp += (mid // i) # 시간 안에 i가 계산 가능한 최대인원
            if temp >= n: # 모두 검사되면  
                break # 종료
        if temp < n: # 모자랄 때는
            start = mid + 1 # 늘리고
        else: # 많으면
            answer = mid # 업데이트하고
            end = mid - 1 # 줄이기 
    return answer