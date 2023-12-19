import pygame as pg

pg.init()

# Установка начального заголовка
pg.display.set_caption("SimulationVirus")

# Размеры экрана
screen_width, screen_height = 1720, 920
screen = pg.display.set_mode((screen_width, screen_height))

clock = pg.time.Clock()
# X-координата верхнего левого угла: 600 Y-координата верхнего левого угла: 100
# ШИРИНА  , ВЫСОТА
bus = pg.Rect(1000, 100, 300, 740)
bus_outline_color = (255, 0, 0)

# Скорость прямоугольника
speed = 3

# Создаем список прямоугольников
humans = [{'x': 0, 'y': 800, 'direction': 1}]

rect_width = 30
rect_height = 30
num_rectangles_horizontal = 2
num_rectangles_vertical = 11

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False

    # Обновляем координаты каждого прямоугольника
    for human in humans:
        human['x'] += speed * human['direction']
        # Проверяем столкновение с автобусом
        if bus.colliderect(pg.Rect(human['x'], human['y'], 30, 30)):
            # Меняем направление на противоположное только если зеленый прямоугольник справа от автобуса
            if human['direction'] == 1 and human['x'] + 30 > bus.right:
                human['direction'] *= -1
        if human['x'] < 0 or human['x'] + 30 > screen_width:
            human['direction'] *= -1

        pg.draw.rect(screen, (0, 128, 0), (human['x'], human['y'], 30, 30))
    for i in range(num_rectangles_horizontal):
        for j in range(num_rectangles_vertical):
            x = 30 + bus.x + 60 * i  # Размещение прямоугольников по горизонтали
            y = 30 + bus.y + 60 * j  # Размещение прямоугольников по вертикали
            pg.draw.rect(screen, (255, 0, 0), (x, y, rect_width, rect_height))
    for i in range(num_rectangles_horizontal):
        for j in range(num_rectangles_vertical):
            x = 180 + bus.x + 60 * i  # Размещение прямоугольников по горизонтали
            y = 30 + bus.y + 60 * j  # Размещение прямоугольников по вертикали
            pg.draw.rect(screen, (255, 0, 0), (x, y, rect_width, rect_height))
    # Высота левой стороны автобуса
    left_side_bus = 780

    pg.draw.line(screen, bus_outline_color, bus.topleft, (bus.left, left_side_bus), 2)
    pg.draw.line(screen, bus_outline_color, bus.topleft, bus.topright, 2)
    pg.draw.line(screen, bus_outline_color, bus.bottomleft, bus.bottomright, 2)
    pg.draw.line(screen, bus_outline_color, bus.topright, bus.bottomright, 2)
    pg.display.flip()
    screen.fill((0, 0, 0))

    clock.tick(140)

pg.quit()
