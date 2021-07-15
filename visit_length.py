'''
 1차 : 런타임 에러
 - numpy를 이용해서 좌표를 2차 행렬로 만듬 -> 이동한 지점을 좌표에 표기하여,
 처음 이동한 곳들을 구함 -> 총 갯수를 세서 반환
 - 이동 좌표가 아닌 경로를 구해야 함.
 - 코드가 너무 복잡함.
'''

import numpy as np

def solution(dirs):
    answer = 0
    
    list1 = np.zeros(11*11, dtype = int).reshape(11, 11)
    list1[5][5] = 2
    a = np.where(list1 == 2)[0][0] # row
    b = np.where(list1 == 2)[0][0] # column
    
    for i in dirs:
        if i == 'U' and a != 0:
            if a != 0:
                list1[a][b] = 1
                a -= 1
                list1[a][b] = 1
            else:
                pass
        elif i == 'D':
            if a != 10:
                list1[a][b] = 1
                a += 1
                list1[a][b] = 1
            else:
                pass
        elif i == 'L':
            if b != 0:
                list1[a][b] = 1
                b -= 1
                list1[a][b] = 1
            else:
                pass
        elif i == 'R':
            if b != 10:
                list1[a][b] = 1
                b += 1
                list1[a][b] = 1
            else:
                pass
        
    
    count = np.unique(list1, return_counts = True)[1][1]
    #print(int(count))
    #print(list1)
    
    return int(count)

print(solution('ULURRDLLU'))
print(solution('LULLLLLLU'))

###############################################################
