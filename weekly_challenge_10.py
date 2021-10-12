# -*- coding: utf-8 -*-
def solution(line):
    answer = []
    
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            if (line[i][0] * line[j][1] - line[i][1] * line[j][0]) != 0:
                x = (line[i][1] * line[j][2] - line[i][2] * line[j][1]) / (line[i][0] * line[j][1] - line[i][1] * line[j][0])
                y = (line[i][2] * line[j][0] - line[i][0] * line[j][2]) / (line[i][0] * line[j][1] - line[i][1] * line[j][0])
                if x % 1 == 0 and y % 1 == 0:
                    answer.append([int(x), int(y)])
                    
    a, b, c, d = 0, 0, 0, 0
    
    for i in range(len(answer)):
        if answer[i][0] > a: # +x 최대 길이
            a = answer[i][0]
        if answer[i][1] > b: # +y 최대 길이
            b = answer[i][1]
        if answer[i][0] < c: # -x 최대 길이
            c = answer[i][0]
        if answer[i][1] < d: # -y 최대 길이
            d = answer[i][1]
            
    print(answer)
    dot = [[] for j in range(a + -1 * c)]
    

    for i in range(len(answer)):
        x = answer[i][0]
        y = answer[i][1]
#        dot[i] = '.' 
        
    
    return dot

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))