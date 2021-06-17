def solution(arr1, arr2):
    answer = [[0 for j in range(len(arr1[0]))] for i in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2[0])):
                answer[i][j] += (arr1[i][k] * arr2[k][j])
        
            
    
    
    
    return answer

#############################################################

def solution2(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for i in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2[0])):
                answer[i][j] += (arr1[i][k] * arr2[k][j])

    
    return answer


############################################################
import numpy as np

def solution3(arr1, arr2):
    return np.dot(arr1, arr2).tolist()


print(solution3([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution3([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))