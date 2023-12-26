def solution(tickets):
    tickets.sort(key = lambda x: (x[0], x[1]))

    def DFS(tickets, path):
        if len(tickets) == 0: # 티켓을 모두 소모했다면
            return path
        
        now = path[-1] # 현재 탐색할 공항
        idx = -1 # 현재 탐색할 인덱스

        # 탐색할 공항 위치 찾기
        for i in range(len(tickets)):
            if tickets[i][0] == now:
                idx = i
                break
        
        while tickets[idx][0] == now:
            # 가장 최근에 사용한 티켓을 삭제, 마지막으로 간 경로는 path에 저장
            next_path = DFS(tickets[:idx] + tickets[idx+1:], path+[tickets[idx][1]])

            if next_path != []:
                return next_path
            idx += 1
            
        return [] # path가 null이 되는 것 방지 (빈 리스트로 다시 시작)
    
    return DFS(tickets, ['ICN'])