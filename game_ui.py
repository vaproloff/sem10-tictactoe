import pygame

BOARD_WIDTH = 300
BOARD_HEIGHT = 330
CROSS_HALFWIDTH = 30
CIRCLE_RADIUS = 30
LINE_WIDTH = 3
WINLINE_WIDTH = 5
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_GREEN = (0, 255, 0)


def init_board():
    screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")
    screen.fill(COLOR_WHITE)
    pygame.draw.line(screen, COLOR_BLACK, (100, 0), (100, 300), LINE_WIDTH)
    pygame.draw.line(screen, COLOR_BLACK, (200, 0), (200, 300), LINE_WIDTH)
    pygame.draw.line(screen, COLOR_BLACK, (0, 100), (300, 100), LINE_WIDTH)
    pygame.draw.line(screen, COLOR_BLACK, (0, 200), (300, 200), LINE_WIDTH)
    update_board()
    return screen


def update_board():
    pygame.display.flip()


def draw_move(screen, position, is_cross):
    center_x = position[0] * 100 + 50
    center_y = position[1] * 100 + 50

    if is_cross:
        pygame.draw.line(screen, COLOR_BLACK, (center_x - CROSS_HALFWIDTH, center_y - CROSS_HALFWIDTH),
                         (center_x + CROSS_HALFWIDTH, center_y + CROSS_HALFWIDTH), LINE_WIDTH)

        pygame.draw.line(screen, COLOR_BLACK, (center_x + CROSS_HALFWIDTH, center_y - CROSS_HALFWIDTH),
                         (center_x - CROSS_HALFWIDTH, center_y + CROSS_HALFWIDTH), LINE_WIDTH)
    else:
        pygame.draw.circle(screen, COLOR_BLACK, (center_x, center_y), CIRCLE_RADIUS, LINE_WIDTH)

    update_board()


def draw_win_line(screen, coord_1, coord_2):
    pygame.draw.line(screen, COLOR_GREEN, coord_1, coord_2, WINLINE_WIDTH)
    update_board()


def click_board():
    (mouse_x, mouse_y) = pygame.mouse.get_pos()

    if mouse_y < 100:
        row = 0
    elif mouse_y < 200:
        row = 1
    else:
        row = 2
    if mouse_x < 100:
        col = 0
    elif mouse_x < 200:
        col = 1
    else:
        col = 2

    return [col, row]


def draw_status(screen, message):
    font = pygame.font.SysFont('couriernew', 18)
    text = font.render(message, True, COLOR_WHITE)
    pygame.draw.rect(screen, COLOR_BLACK, (0, 300, 300, 330), 0)
    screen.blit(text, (5, 300))
    update_board()
