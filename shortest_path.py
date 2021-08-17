# -*- coding: utf-8 -*-
'''
 1차
 - bfs(너비우선탐색) 없이 while문으로 경로 하나씩 탐색
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

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))

'''
 - 2차
 
'''
