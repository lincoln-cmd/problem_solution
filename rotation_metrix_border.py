# -*- coding: utf-8 -*-

'''
 1차
 - numpy를 이용해서 2차원 배열 생성
'''
import numpy as np

def solution(rows, columns, queries):
    answer = []
    arr = np.arange(1, rows*columns + 1).reshape((rows, columns))
    
    #for i in queries:
        
    
    
    return arr

#print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))



#################################################################

'''
 2차
 - 1차원 2중 리스트 배열 생성해서 접근
'''

def solution2(rows, columns, queries):
    answer = []
    # 행렬 생성
    arr = [[0 for i in range(1, columns + 1)] for j in range(rows)]
    
    a = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = a
            a += 1
       
    # queries에 주어진 좌표값으로 회전할 범위 설정
    # -> for문 안에 총 4개의 for문이 만들어 져야 함. -> 회전이 사각형 형태에서 일어남으로, 각 변마다 범위를 따로 설정 해 줘야 함.
    for x1, y1, x2, y2 in queries:
        answer2 = []
        a = arr[x1-1][y1-1]
        
        # 왼쪽
        for i in range(x1 - 1, x2 - 1):
            temp = arr[i+1][y1 - 1]
            arr[i][y1 - 1] = temp
            answer2.append(temp)
        # 아래
        for i in range(y1 - 1, y2 - 1):
            temp = arr[x2 - 1][i+1]
            arr[x2 - 1][i] = temp
            answer2.append(temp)
        # 오른쪽
        for i in range(x2 - 1, x1 - 1, -1):
            temp = arr[i-1][y2 - 1]
            arr[i][y2 - 1] = temp
            answer2.append(temp)
        # 위
        for i in range(y2 - 1, y1 - 1, -1): # range범위에서 역순으로 i에 대입 -> 정순으로 하면 for문을 돌면서 i가 커질 때, temp변수에 입력되는 인자가 다음 값이랑 같아짐.
            temp = arr[x1 - 1][i-1]
            arr[x1 - 1][i] = temp
            answer2.append(temp)
        
        arr[x1-1][y1] = a
        answer2.append(a)
        
        
        answer.append(min(answer2))
    
        
    
        
    
    return answer

print(solution2(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution2(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))