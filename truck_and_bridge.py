'''
 1차 : IndexError: list index out of range
'''

def solution(bridge_length, weight, truck_weights):
    a = 0
    list1 = [] # 다리를 건너고 있는 트럭 리스트
    while True:
        # 1. 다리를 건너는 트럭의 전체 무게가 weight보다 작으면 대기 중인 트럭 중 첫번째 트럭의 무게를 확인
        # 2. 확인한 트럭과 다리를 건너고 있는 트럭의 총 무게를 계산
        # 3. bridge_length만큼 시간에 더해주고 처음 건너던 트럭을 pop
        # 4. 반복
        if len(truck_weights) != 0:
            list1.append(truck_weights.pop(0)) # 트럭이 다리를 건너기 시작
            a += 1 # 시간 + 1
            if sum(list1) + truck_weights[0] <= weight and len(list1) + 1 < bridge_length:
                list1.append(truck_weights.pop(0))
                a += 1
                a += bridge_length
                list1.pop(0)
                a += 1
            elif sum(list1) + truck_weights[0] > weight:
                    a += bridge_length
                    list1.pop(0)
                    a += 1
        else:
            a += bridge_length
            return a + 1

    return a + 1

###################################################################

'''
 정답
'''
def solution(bridge_length, weight, truck_weights):
    passing = [0] * bridge_length
    time = 0
    while passing:
        passing.pop(0)
        time += 1
        if len(truck_weights) != 0:
            if sum(passing) + truck_weights[0] <= weight:
                passing.append(truck_weights.pop(0))
            else:
                passing.append(0)
            
        
    return time