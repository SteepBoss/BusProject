import pygame as pg

pg.init()

# Размеры экрана
screen_width, screen_height = 1280, 720
screen = pg.display.set_mode((screen_width, screen_height))

clock = pg.time.Clock()

bus = pg.Rect(600, 100, 300, 500)
bus_outline_color = (255, 255, 255)

# Скорость прямоугольника
speed = 1

# Создаем список прямоугольников
rectangles = [{'x': 0, 'y': 360, 'direction': 1}]

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False

    # Проверяем, достиг ли текущий прямоугольник правого края
    if rectangles[-1]['x'] >= screen_width - 30:
        # Создаем новый прямоугольник
        new_rect = {'x': 0, 'y': 360, 'direction': 1}
        rectangles.append(new_rect)

    # Обновляем координаты каждого прямоугольника
    for rect in rectangles:
        rect['x'] += speed * rect['direction']

        # Изменяем направление, если прямоугольник достиг границы экрана
        if rect['x'] <= 0 or rect['x'] >= screen_width - 30:
            rect['direction'] *= -1
    screen.fill((0, 0, 0))

    pg.draw.rect(screen, bus_outline_color, bus ,2)

    # Отрисовка всех прямоугольников
    for rect in rectangles:
        pg.draw.rect(screen, (0, 128, 0), (rect['x'], rect['y'], 30, 30))
    pg.display.flip()

    clock.tick(140)

pg.quit()
