# -*- coding: utf-8 -*-
'''
def solution(line):
    answer = []
    
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            if (line[i][0] * line[j][1] - line[i][1] * line[j][0]) != 0:
                # 교점 공식
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
    dot = ['' for j in range(a + -1 * c + 1)] # x좌표의 최대값과 최솟값의 길이에 0까지 더해줌.
    len_y = (b + -1 * d + 1) # 위와 같은 방법으로 y좌표의 길이를 구해줌.
    
    for i in range(len(answer)):
    answer[i][0] += (-1 * c)
    answer[i][1] += (-1 * d)
        
    for i in range(len(answer)):
        dot[answer[i]] = ('.' * len_y)
    #for i in range(len_y):
        
        
    
    #return dot
'''
#########################################################################################
'''
def solution2(line):
    INF = float('inf')
    mark, l = [], len(line)
    minx, maxx, miny, maxy = INF, -INF, INF, -INF
    for i in range(l):
        for j in range(i, l):
            if i == j: continue
            a, b, c, d, e, f = *line[i], *line[j]
            mo = a*d - b*c
            if mo == 0: continue
            x, y = (b*f - e*d) / mo, (e*c - a*f) / mo
            #if (not x.is_integer()) or (not y.is_integer()): continue
            if x-int(x) or y-int(y): continue    
            #if (b*f - e*d) % mo or (e*c - a*f) % mo: continue
            x, y = int(x), int(y)
            minx, maxx, miny, maxy = min(minx, x), max(maxx, x), min(miny, y), max(maxy, y)
            mark.append((x, y))
    res = [['.' for _ in range(maxx-minx + 1)] for _ in range(maxy - miny + 1)]
    for x, y in mark: res[maxy - y][x - minx] = '*'
    return [''.join(s) for s in res]



#(https://velog.io/@edhz8888/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9C%84%ED%81%B4%EB%A6%AC-%EC%B1%8C%EB%A6%B0%EC%A7%80-10%EC%A3%BC%EC%B0%A8-%EA%B5%90%EC%A0%90%EC%97%90-%EB%B3%84-%EB%A7%8C%EB%93%A4%EA%B8%B0)
def solution3(line):
    INF = float('inf')
    mark,L = [],len(line)
    minx,maxx,miny,maxy=INF,-INF,INF,-INF
    for i in range(L):
        for j in range(i,L):
            if i==j : continue
            A,B,E,C,D,F = *line[i],*line[j]
            mo = A*D-B*C
            if mo==0: continue
            x,y=(B*F-E*D)/mo,(E*C-A*F)/mo
            if x-int(x) or y-int(y) : continue
            x,y=int(x),int(y)
            minx,maxx,miny,maxy = min(minx,x),max(maxx,x),min(miny,y),max(maxy,y)
            mark.append((x,y))
    res=[['.' for _ in range(maxx-minx+1)] for _ in range(maxy-miny+1)]
    for x,y in mark : res[maxy-y][x-minx] = '*'
    return [''.join(s) for s in res]
'''

###############################################################################################
'''
def solution4(line):
    INF = float('inf')
    mark, l = [], len(line)
    minx, maxx, miny, maxy = INF, -INF, INF, -INF
    for i in range(l):
        for j in range(i, l):
            if i == j: continue
            a, b, c, d, e, f = *line[i], *line[j]
            mo = a*d - b*c
            if mo == 0: continue
            x, y = (b*f - e*d) / mo, (e*c - a*f) / mo
            if x - int(x) or y - int(y): continue
            x, y = int(x), int(y)
            minx, maxx, miny, maxy = min(minx, x), max(maxx, x), min(miny, y), max(maxy, y)
            mark.append((x, y))
    res = [['.' for _ in range(maxx - minx + 1)] for _ in range(maxy - miny + 1)]
    for x, y in mark: res[maxy - y][x - minx] = '*'
    return [''.join(s) for s in res]

'''

#################################################################################################

def check(line1, line2):
    a, b, e = line1
    c, d, f = line2
    mo = a*d - b*c
    
    if mo != 0 and (b*f - e*d) % mo == 0 and (e*c - a*f) % mo == 0:
        return [(b*f - e*d) // mo, -(e*c - a*f) // mo]
    return False


def solution5(line):
    answer = []
    result = []
    
    for i in range(len(line) - 1):
        for j in range(i+1, len(line)):
            a = check(line[i], line[j])
            
            if a:
                minx = min(minx, a[0]) if len(result) != 0 else a[0]
                maxx = max(maxx, a[0]) if len(result) != 0 else a[0]
                miny = min(miny, a[1]) if len(result) != 0 else a[1]
                maxy = max(maxy, a[1]) if len(result) != 0 else a[1]
                result.append(a)
                
    answer = [['.'] * (maxx - minx + 1) for _ in range(maxy - miny + 1)]
    
    for x, y in result:
        answer[y - miny][x - minx] = '*'
        
    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])
        
    return answer




print(solution5([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))



