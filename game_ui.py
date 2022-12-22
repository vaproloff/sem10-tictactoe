import pygame

WIDTH = 300
HEIGHT = 300

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()
screen.fill((255, 255, 255))

pygame.draw.line(screen, (0, 0, 0), (100, 0), (100, 300), 2)
pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 300), 2)
pygame.draw.line(screen, (0, 0, 0), (0, 100), (300, 100), 2)
pygame.draw.line(screen, (0, 0, 0), (0, 200), (300, 200), 2)


def draw_move(position, is_cross):
    center_x = position[0] * 100 + 50
    center_y = position[1] * 100 + 50

    if is_cross:
        pygame.draw.line(screen, (0, 0, 0), (center_x - 20, center_y - 20),
                         (center_x + 20, center_y + 20), 2)

        pygame.draw.line(screen, (0, 0, 0), (center_x + 20, center_y - 20),
                         (center_x - 20, center_y + 20), 2)
    else:
        pygame.draw.circle(screen, (0, 0, 0), (center_x, center_y), 40, 2)


def get_position(mouse_x, mouse_y):
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

    return [row, col]


def click_board():
    (mouseX, mouseY) = pygame.mouse.get_pos()
    position = get_position(mouseX, mouseY)
    draw_move(position, True)


def show_board(ttt, board):

    # (re)draw the game board (board) on the screen (ttt)
    # drawStatus(board)
    ttt.blit (board, (0,0))
    pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type is pygame.MOUSEBUTTONDOWN:
            click_board()
            show_board(ttt, board)
