import pygame
import random
import time

# Initialize window
def init_window():
    # window size
    WIDTH  = 600
    HEIGHT = 500

    # color
    BlACK  = (0, 0, 0)
    WHITE  = (255, 255, 255)
    BLUE   = (0, 0, 255)
    RED    = (255, 0, 0)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 165, 0)

    pygame.init()

    # game window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BlACK)
    pygame.display.set_caption('PAC MAN')

    return BlACK, WHITE, BLUE, RED, YELLOW, ORANGE, screen

# Initialize game
def init_game():
    score = 0

    # font
    font_size = 36
    font = pygame.font.Font(None, font_size)

    # map 10*10(8*8)
    #0: dot 1: wall 2:pacman 3:enemy
    map_data = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 2, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 3, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    # pacman's initial position(index)
    pacman_x = 4
    pacman_y = 1

    # enemy's initial position
    enemy_0_x = 4
    enemy_0_y = 8

    # all mapdata and character size(square)
    block_size = 30

    return score, map_data, pacman_x, pacman_y, block_size, enemy_0_x, enemy_0_y

def draw_game_window(map_data, pacman_x, pacman_y, enemy_0_x, enemy_0_y, screen, WHITE, BLACK, BLUE, RED, YELLOW, ORANGE, block_size):
    #draw 
    for y in range(len(map_data)):
        for x in range(len(map_data[y])):
            # draw wall
            if map_data[y][x] == 1:
                pygame.draw.rect(screen, BLUE,   (block_size * x, block_size * y, block_size, block_size))
            
            # draw dot
            elif map_data[y][x] == 0:
                pygame.draw.rect(screen, ORANGE, (block_size * x, block_size * y, block_size, block_size))

            # draw pacman
            elif map_data[y][x] == 2:
                pygame.draw.rect(screen, YELLOW, (block_size * x, block_size * y, block_size, block_size))

            # draw enemy
            elif map_data[y][x] == 3:
                pygame.draw.rect(screen, RED,    (block_size * x, block_size * y, block_size, block_size))

def move_coordinate(up, down, left, right, map_data, pacman_x, pacman_y, enemy_0_x, enemy_0_y):
    #Packman Movement
    if up:
        for y in range(len(map_data)):
            for x in range(len(map_data[y])):
                if map_data[y][x] == 2:

                    # collision processing
                    if map_data[y-1][x] == 0:

                        map_data[y-1][x] = 2
                        map_data[y][x]   = 0

    elif down:
        for y in range(len(map_data)):
            for x in range(len(map_data[y])):
                if map_data[y][x] == 2:

                    # collision processing
                    if map_data[y+1][x] == 0:

                        map_data[y+1][x] = 2
                        map_data[y][x]   = 0

    elif left:
        for y in range(len(map_data)):
            for x in range(len(map_data[y])):
                if map_data[y][x] == 2:

                    # collision processing
                    if map_data[y][x-1] == 0:

                        map_data[y][x-1] = 2
                        map_data[y][x]   = 0

    elif right:
        for y in range(len(map_data)):
            for x in range(len(map_data[y])):
                if map_data[y][x] == 2:

                    # collision processing
                    if map_data[y][x+1] == 0:

                        map_data[y][x+1] = 2
                        map_data[y][x]   = 0

    #Enemy Movement
    can_move = []

    # collision up processing
    for y in range(len(map_data)):
        for x in range(len(map_data[y])):
            if map_data[y][x] == 3:

                if y - 1 == -1:
                    break
                
                if map_data[y-1][x] == 0:
                    can_move.append(0)

    # collision down processing
    for y in range(len(map_data)):
        for x in range(len(map_data[y])):
            if map_data[y][x] == 3:

                if y + 1 == 10:
                    break
                
                if map_data[y+1][x] == 0:
                    can_move.append(1)

    # collision left processing
    for y in range(len(map_data)):
        for x in range(len(map_data[y])):
            if map_data[y][x] == 3:

                if x - 1 == -1:
                    break
                
                if map_data[y][x-1] == 0:
                    can_move.append(2)

    # collision right processing
    for y in range(len(map_data)):
        for x in range(len(map_data[y])):
            if map_data[y][x] == 3:

                if x + 1 == 10:
                    break
                
                if map_data[y][x+1] == 0:
                    can_move.append(3)

    random.shuffle(can_move)

    movement = can_move[0]

    if movement == 0:
        for y in range(len(map_data)):
            for x in range(len(map_data[y])):
                if map_data[y][x] == 3:
                    map_data[y-1][x] = 3
                    map_data[y][x]   = 0

    elif movement == 1:
        for y in range(len(map_data)):
            for x in range(len(map_data[y])):
                if map_data[y][x] == 3:
                    map_data[y+1][x] = 3    
                    map_data[y][x]   = 0

    elif movement == 2:
        for y in range(len(map_data)):
            for x in range(len(map_data[y])):
                if map_data[y][x] == 3:
                    map_data[y][x-1] = 3
                    map_data[y][x]   = 0

    elif movement == 3:
        for y in range(len(map_data)):
            for x in range(len(map_data[y])):
                if map_data[y][x] == 3:
                    map_data[y][x+1] = 3
                    map_data[y][x]   = 0

def main():
    BLACK, WHITE, BLUE, RED, YELLOW, ORANGE, screen                       = init_window()
    score, map_data, pacman_x, pacman_y, block_size, enemy_0_x, enemy_0_y = init_game()

    # game loop
    running = True
    clock = pygame.time.Clock()

    # Let them watch for 5s and then start
    draw_game_window(map_data, pacman_x, pacman_y, enemy_0_x, enemy_0_y, screen, WHITE, BLACK, BLUE, RED, YELLOW, ORANGE, block_size)
    pygame.display.update()
    time.sleep(1)
    
    while running:
        # input(reset)
        up    = False
        down  = False
        left  = False
        right = False

        # process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K.UP:
                up = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K.DOWN:
                down = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K.LEFT:
                left = True
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K.RIGHT:
                right = True

        move_coordinate(up, down, left, right, map_data, pacman_x, pacman_y, enemy_0_x, enemy_0_y)
    
        draw_game_window(map_data, pacman_x, pacman_y, enemy_0_x, enemy_0_y, screen, WHITE, BLACK, BLUE, RED, YELLOW, ORANGE, block_size)

        pygame.display.update()
    
        #FPS
        clock.tick(1)