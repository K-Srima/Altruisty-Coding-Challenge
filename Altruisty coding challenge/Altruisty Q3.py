from collections import deque
def bfs(n, m):
    result = []
    queue = deque(range(10))  
    while queue:
        num = queue.popleft()
        if num > m:
            continue
        if num >= n:
            result.append(num)      
        last_digit = num % 10
        if last_digit > 0:
            next_num = num * 10 + (last_digit - 1)
            if next_num <= m:
                queue.append(next_num)
        if last_digit < 9:
            next_num = num * 10 + (last_digit + 1)
            if next_num <= m:
                queue.append(next_num)
    return sorted(result)
n, m = 100, 500
print(bfs(n, m)) 
