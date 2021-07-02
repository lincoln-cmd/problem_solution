'''
 1차 정답
'''


def solution(brown, yellow):
    # 가로 -> x, 세로 -> y
    # brown = 2x + 2(y - 2)
    # yellow = (x - 2)(y - 2)
    for i in range(1, brown + yellow):
        if (brown + yellow) % i == 0:
            y = i
            x = (brown + yellow) // y
            if yellow == (x - 2) * (y - 2):
                return [x, y]
            
            
######################################################

'''
 2차 정답 : 근의 공식 이용
'''

def solution(brown, yellow):
    # brown = 2x + 2(y - 2)
    # yellow = (x - 2)(y - 2)
    # x = b +- [(b+4)^2 + 16b + 16e]^0.5 / 4
    # (b = brown, e = yellow)
    b = brown
    e = yellow
    x = (2 + 0.5*b + ((0.5*b+2)**2 - 4*b - 4*e)**0.5) / 2
    y = (brown + yellow) // x
    
    return [x, y]