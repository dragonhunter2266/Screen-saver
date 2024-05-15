import pygame
import random

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
clock = pygame.time.Clock()

grey = 100, 100, 100
red = [255, 0, 0]
black = 0, 0, 0
block_size = 10


def game():
    run = True
    dis.fill(black)
    pygame.display.update()
    x = round(random.randrange(0, 790) / 10) * 10
    y = round(random.randrange(0, 590) / 10) * 10
    x_change = random.randrange(1, 5)
    y_change = random.randrange(1, 5)
    player = []
    color = red

    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    run = False
                    game()
                if event.key == pygame.K_q:
                    run = False
                if event.key == pygame.K_w:
                    if x_change > 0:
                        x_change += 1
                    else:
                        x_change -= 1
                    if y_change > 0:
                        y_change += 1
                    else:
                        y_change -= 1
                if event.key == pygame.K_s:
                    if x_change > 0:
                        x_change -= 1
                    else:
                        x_change += 1
                    if y_change > 0:
                        y_change -= 1
                    else:
                        y_change += 1
        x += x_change
        y += y_change
        playerloc = [x, y, color.copy()]
        player.append(playerloc)
        if 0 > x or x > 790:
            x_change = -x_change
        if 0 > y or y > 590:
            y_change = -y_change
        if len(player) > 150:
            pygame.draw.rect(dis, black, (player[0][0], player[0][1], block_size, block_size))
            del player[0]
            pygame.draw.rect(dis, player[0][2], (player[0][0], player[0][1], block_size, block_size))
        pygame.draw.rect(dis, color, (x, y, block_size, block_size))
        pygame.display.update()
        clock.tick(120)
        if color[0] == 255 and color[1] != 255 and color[2] == 0:
            color[1] += 1
        if color[0] != 0 and color[1] == 255 and color[2] == 0:
            color[0] -= 1
        if color[1] == 255 and color[2] != 255 and color[0] == 0:
            color[2] += 1
        if color[1] != 0 and color[2] == 255 and color[0] == 0:
            color[1] -= 1
        if color[2] == 255 and color[0] != 255 and color[1] == 0:
            color[0] += 1
        if color[2] != 0 and color[0] == 255 and color[1] == 0:
            color[2] -= 1
    pygame.quit()
    quit()


game()
