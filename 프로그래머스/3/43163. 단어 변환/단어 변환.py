from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    visited = [0] * len(words)
    
    while q:
        current_word, step = q.popleft()
        
        if current_word == target:
            return step
        
        for i in range(len(words)):
            if not visited[i]:
                diff = sum(1 for a, b in zip(current_word, words[i]) if a!=b)
                if diff == 1:
                    visited[i] = 1
                    q.append((words[i], step+1))
    return 0