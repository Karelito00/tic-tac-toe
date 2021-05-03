import random

PLAYERS = ['X', 'O']

def check_state(mat):
    for c in PLAYERS:
        win_diag1 = True
        win_diag2 = True
        for i in range(3):
            # check rows
            win_rows = True
            win_columns = True
            for j in range(3):
                if(mat[i][j] != c):
                    win_rows = False
                if(mat[j][i] != c):
                    win_columns = False
            if(win_rows or win_columns):
                return c
            if(mat[i][i] != c):
                win_diag1 = False
            if(mat[i][2 - i] != c):
                win_diag2 = False
        if(win_diag1 or win_diag2):
            return c
    return ' '

def best_move(k, mat, player):
    check = check_state(mat)
    if(check != ' '):
        return 10 - k if k % 2 == 0 else -(10 - k)
    best = 20 * (1 if k % 2 == 0 else -1)
    for i in range(3):
        for j in range(3):
            if(mat[i][j] == ' '):
                mat[i][j] = player
                state = best_move(k + 1, mat, 'X' if player == 'O' else 'O')
                mat[i][j] = ' '
                if(k % 2 == 0):
                    best = min(best, state)
                else:
                    best = max(best, state)
    if(abs(best) == 20): #tie
        return 0
    return best

def play_turn(mat, player):
    max_m = -100
    coord = (0, 0)
    for i in range(3):
        for j in range(3):
            if(mat[i][j] == ' '):
                mat[i][j] = player
                state = best_move(0, mat, 'X' if player == 'O' else 'O')
                mat[i][j] = ' '
                if(state > max_m):
                    max_m = state
                    coord = (i, j)
    return coord

def init():
    return [[' '] * 3, [' '] * 3, [' '] * 3]

def print_game(mat):
    for i in range(3):
        for j in range(3):
            print(mat[i][j], end=" ")
            if(j != 2):
                print('|', end=" ")
        print()
        if(i != 2):
            print('__________')

def Game():
    mat = init()
    player = "O"
    mov = 0
    while(True):
        print("Enter coordinates")
        a = 0
        b = 0
        while(True):
            a, b = [int(x) for x in input().split(' ')]
            if(a > 2 or a < 0 or b > 2 or b < 0 or mat[a][b] != ' '):
                print("Invalid coordinates")
                continue
            break
        mat[a][b] = 'O'
        print_game(mat)
        check = check_state(mat)
        if(check != ' '):
            print('Win: ' + check)
            return
        if(mov == 4):
            print('Tie')
            return
        coord = play_turn(mat, 'X')
        mat[coord[0]][coord[1]] = 'X'
        print_game(mat)
        check = check_state(mat)
        if(check != ' '):
            print('Win: ' + check)
            return
        mov += 1

Game()

