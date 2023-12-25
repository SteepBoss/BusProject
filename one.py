import pygame as pg

# Инициализация Pygame
pg.init()

# Создание экрана
screen_width, screen_height = 800, 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Движение вправо и вниз")

# Определение цветов
black = (0, 0, 0)
white = (255, 255, 255)

# Начальные координаты и размеры квадрата
x, y = 100, 100
width, height = 30, 30
speed = 2  # Скорость движения

# Координаты конечной точки
target_x, target_y = 500, 500

# Основной цикл игры
running = True
move_right = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Если движемся вправо
    if move_right:
        x += speed
        # Если достигли нужной координаты по оси X
        if x >= target_x:
            move_right = False  # Переключаемся на движение вниз
    else:
        y += speed
        # Если достигли нужной координаты по оси Y
        if y >= target_y:
            running = False  # Завершаем программу

    # Отрисовка
    screen.fill(black)
    pg.draw.rect(screen, white, (int(x), int(y), width, height))

    # Обновление экрана
    pg.display.flip()

    # Установка частоты кадров
    pg.time.Clock().tick(60)

# Завершение работы Pygame
pg.quit()
