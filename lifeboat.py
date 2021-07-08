'''
 1차 답안 : if 조건문에서 list인덱스의 범위 초과 -> people리스트가 1일때,
 people에서 마지막 요소가 pop되면 if문에서 에러 발생
'''

def solution(people, limit):
    answer = 0
    people.sort()
    list1 = []
    while people:
        list1.append(people.pop(0))
        if sum(list1) + people[0] >= limit and len(people) != 0:
            answer += 1
            list1.clear()
            
            
    return answer

#print(solution([70,50,80,50], 100))


############################################################


'''
 2차 답안 : if 조건문에서 만약 list1에 들어가있는 요소들의 합과 people의 처음 요소의 총 합이
 limit와 같은 때, people의 요소를 list1에 넣어주고 answer값을 1 올려줘야 하는데 이를 빼먹음.
'''
def solution2(people, limit):
    answer = 0
    people.sort()
    list1 = []
    
    while people:
        if list1 and len(people) > 0:
            if sum(list1) + people[0] >= limit:
                answer += 1
                list1.clear()
        list1.append(people.pop(0))
    return answer

print(solution2([70,80,50],100))


############################################################

'''
 3차 답안 : 정확성(20), 효율성(0)
 - sort를 해서 최소값부터 묶어서 접근 -> 만약 [20,30,70,80],100 인 경우,
 이 접근법을 이용하면 (20,30),(70),(80) 이 되서 결과값이 3이 됨.
 but, (20,80),(30,70)으로 묶으면 결과값이 2가 되고, 이가 최소값.
 
'''

def solution(people, limit):
    answer = 0
    people.sort()
    list1 = []
    
    while people:
        if list1 and len(people) > 0:
            if sum(list1) + people[0] > limit:
                answer += 1
                list1.clear()
            elif sum(list1) + people[0] == limit:
                list1.append(people.pop(0))
                answer += 1
                list1.clear()
        
            
        list1.append(people.pop(0))
    
    if list:
        answer += 1
    return answer

##########################################################

'''
 4차 답안 : 정확성(20), 효율성(0)
 - 위 코드에서 sort를 sort(reverse = True)로 주고 무거운 사람부터 list1에 대입해서
 조건문 순회, but 실패
'''

def solution(people, limit):
    answer = 0
    list1 = []
    people.sort(reverse = True)
    
    
    while people:
        list1.append(people.pop(0))
        
        if list1 and len(people) > 0:
            for i in people[::-1]:
                if sum(list1) + i > limit:
                    answer += 1
                    list1.clear()
                elif sum(list1) + i == limit:
                    list1.append(people.pop())
                    answer += 1
                    list1.clear()
                    break
    
    if list1:
        answer += 1
        
                    
    
    return answer

##########################################################
'''
 정답
 - 인터넷 참조
'''

def solution(people, limit):
    answer = 0
    people.sort()
    a, b = 0, len(people) - 1
    
    while a <= b:
        answer += 1
        if people[a] + people[b] <= limit:
            a += 1
        b -= 1
    return answer

# 80,70,50,50
# 50,50,70,80