# здесь подключаются модули
import pygame
import sys
import random

# здесь определяются константы,
# классы и функции
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)

# здесь происходит инициация,
# создание объектов
pygame.init()
sc = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
circles = []
count = 0

# если надо до цикла отобразить
# какие-то объекты, обновляем экран
pygame.display.update()

# главный цикл
while True:

    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            print(i.pos[0], i.pos[1])
            for el in circles:
                # (x-x0)^2 + (y-y0)^2 <= r^2
                # от точки (x, y) до точки (x0, y0)
                if (el[0]-i.pos[0])**2 + (el[1]-i.pos[1])**2 <= el[2]**2:
                    circles.remove(el)
                    count -= 1
                    # добавить нечто, чтобы потом появлялся новый круг
        # отображать координаты нажатий левой кнопкой мыши

    # --------
    # изменение объектов
    # --------

    sc.fill(WHITE)
    # создавать круги со случайными координатами до тех пор, пока их не станет 5 штук

    if count < 5:
        x = random.randint(0, 600)
        y = random.randint(0, 400)
        r = random.randint(10, 50)
        circles.append((x, y, r))
        count += 1
    for el in circles:
        pygame.draw.circle(sc, GREEN, (el[0], el[1]), el[2])

    # обновление экрана
    pygame.display.update()
