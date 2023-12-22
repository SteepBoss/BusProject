from statistic import draw_statistics
from settings import *

running = True
paused = False
spawn_timer = pg.time.get_ticks()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False
            elif event.key == pg.K_SPACE:
                paused = not paused
        elif event.type == pg.MOUSEMOTION:
            mouse_x, mouse_y = event.pos

    if not paused:
        for human in humans:
            human.update_position(speed)
            human.handle_collision(bus)

        current_time = pg.time.get_ticks()
        if current_time - spawn_timer > 2000:
            if len(humans) < 5:
                humans.append(Human(0, 800, 1, 0))
                spawn_timer = current_time

        screen.fill((0, 0, 0))
        for human in humans:
            pg.draw.rect(screen, (0, 128, 0), (human.x, human.y, 30, 30))
        for i in range(4):
            for j in range(sit_vertical):
                x_offset = 30 if i < sit_horizont else 180
                x = x_offset + bus.x + 60 * (i % sit_horizont)  # Размещение прямоугольников по горизонтали
                y = 30 + bus.y + 60 * j  # Размещение прямоугольников по вертикали
                pg.draw.rect(screen, (255, 0, 0), (x, y, rect_width, rect_height))
        left_side_bus = 780
        pg.draw.line(screen, bus_outline_color, bus.topleft, (bus.left, left_side_bus), 1)
        pg.draw.line(screen, bus_outline_color, bus.topleft, bus.topright, 1)
        pg.draw.line(screen, bus_outline_color, bus.bottomleft, bus.bottomright, 1)
        pg.draw.line(screen, bus_outline_color, bus.topright, bus.bottomright, 1)

        draw_statistics(screen, humans, speed, sit_horizont, sit_vertical, all_sit, bus, mouse_x, mouse_y)
    pg.display.flip()
    clock.tick(140)
pg.quit()
