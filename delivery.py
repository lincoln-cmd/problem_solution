# -*- coding: utf-8 -*-

# 다익스트라 알고리즘
# 참고 : https://blog.naver.com/PostView.naver?blogId=ndb796&logNo=221234424646&redirect=Dlog&widgetTypeCall=true&directAccess=false


'''
 1번 마을을 제외한 나머지 마을들을 딕셔너리의 key값으로 주고, 1번 마을에서 각 마을로
 이동하는데 걸리는 시간을 value값으로 준다. 만약 한 마을에서 다른 마을로 가는 경로가 여러개라면,
 더 작은 값을 넣어준다.
'''
def solution(N, road, K):
    answer = 0
    dic = dict()
    
    for i in range(2, N + 1):
        dic[i] = 0
        
    dic2 = dic.copy()
    
    
    a = 1
    while a <= N:
        for i in range(len(road)):
            b = road[i][0]
            c = road[i][1]
            if b == a:
                if dic[c] == 0:
                    dic[c] = road[i][2]
                else:
                    if dic[c] > road[i][2]:
                        dic[c] = road[i][2]
        a += 1
        
    d = 1
    for i in range(len(road)):
        for j in dic.keys():
            if d == road[i][0]:
                dic[j]
        
    

    return dic

print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))

#########################################################################

'''
 2차
'''












