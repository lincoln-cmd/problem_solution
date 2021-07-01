'''
 1차 답안 : 정확성(93.8)
'''

def solution(citations):
    citations.sort(reverse = True)
    print(citations)
    for i in range(len(citations)):
        if citations[i] < i+1:
            return i
        
        
'''
 정답
 - 1) 만약 발표된 논문이 1개이고, 이 논문이 인용된 횟수가 1회 이상이면 1을 반환해야 한다.
    e.g) [3] -> return 1
 2) 만약 발표된 논문 전체의 수보다 각각의 논문이 인용된 횟수가 더 많다면 발표된 논문의 수를 반환해야 한다.
    e.g) [10,20,30] -> return 3
'''

def solution(citations):
    citations.sort(reverse = True)
    print(citations)
    if len(citations) == 1 and citations[0] != 0:
        return 1
    for i in range(len(citations)):
        if citations[i] < i+1:
            return i
    return len(citations)