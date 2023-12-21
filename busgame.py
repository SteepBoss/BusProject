import pygame as pg
from statistic import draw_statistics

pg.init()

# Установка начального заголовка
pg.display.set_caption("SimulationVirus")
# Размеры экрана
screen_width, screen_height = 1720, 920
screen = pg.display.set_mode((screen_width, screen_height))
bus_outline_color = (255, 0, 0)
# Создаем список прямоугольников
human = {'x': 0, 'y': 0, 'direction_x': 0, 'direction_y': 0}
humans = [{'x': 0, 'y': 800, 'direction_x': 1, 'direction_y': 0}]
# Скорость прямоугольника
speed = 3
rect_width = 30
rect_height = 30
sit_horizont = 2
sit_vertical = 11
mouse_x, mouse_y = 0, 0
# X-координата верхнего левого угла: 600 Y-координата верхнего левого угла: 100
# ШИРИНА  , ВЫСОТА
all_sit = (sit_horizont * sit_vertical)
bus = pg.Rect(1000, 100, 300, 740)
clock = pg.time.Clock()
running = True
paused = False
spawn_timer = pg.time.get_ticks()  # Инициализация таймера для создания нового человека

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False
            elif event.key == pg.K_SPACE:
                paused = not paused  # Инвертируем состояние паузы
        elif event.type == pg.MOUSEMOTION:
            mouse_x, mouse_y = event.pos  # Обновляем координаты мыши

    if not paused:
        # Обновляем координаты каждого прямоугольника
        for human in humans:
            human['x'] += speed * human['direction_x']
            human['y'] += speed * human['direction_y']
            # Проверяем столкновение с автобусом
            if bus.colliderect(pg.Rect(human['x'], human['y'], 30, 30)):
                # Меняем направление на противоположное только если зеленый прямоугольник справа от автобуса
                if human['direction_x'] == 1 and human['x'] + 30 > bus.right - 135:
                    human['direction_y'] = -1
                    human['direction_x'] = 0
                    human['x'] = bus.right - 165
                if human['direction_x'] == 1 and human['x'] + 30 > bus.right:
                    human['direction_y'] = -1
                    human['x'] = bus.right - 30
                if human['direction_y'] == -1 and human['y'] < bus.top:
                    human['direction_y'] *= -1
                    human['direction_x'] = 0
                elif human['direction_y'] == 1 and human['y'] + 30 > bus.bottom:
                    human['direction_y'] *= -1
                    human['direction_x'] = 0


        current_time = pg.time.get_ticks()
        if current_time - spawn_timer > 2000:  # Проверяем, прошло ли 2 секунды с последнего создания человека
            if len(humans) < 5:  # Проверяем, что количество человек меньше 5
                humans.append({'x': 0, 'y': 800, 'direction_x': 1, 'direction_y': 0})
                spawn_timer = current_time

        screen.fill((0, 0, 0))  # Заливаем экран черным
        # Рисуем прямоугольники и автобус
        for human in humans:
            pg.draw.rect(screen, (0, 128, 0), (human['x'], human['y'], 30, 30))
        for i in range(4):  # 4 раза горизонт
            for j in range(sit_vertical):
                x_offset = 30 if i < sit_horizont else 180
                x = x_offset + bus.x + 60 * (i % sit_horizont)  # Размещение прямоугольников по горизонтали
                y = 30 + bus.y + 60 * j  # Размещение прямоугольников по вертикали
                pg.draw.rect(screen, (255, 0, 0), (x, y, rect_width, rect_height))
        # Рисуем левую сторону автобуса
        left_side_bus = 780
        pg.draw.line(screen, bus_outline_color, bus.topleft, (bus.left, left_side_bus), 1)
        pg.draw.line(screen, bus_outline_color, bus.topleft, bus.topright, 1)
        pg.draw.line(screen, bus_outline_color, bus.bottomleft, bus.bottomright, 1)
        pg.draw.line(screen, bus_outline_color, bus.topright, bus.bottomright, 1)

        # Выводим статистику
        draw_statistics(screen, human, speed, humans, sit_horizont, sit_vertical, all_sit, bus, mouse_x, mouse_y)
    pg.display.flip()
    clock.tick(140)

pg.quit()
