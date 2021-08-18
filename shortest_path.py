# -*- coding: utf-8 -*-
'''
 1차
 - bfs(너비우선탐색) 없이, while문으로 경로 하나씩 탐색
'''
def solution(maps):
    answer = 0
    
    rows = len(maps)
    col = len(maps[0])
    path = maps.count(1)
    length = 0
    
    i, j = 0, 0
    while i <= rows and j <= col:
        if maps[i + 1][j] == 1:
            i += 1
            length += 1
        elif maps[i + 1][j + 1] == 1:
            i +=1
            j += 1
            length += 1
        elif maps[i - 1][j] == 1:
            i -= 1
            length += 1
        else:
            j -= 1
            length += 1
            
        if i == rows and j == col:
            return length
        else:
            return -1

#print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
#print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))

###################################################################################

'''
 - 2차
 
'''
def solution2(maps):
    answer = 0
    
    row = len(maps)
    col = len(maps[0])
    
    maps[-1][-1] = 2
    a, b = 0, 0
    path = 0
    
    for i in range(len(maps) - 1):
        for j in range(len(maps[0]) - 1):
            if maps[a + 1][b] == 1:
                a += 1
                path += 1
            elif maps[a][b + 1] == 1:
                b += 1
                path += 1
            elif maps[a - 1][b] == 1:
                a -= 1
                path += 1
            elif maps[a][b - 1] == 1:
                b -= 1
                path += 1
        if maps[a][b] == 2:
            return path
    
    return -1

#print(solution2([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))


###################################################################################

'''
 - 3차
 bfs이용.
 인터넷 해설 참조
'''

from collections import deque

def solution3(maps):
    dd = [[1,0], [0,1],[-1,0],[0,-1]]
    
    y = len(maps)
    x = len(maps[0])
    
    check = [[-1 for _ in range(x)] for _ in range(y)]
    check[0][0] = 1
    
    queue = []
    queue.append([0, 0])
    
    while queue:
        b, a = queue.pop(0)
        for i in range(4):
            dy = b + dd[i][0]
            dx = a + dd[i][1]
            
            if -1 < dx < x and -1 < dy < y:
                if maps[dy][dx] == 1:
                    if check[dy][dx] == -1:
                        check[dy][dx] = check[b][a] + 1
                        queue.append([dy, dx])

    return check[-1][-1]

print(solution3([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution3([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))