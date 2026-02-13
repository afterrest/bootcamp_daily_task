from collections import deque

def check_connect(word1, word2):
    length = len(word1)
    if length != len(word2):
        return False
    count = 0
    for i in range(length):
        if word1[i] != word2[i]:
            count += 1
        if count > 1:
            return False
    if count == 1:
        return True
    else: # 같은 단어
        return False
def mapping(words):
    length = len(words)
    edges = [[] for _ in range(length)]
    for i in range(length):
        for j in range(i+1, length):
            if check_connect(words[i], words[j]):
                edges[i].append(j)
                edges[j].append(i)
    return edges
def bfs(start, end, network):
    queue = deque([start])
    visited = set([start])
    steps = 0

    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            current = queue.popleft()
            if current == end:
                return steps
            for neighbor in network[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        steps+=1
    return 0

def solution(begin, target, words):
    if target not in words:
        return 0
    
    if begin not in words:
        words.append(begin)
        
    network = mapping(words)
    begin_index = words.index(begin)
    target_index = words.index(target)

    answer = bfs(begin_index, target_index, network)
            
        
    return answer
