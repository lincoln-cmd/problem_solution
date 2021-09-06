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
        if list1[i][-1].count('W') + list1[i][-1].count('L') != 0:
            a = (list1[i][-1].count('W') / (list1[i][-1].count('W') + list1[i][-1].count('L'))) * 100
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

print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"]))
print(solution([145,92,86], ["NLW","WNL","LWN"]))
print(solution([60,70,60], ["NNN","NNN","NNN"]))