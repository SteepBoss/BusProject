import pygame as pg

pg.init()

# Установка начального заголовка
pg.display.set_caption("SimulationVirus")

# Размеры экрана
screen_width, screen_height = 1280, 720
screen = pg.display.set_mode((screen_width, screen_height))

clock = pg.time.Clock()

bus = pg.Rect(600, 100, 600, 300)
bus_outline_color =  (255, 0, 0)

# Скорость прямоугольника
speed = 3


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

    # Обновляем координаты каждого прямоугольника
    for rect in rectangles:
        rect['x'] += speed * rect['direction']
        # Проверяем столкновение с автобусом
        if bus.colliderect(pg.Rect(rect['x'], rect['y'], 30, 30)):
            # Меняем направление на противоположное только если зеленый прямоугольник справа от автобуса
            if rect['direction'] == 1 and rect['x'] + 30 > bus.right:
                rect['direction'] *= -1
        if rect['x'] < 0:
            rect['direction'] *= -1
        pg.draw.rect(screen, (0, 128, 0), (rect['x'], rect['y'], 30, 30))
    # Высота левой стороны автобуса
    left_side_bus = 350
    pg.draw.line(screen, bus_outline_color, bus.topleft, (bus.left, left_side_bus), 2)
    pg.draw.line(screen, bus_outline_color, bus.topleft, bus.topright, 2)
    pg.draw.line(screen, bus_outline_color, bus.bottomleft, bus.bottomright, 2)
    pg.draw.line(screen, bus_outline_color, bus.topright, bus.bottomright, 2)
    pg.display.flip()
    screen.fill((0, 0, 0))

    clock.tick(140)

pg.quit()
