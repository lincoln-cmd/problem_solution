# -*- coding: utf-8 -*-

def solution(scores):
    answer = ''
    
    list1 = [[] for _ in range(len(scores))]
    
    for i in range(len(scores)):
        for j in range(len(scores)):
            list1[i].append(scores[j][i])
        if list1[i].count(list1[i][i]) == 1:
            if list1[i][i] == max(list1[i]) or list1[i][i] == min(list1[i]):
                del list1[i][i]
            
    
    for i in range(len(list1)):
        list1[i] = sum(list1[i]) / len(list1[i])
            
    for i in list1:
        if i >= 90:
            answer += 'A'
        elif 90 > i >= 80:
            answer += 'B'
        elif 80 > i >= 70:
            answer += 'C'
        elif 70 > i >= 50:
            answer += 'D'
        else:
            answer += 'F'
    
    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))

