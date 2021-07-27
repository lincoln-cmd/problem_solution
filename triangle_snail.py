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

print(solution2(4))



















