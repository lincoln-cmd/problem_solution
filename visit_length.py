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

#print(solution('ULURRDLLU'))
#print(solution('LULLLLLLU'))

###############################################################

'''
 통과

'''

def solution2(dirs):
    move = {'U' : (0, 1), 'D' : (0, -1), 'R' : (1, 0), 'L' : (-1, 0)}
    x, y = 0, 0 # 처음 위치(x0, y0)
    length = set()
    
    for i in dirs:
        x1 = move[i][0] # x방향의 거리 변화량(dx)
        y1 = move[i][1] # y방향의 거리 변화량(dy)
        x2 = x + x1 # x의 나중 위치 -> x = x0 + dx
        y2 = y + y1 # y의 나중 위치 -> y = y0 + dy
        if -5 <= x2 <= 5 and -5 <= y2 <= 5:
            length.add((x, y, x2, y2)) # 이동하는 경로
            #length.add((x2, y2, x, y)) # 되돌아가는 경로
            x, y = x2, y2 # 현재 위치를 리셋 해준다. -> x, y가 이동전 위치를 가지므로,
                          # 그 값을 이동 후 위치로 바꿔서 for문을 돌린다.
                          # if 조건문 안에 위치한 이유는 좌표 전체의 크기가 (5x5)크기 이기 때문에
                          # 그 값을 넘어갈 수 없기 때문.
    
    return len(length) // 2

#print(solution2('ULURRDLLU'))
#print(solution2('LULLLLLLU'))
    
    
####################################################################
'''
 실패
'''

def solution3(dirs):
    move = {'U' : (0, 1), 'D' : (0, -1), 'R' : (1, 0), 'L' : (-1, 0)}
    length = set()
    x, y = 0, 0
    
    for i in dirs:
        x1 = move[i][0]
        y1 = move[i][1]
        x2 = x + x1
        y2 = x + y1
        if -5 <= x2 <= 5 and -5 <= y2 <= 5:
            a = (x, y, x2, y2)
            b = (x2, y2, x, y)
            x, y = x2, y2
        else:
            x2 -= x1
            y2 -= y1
        
        if a not in length:
            length.add(a)
            length.add(b)
            
    return len(length) // 2
    
    
    
##################################################################
'''
 통과
'''


def solution4(dirs):
    command = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)}
    road = set()
    cur_x, cur_y = (0,0)
    
    for d in dirs:
        next_x, next_y = cur_x + command[d][0], cur_y + command[d][1]
        if -5<= next_x <=5 and -5<= next_y <=5:
            road.add((cur_x, cur_y, next_x, next_y))
            road.add((next_x, next_y, cur_x, cur_y))
            cur_x, cur_y = next_x, next_y

    return len(road) // 2
    
    
    
print(solution4('ULURRDLLU'))
print(solution4('LULLLLLLU'))    
    
    
    
    
    
    
    
    
    