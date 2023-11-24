import random

import pygame

pygame.init()

# KEY VARIABLES
WIDTH = 400
HEIGHT = 500
timer = pygame.time.Clock()
FPS = 60
FONT = pygame.font.Font('freesansbold.ttf', 24)

COLORS = {
    0: (204, 192, 179),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
    'light text': (249, 246, 242),
    'dark text': (119, 110, 101),
    'other': (0, 0, 0),
    'bg': (187, 173, 160)
}

BOARD_VALUES = [[0 for _ in range(4)] for _ in range(4)]
game_over = False
spawn_new = True
init_count = 0

# SCREEN SETUP
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('2048')


def draw_board():
    pygame.draw.rect(screen, COLORS['bg'], [0, 0, 400, 400], 0, 10)


def draw_pieces(board_values):
    for i in range(len(board_values)):
        for j in range(len(board_values)):
            value = board_values[i][j]
            if value > 8:
                value_color = COLORS['light text']
            else:
                value_color = COLORS['dark text']
            if value <= 2048:
                color = COLORS[value]
            else:
                color = COLORS['other']

            pygame.draw.rect(screen, color, [j * 95 + 20, i * 95 + 20, 75, 75], 0, 5)

            if value > 0:
                value_len = len(str(value))
                font = pygame.font.Font('freesansbold.ttf', 48 - (5 * value_len))
                value_text = font.render(str(value), True, value_color)
                text_rect = value_text.get_rect(center=(j * 95 + 57, i * 95 + 57))
                screen.blit(value_text, text_rect)
                pygame.draw.rect(screen, 'black', [j * 95 + 20, i * 95 + 20, 75, 75], 2, 5)


def new_pieces(board_values):
    full = False
    count = 0
    while any(0 in row for row in board_values) and count < 1:
        row = random.randint(0, 3)
        column = random.randint(0, 3)
        if board_values[row][column] == 0:
            count += 1
            if random.randint(1, 10) == 10:
                board_values[row][column] = 4
            else:
                board_values[row][column] = 2
    if count < 1:
        full = True

    return board_values, full


# GAME LOOP
def game_loop():
    global spawn_new, init_count
    running = True
    while running:
        timer.tick(FPS)
        screen.fill('gray')
        draw_board()
        draw_pieces(BOARD_VALUES)

        if spawn_new or init_count < 2:
            board_values, game_over = new_pieces(BOARD_VALUES)
            spawn_new = False
            init_count += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:


        pygame.display.flip()
    pygame.quit()


game_loop()
