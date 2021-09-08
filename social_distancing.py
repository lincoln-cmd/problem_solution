# -*- coding: utf-8 -*-
'''
 - 재귀 함수, 다중 for문
 - p와 x의 인덱스 위치만 이용
'''

'''
 - 1차: 재귀함수 이용, 노가다 코딩
 정확성 : 81.3 / 100
'''
def check(s):
    list1 = s
    
    #for i in range(len(s)):
     #   list1[i].append(s)
    print(list1)
        
    for i in range(1, 4):
        for j in range(1, 4):
            if list1[i][j] == 'P':
                if list1[i-1][j] == 'P' or list1[i][j-1] == 'P' or list1[i][j+1] == 'P' or list1[i+1][j] == 'P':
                    return False
                elif list1[i-1][j-1] == 'P' and (list1[i-1][j] != 'X' or
                                                 list1[i][j-1] != 'X'):
                    return False
                elif list1[i-1][j+1] == 'P' and (list1[i-1][j] != 'X' or
                                                 list1[i][j+1] != 'X'):
                    return False
                elif list1[i+1][j-1] == 'P' and (list1[i][j-1] != 'X' or
                                                 list1[i][j+1] != 'X'):
                    return False
                elif list1[i+1][j+1] == 'P' and (list1[i][j+1] != 'X' or
                                                 list1[i+1][j] != 'X'):
                    return False
    
    for i in range(4):
        x = i
        for j in range(4):
            y = j
            if list1[i][j] == 'P':
                if 0 <= x <= 3 and 0 <= y <= 3:
                    if list1[i+1][j] == 'P' or list1[i][j+1] == 'P':
                        return False
                #if 0 <= x <= 2 and 0 <= y <= 2:
                 #   if list1[i+2][j] == 'P' or list1[i][j+2] == 'P':
                  #      return False
    
    return True
                
                


def solution(places):
    answer = []
    
    
    
    for i in places:
        if check(i) == True:
            answer.append(1)
        else:
            answer.append(0)

    return answer

'''
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
'''
###############################################################
'''
 - 2차
 너비 우선 탐색(BFS) 사용
'''
from collections import deque
def 

def solution2(places):
    answer = []
    
    return answer



