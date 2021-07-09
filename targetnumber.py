'''
 완전 탐색을 이용한 함수
'''

from itertools import product as pro

def solution(numbers, target):
    l = [(i, -i) for i in numbers]
    s = list(map(sum, pro(*l)))
    print(l)
    print(s)
    #t = list(pro(*l)) # itertools.product(*list) -> returns the all possible options
    # which can be made with the componets in the list
    #print(t)
    #print(len(t))
    return s.count(target)

#print(solution([1,1,1,1,1], 3))
#print(solution([1,2,3,4,5], 2))
#print(solution([1,2,1,2], 6))

############################################################

'''
 BFS 풀이
'''
def solution2(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
            print('tmp : ', tmp)
        leaves = tmp
        print('leaves', leaves)
    
print(solution2([1,2,3],2))

##########################################################

'''
 BFS 방법을 참조해서 이중 for문으로 구현
'''

def solution(numbers, target):
    answer = 0
    list1 = [(i, -i) for i in numbers]
    list2 = [0]
    for i in range(len(list1)):
        temp = []
        for j in list2:
            temp.append(j + list1[i][0])
            temp.append(j + list1[i][1])
        list2 = temp
    return list2.count(target)