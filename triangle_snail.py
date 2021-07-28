#-*-coding:utf-8-*-

'''
 1차
 - 모든 값들을 직접 대입. -> 방향을 바꾸는 횟수 = (n - 1)번. 즉, 변을 따라 이동하는 총 횟수 = n
 주어진 n의 값과 같은 for문이 필요.
 ex) n = 4, for문 4개 필요, n = 5, for문 5개 필요...
 -> n의 값이 변할 때마다 함수 내 반복문 자체의 필요 개수가 달라짐.
  -> reusable한 함수 구현 불가.
'''

def solution(n):
    a = 0
    for i in range(n+1):
        a += i
        
    
    list1 =[[] for i in range(n)]
    
    list1[0].append(1)
    
    for i in range(1, n-1):
        list1[i].append(i+1)
    
    for i in range(n, 2 * n):
        list1[-1].append(i)
        
        
    #for i in range(2 * n , 2*n + n-2):
     #   list1[i].append(i)
    
    return list1

#print(solution(6))


########################################################
'''
 2차
 - 변을 따라 이동하는 총 횟수 : n번, 방향을 바꾸는 횟수 : n - 1번,
 각각의 변을 따라 이동하는 횟수마다 리스트에 채워야 하는 숫자의 갯수 : n - i개(i : 0부터 시작하는 횟수)
 즉, 총 넣어햐 하는 숫자의 개수와 각 이동 횟수마다 리스트에 넣어야 하는 숫자의 개수는 동일.
 total number = the number of number which has to insert in list = Σ(i = 0, n)(n - i)
 
'''
import numpy as np

def solution2(n):
    count = 0
    a = 0
    for i in range(n + 1):
        a += i

    list1 = np.zeros((n, n)).reshape((n, n))
    
    #for i in range(n):
     #   list1[i].append(i)
    
    #while True:
        
    return list1

#print(solution2(4))


##########################################################
'''
 3차. 인터넷 참조
 - 삼각형을 좌표로 변환하고 상, 하, 우로 이동하는 함수로 구현
'''

def solution3(n):
    list1 = [[0 for i in range(1, j +1)] for j in range(1, n + 1)]
    x, y = 0, -1
    print(list1)

    num = 1
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                y -= 1
            elif i % 3 == 1:
                x += 1
            else:
                x -= 1
                y += 1
            list1[x][y] = num
            num += 1
    
    return sum(list1, [])

#print(solution3(4))


#########################################################
'''
 4차
 - 3차의 문제점 : 삼각형모양을 좌표화 해서 구현할 때, 수학적 2차원 직교 좌표계에 적용.
  -> 따라서 이동시, 상 : y += 1, 하 : y -= 1, 좌 : x -= 1, 우 : x += 1
  와 같은 방식으로 구현함.
  -> 리스트에서는 위에서 아래로 내려올때 값이 1씩 증가함.
'''

def solution4(n):
    list1 = [[0 for i in range(1, j + 1)] for j in range(1, n + 1)]
    print(list1)
    x, y = -1, 0 # 처음에는 (0, 0)에서 아래로 이동하므로 x = -1
                 # for문을 처음 돌때 아래로 내려가므로 x += 1이 됨.
                 # 이때, list1삼각 배열을 좌표화 했을 때, 현 위치의 x값이 0.
                 # 2차 배열로 보면, x : 행, y : 열
    
    num = 1 # 표기되는 숫자의 처음이 1부터 시작.
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0: # 아래
                x += 1
            elif i % 3 == 1: # 오른쪽
                y += 1
            else: # 왼쪽위 대각선
                x -= 1
                y -= 1
            print(x, y)
            list1[x][y] = num # 두번 째 for문에서 조건문을 충족해서 얻어지는 x, y값이 list1의 위치 좌표
            num += 1 # 각 칸으로 이동 시 마다 숫자가 1씩 증가
            
    return sum(list1, [])


print(solution4(4))









