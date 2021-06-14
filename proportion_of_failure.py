import operator

def solution(N, stages):
    # 단계별 성공한 유저 수
    clear = {}
    for i in range(1, N+1):
        clear[i] = 0
    for i in stages:
        for j in range(1, i):
            clear[j] += 1
            
            
    # 단계별 도달 유저 수
    reach = clear.copy()
    for i in stages:
        if i <= N:
            reach[i] += 1
            
    # 성공률을 구하고, 실패율을 구함, (1- 성공률) = 실패율
    rate = clear.copy()
    for i, j in reach.items():
        rate[i] = 1 - (clear[i] / j)
    dic = sorted(rate.items(), key = operator.itemgetter(1), reverse = True)
        
    list1 = [dic[i][0] for i in range(len(dic))]
    
    print(clear)
    print(reach)
    print(list1)
    
    return list1

##############################################################


import operator

def solution2(N, stages):
    clear, reach, rate = {}, {}, {}
    
    for i in range(1, N+1):
        clear[i] = 0
        reach[i] = 0
        rate[i] = 0
    
    for i in stages:
        for j in range(1, i):
            clear[j] += 1
            reach[j] += 1
        if i <= N:
            reach[i] += 1
    
    for i in rate:
        rate[i] = (reach[i] - clear[i]) / reach[i]
    
    dic = [[sorted(rate.items(), key = operator.itemgetter(1), reverse = True)][0][i][0] for i in range(N)]
        
    print(clear)
    print(reach)
    print(rate)
    print(dic)
    print(len(dic))
    
print(solution2(5, [2, 1, 2, 6, 2, 4, 3, 3]))
    