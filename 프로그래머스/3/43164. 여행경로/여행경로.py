
def solution(tickets):
    tickets_dict = {}
    visited = [False] * len(tickets)
    for i in range (len(tickets)):
        start = tickets[i][0]
        end = tickets[i][1]
        
        if start not in tickets_dict:
            tickets_dict[start] =[(end, i)]
        else :
            tickets_dict[start].append((end, i))
            
    for start in tickets_dict:
        tickets_dict[start].sort()
    
    answer = []

    def dfs(current, path):
        if len(path) == len(tickets) + 1:
            answer.append(path[:])
            return True
        
        if current not in tickets_dict:
            return False
        
        for next_city, ticket_idx in tickets_dict[current]:
            if not visited[ticket_idx]:
                visited[ticket_idx] = True
                path.append(next_city)
                
                if dfs(next_city, path):
                    return True
                
                visited[ticket_idx] = False
                path.pop()
        return False

    
    dfs("ICN", ["ICN"])
        
    return answer[0] if answer else []