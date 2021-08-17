# -*- coding: utf-8 -*-
def solution(game_board, table):
    answer = 0
    
    
    for i in range(len(table) - 1):
        length = 0
        for j in range(len(table) - 1):
            if table[i][j] == 1:
                while table[i][j+1] == 1 or table[i+1][j] == 1:
                    length += 1
        for a in range(len(game_board) - 1):
            length2 = 0
            for b in range(len(Game_board) - 1):
                if game_board[a][b] == 1:
                    while game_board[a][b+1] == 1 or game_board[a+1][b] == 1:
                        length2 += 1
        if len(length) == len(length2):
            answer += length
    return answer

