def solution(board, moves):
    n = len(board)
    s = []
    answer = 0
    for i in moves:
        for j in range(n):
            if board[i - 1][j] != 0:
                s.append(board[i - 1][j])
                board[i - 1][j] = 0
                break
        if len(s) >= 2:
            for k in range(1, len(s)):
                for l in range(len(s) - 1):
                    if s[k] == s[l]:
                        del s[k], s[l]
                        answer += 2
                
    return answer


if __name__ == "__main__":
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    so = solution(board, moves)
    print(so)
    
