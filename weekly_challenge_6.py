# -*- coding: utf-8 -*-
'''
 1차
 - weights의 순서대로 번호 부여 -> 몸무게, head2haed 대입 -> head2head에서 승률 계산 후 대임 -> 상위체급 승리 횟수 구해서 대입
 - sorted(key = lambda x : ())를 이용해서 조건 순서대로 정렬
'''

def solution(weights, head2head):
    answer = []
    
    list1 = []
    
    for i in range(len(weights)):
        list1.append([(i+1), weights[i], head2head[i]])
    
        
    
    for i in range(len(list1)):
        # 승률 계산
        total = list1[i][-1].count('W') + list1[i][-1].count('L')
        win = list1[i][-1].count('W')
        if total != 0:
            a = win / total * 100
        else:
            a = 0
        list1[i].append(a)
        b = 0
        for j in list1[i][-2]:
            if j == 'W':
                c = list1[i][-2].index(j)
                if list1[c][1] > list1[i][1]:
                    b += 1
        
        list1[i].append(b)
                
    list1 = sorted(list1, key = lambda x : (-x[3], -x[4], -x[1], x[0]))
    
    for i in list1:
        answer.append(i[0])
    
    print(list1)
    return answer

#print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"]))
#print(solution([145,92,86], ["NLW","WNL","LWN"]))
#print(solution([60,70,60], ["NNN","NNN","NNN"]))

#################################################################
'''
 2차
 - 1차에서 자신보다 체중이 많이나가는 복서를 이긴 횟수를 계산 하는 for문을 밖으로 뺌.
'''
def solution2(weights, head2head):
    answer = []
    
    list1 = []
    
    for i in range(len(weights)):
        list1.append([i+1, weights[i], head2head[i]])
        
    # 승률 계산
    for i in range(len(list1)):
        total = list1[i][-1].count('W') + list1[i][-1].count('L')
        win = list1[i][-1].count('W')
        if total != 0:
            a = (win / total) * 100
        else:
            a = 0
        list1[i].append(a)
        
    # 상위 체급 전적 계산
    for i in range(len(list1)):
        a = 0
        for j in range(len(list1[i][-2])):
            if list1[i][-2][j] == 'W':
                if list1[j][1] > list1[i][1]:
                    a += 1
        list1[i].append(a)
        
    list1 = sorted(list1, key = lambda x: (-x[3], -x[4], -x[1], x[0]))
        
    #print(list1)
    
    for i in list1:
        answer.append(i[0])
    
    return answer
    

print(solution2([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"]))
print(solution2([145,92,86], ["NLW","WNL","LWN"]))
print(solution2([60,70,60], ["NNN","NNN","NNN"]))