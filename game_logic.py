import random
import time
from game_ui import *


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


def check_board_full(screen, board):
    for i in range(len(board)):
        for j in board[i]:
            if j == ' ':
                return False
    draw_status(screen, 'Ничья')
    time.sleep(3)
    pygame.quit()
    exit()


def check_win(screen, board, is_player):
    is_winner = False
    for col in range(len(board)):
        if board[col].count(True) == len(board) or board[col].count(False) == len(board):
            is_winner = True
            draw_win_line(screen, ((col + 1) * 100 - 50, 0), ((col + 1) * 100 - 50, 300))
            break
    for i in range(len(board)):
        row = [board[j][i] for j in range(len(board))]
        if row.count(True) == len(board) or row.count(False) == len(board):
            is_winner = True
            draw_win_line(screen, (0, (i + 1) * 100 - 50), (300, (i + 1) * 100 - 50))
            break
    diag1 = [board[i][i] for i in range(len(board))]
    if diag1.count(True) == len(board) or diag1.count(False) == len(board):
        is_winner = True
        draw_win_line(screen, (50, 50), (250, 250))
    diag2 = [board[i][-i - 1] for i in range(len(board))]
    if diag2.count(True) == len(board) or diag2.count(False) == len(board):
        is_winner = True
        draw_win_line(screen, (250, 50), (50, 250))

    if is_winner:
        draw_status(screen, f'Выиграл {"игрок. Поздравляем!" if is_player else "бот"}')
        time.sleep(3)
        pygame.quit()
        exit()


def bot_turn(board):
    time.sleep(0.5)
    position = [-1, -1]
    while not check_position(position, board):
        position = [random.randint(0, len(board) - 1), random.randint(0, len(board[0]) - 1)]
    return position


def make_turn(screen, board, position, is_player):
    board[position[0]][position[1]] = is_player
    draw_move(screen, position, is_player)
    check_win(screen, board, is_player)
    check_board_full(screen, board)
    return not is_player


def play_game(board):
    pygame.init()
    screen = init_board()

    is_player = True
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = click_board()
                if check_position(position, board):
                    is_player = make_turn(screen, board, position, is_player)
            else:
                if not is_player:
                    draw_status(screen, 'Ход бота')
                    position = bot_turn(board)
                    is_player = make_turn(screen, board, position, is_player)
                draw_status(screen, 'Ход игрока')
