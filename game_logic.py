import random
import time
from main import draw_move


def generate_board():
    board = []
    for i in range(3):
        board.append([])
        for j in range(3):
            board[i].append(' ')
    return board


def check_position(position, board):
    if not (0 <= position[0] < len(board) or 0 <= position[1] < len(board[0])):
        return False
    else:
        return board[position[0]][position[1]] == ' '


def check_board_full(board):
    for i in range(len(board)):
        for j in board[i]:
            if j == ' ':
                return False
    return True


def check_win(board):
    for i in board:
        if i.count(True) == len(board) or i.count(False) == len(board):
            return True
    for i in range(len(board)):
        col = [board[j][i] for j in range(len(board))]
        if col.count(True) == len(board) or col.count(False) == len(board):
            return True
    diag1 = [board[i][i] for i in range(len(board))]
    if diag1.count(True) == len(board) or diag1.count(False) == len(board):
        return True
    diag2 = [board[i][-i - 1] for i in range(len(board))]
    if diag2.count(True) == len(board) or diag2.count(False) == len(board):
        return True
    return False


def player_turn(board):
    position = [-1, -1]
    while not check_position(position, board):
        position = [int(input(f'Ваш ход. Введите номер строки (1-{len(board)}): ')) - 1,
                    int(input(f'Введите номер столбца (1-{len(board)}): ')) - 1]
        if not check_position(position, board):
            print('Неверная позиция. Попробуйте снова')
            time.sleep(0.5)
    return position


def bot_turn(board):
    time.sleep(0.5)
    position = [-1, -1]
    while not check_position(position, board):
        position = [random.randint(0, len(board) - 1), random.randint(0, len(board[0]) - 1)]
    return position


def play_game(board):
    is_player = True
    while not check_board_full(board):
        if is_player:
            position = player_turn(board)
        else:
            position = bot_turn(board)
        board[position[0]][position[1]] = is_player
        draw_move(position, is_player)
        if check_win(board):
            print(f'Игра завершена. {"Вы выиграли. Поздравляем!" if is_player else "Выиграл бот:("}')
            break
        is_player = not is_player
        time.sleep(0.5)
    else:
        print('Никто не выиграл')
