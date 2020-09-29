import pygame as pg
import random
import numpy as np

pg.init()

process = True
screen_width = 1000
screen_height = 700
hedgehog_width = 220
hedgehog_height = 80
screen = pg.display.set_mode((screen_width, screen_height))

black = (0, 0, 0)
color_dirt = (70, 70, 70)
color_sky = (84, 200, 117)
color_tree = (236, 205, 0)
white = (255, 255, 255)
color1 = (68, 0, 19)
# Создаем фон
screen.fill(color_sky)
pg.draw.rect(screen, color_dirt, (0, 400, screen_width, screen_height))
pg.draw.rect(screen, color_tree, (int(screen_width * 0.75), 0, 100, 440))
pg.draw.rect(screen, color_tree, (int(screen_width * 0.1), 0, 200, 650))
pg.draw.rect(screen, color_tree, (int(screen_width * 0.9), 0, 60, 520))
pg.draw.rect(screen, color_tree, (int(screen_width * 0), 0, 40, 440))


def igolki(x, y, hedgehog_width, hedgehog_height,n):
    a = hedgehog_width / 2.3
    b = hedgehog_height / 2.3

    for i in range(n):
        x0 = random.randint(-int(a), int(a))
        y0 = random.randint(-int(b * (1 - (x0 / a) ** 2) ** 0.5), int(b * (1 - (x0 / a) ** 2) ** 0.5))
        k = random.uniform(-np.pi / 4, np.pi / 4)
        A = [screen_width * x + a + x0, screen_height * y + b + y0]
        B = [screen_width * x + a + x0 + 20 * np.cos(k), screen_height * y + b + y0 - 20 * np.sin(k)]
        C = [screen_width * x + a + x0 + 5 - 90 * np.sin(k), screen_height * y + b + y0 - 90 * np.cos(k)]
        pg.draw.polygon(screen, (30, 30, 30), (A, B, C), )
        pg.draw.polygon(screen, (0, 0, 0), [A, B, C], 1)


def mushroom(x, y):
    pg.draw.ellipse(screen, white,
                    (screen_width * x + hedgehog_width - 140, screen_height * y + hedgehog_height - 160, 20, 70))
    pg.draw.ellipse(screen, (255, 127, 116),
                    (screen_width * x + hedgehog_width - 175, screen_height * y + hedgehog_height - 160, 90, 30))


# Создаем функцию, создающую ежа
def hedgehog(x, y):
    pg.draw.ellipse(screen, (68, 0, 19), (screen_width * x, screen_height * y, hedgehog_width, hedgehog_height))
    pg.draw.ellipse(screen, (100, 100, 100), (screen_width * x, screen_height * y, hedgehog_width, hedgehog_height), 3)

    pg.draw.ellipse(screen, (68, 0, 19),
                    (screen_width * x + hedgehog_width * 0.9, screen_height * y + hedgehog_height * 0.4, 50, 30))
    pg.draw.ellipse(screen, black,
                    (screen_width * x + hedgehog_width * 0.9, screen_height * y + hedgehog_height * 0.4, 50, 30), 1)

    pg.draw.ellipse(screen, black,
                    (screen_width * x + hedgehog_width + 13, screen_height * y + hedgehog_height * 0.4 + 6, 8, 8))
    pg.draw.ellipse(screen, black,
                    (screen_width * x + hedgehog_width + 2, screen_height * y + hedgehog_height * 0.4 + 10, 8, 8))
    pg.draw.ellipse(screen, black,
                    (screen_width * x + hedgehog_width + 23, screen_height * y + hedgehog_height * 0.4 + 11, 6, 6))
    pg.draw.ellipse(screen, white,
                    (screen_width * x + hedgehog_width + 13, screen_height * y + hedgehog_height * 0.4 + 6, 8, 8), 1)
    pg.draw.ellipse(screen, white,
                    (screen_width * x + hedgehog_width + 2, screen_height * y + hedgehog_height * 0.4 + 10, 8, 8), 1)
    pg.draw.ellipse(screen, white,
                    (screen_width * x + hedgehog_width + 23, screen_height * y + hedgehog_height * 0.4 + 11, 6, 6), 1)

    pg.draw.ellipse(screen, (68, 0, 19), (screen_width * x, screen_height * y + hedgehog_height - 20, 40, 20))
    pg.draw.ellipse(screen, (100, 100, 100), (screen_width * x, screen_height * y + hedgehog_height - 20, 40, 20), 2)
    pg.draw.ellipse(screen, (68, 0, 19),
                    (screen_width * x + hedgehog_width - 35, screen_height * y + hedgehog_height - 20, 40, 20))
    pg.draw.ellipse(screen, (100, 100, 100),
                    (screen_width * x + hedgehog_width - 35, screen_height * y + hedgehog_height - 20, 40, 20), 2)

    pg.draw.ellipse(screen, (255, 33, 0),
                    (screen_width * x + hedgehog_width - 100, screen_height * y + hedgehog_height - 140, 70, 70))
    pg.draw.ellipse(screen, (230, 145, 0),
                    (screen_width * x + hedgehog_width - 200, screen_height * y + hedgehog_height - 140, 50, 50))

    igolki(x, y, hedgehog_width, hedgehog_height,50)
    mushroom(x, y)
    igolki(x, y, hedgehog_width, hedgehog_height, 10)


hedgehog(0.6, 0.7)
hedgehog_width = 100
hedgehog_height = 50
hedgehog(0, 0.7)
pg.display.update()

while process:
    # hedgehog(0.6, 0.7)
    # pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            process = False
