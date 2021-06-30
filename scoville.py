'''
 1차 답안 : 정확성(76.2), 효율성(0)
 - 단순 while 반복문만 사용 -> 직관적 접근
'''


def solution(scoville, K):
    answer = 0
    while min(scoville) < K:
        scoville.sort()
        a = scoville.pop(0) + scoville.pop(0) * 2
        scoville.append(a)
        answer += 1
        if len(scoville) <= 1 and min(scoville) < K:
            return -1
    return answer


#########################################################

'''
 2차 답안 : 정확성(76.2), 효율성(0)
 - heapq + while 이용
'''


import heapq

def solution(scoville, K):
    answer = 0
    while min(scoville) < K:
        heapq.heapify(scoville)
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1
        if len(scoville) == 1 and min(scoville) < K:
            return -1
    
    return answer

#######################################################

'''
 3차 답안 : 정확성(76.2), 효율성(0)
 - 1, 2차 답안에서 정렬(sort, heapify)를 while문 안에 넣어서
 시간 복잡도 증가 -> heapify를 while문 밖으로 꺼냄
'''


import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while min(scoville) < K:
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1
        if len(scoville) == 1 and min(scoville) < K:
            return -1
    
    return answer




#######################################################
'''
 4차 답안
 
'''


import heapq as q


def solution(scoville, K):
    answer = 0
    if min(scoville) >= K:
        return 0
    q.heapify(scoville)
    while len(scoville) > 1:
        q.heappush(scoville, q.heappop(scoville) + q.heappop(scoville) * 2)
        answer += 1
        if min(scoville) >= K:
            return answer
    return -1


########################################################
'''
 정답 코드
 - 반복문 전 부분은 이전 코드들과 동일.
 while문 조건 자체를 인덱스 값으로 지정하여 K값과 비교 -> heapq.heapify가 정렬
 heapq.heappush를 if 조건문 안으로 넣어서 while문이 불필요하게 많이 실행되지 않도록 함.
 
'''


import heapq as q


def solution(scoville, K):
    answer = 0
    q.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) > 1:
            q.heappush(scoville, q.heappop(scoville) + q.heappop(scoville) * 2)
            answer += 1
        else: return -1
    return answer