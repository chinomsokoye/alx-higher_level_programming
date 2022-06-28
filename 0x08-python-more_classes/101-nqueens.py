#!/usr/bin/python3


import sys


def game_board(board):
    if any(1 in i for i in board):
        print([[idx, board[idx].index(1)] for idx, valu in enumerate(board)])


def safe_game(row, square, chessboard, N, diagon):
    if chessboard[row][square]:
        return False
    if square - diagon >= 0 and chessboard[row][square - diagon]:
        return False
    if square + diagon < (N) and chessboard[row][square + diagon]:
        return False
    if row == 0:
        return True
    return safe_game(row - 1, square, chessboard, N, diagon + 1)


def square_placed(row, position, chessboard, N):
    for square in range(position, N):
        if 1 in chessboard[row]:
            return 0
        if not safe_game(row - 1, square, chessboard, N, 1):
            continue
        chessboard[row][square] = 1
        return
    return 1


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

if not str.isdigit(N):
    print("N must be a number")
    sys.exit(1)

N = int(N)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = 0

while queen != N:
    chessboard = [[0 for i in range(N)] for i in range(N)]
    chessboard[0][queen] = 1
    position = 0
    row = 1
    while row < N:
        if square_placed(row, position, chessboard, N):
            row -= 1
            position = chessboard[row].index(1)
            chessboard[row][position] = 0
            position += 1
            if not row:
                break
        row += 1
        position = 0
    game_board(chessboard)
    queen += 1
