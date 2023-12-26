from statistic import draw_statistics
from settings import *
from seat import Seat

spawn_timer = pg.time.get_ticks()
seats = []
for j in range(sit_vertical):
    for i in range(sit_horizont):
        for x_offset in (30, 180 if i < sit_horizont else 0):
            seat = Seat(x_offset + bus.x + 60 * i, 30 + bus.y + 60 * j)
            seats.append(seat)

running = True
paused = False

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                speed -= 1  # Уменьшаем скорость при нажатии стрелки вниз
            elif event.key == pg.K_RIGHT:
                speed += 1  # Увеличиваем скорость при нажатии стрелки вверх
            elif event.key == pg.K_q:
                running = False
            elif event.key == pg.K_SPACE:
                paused = not paused
            elif event.key == pg.K_s:
                for seat in seats:
                    print(seat)
        elif event.type == pg.MOUSEMOTION:
            mouse_x, mouse_y = event.pos

    if not paused:
        screen.fill((0, 0, 0))
        for human in humans:
            human.update_position(speed)
            human.handle_collision(bus, seats)
            human.move_towards_target(all_seats=seats)
            pg.draw.rect(screen, (0, 128, 0), (human.x, human.y, 30, 30))
        current_time = pg.time.get_ticks()
        if current_time - spawn_timer > time_spawn:
            if len(humans) < 10:
                new_human = Human(0, 800, 1, 0, random.randint(0, 100),
                                  random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
                humans.append(new_human)
                spawn_timer = current_time

        for idx, seat in enumerate(seats, start=1):
            seat.set_count(idx)
        # for seat in seats:
        #     print(seat)
        # for human in humans:
        #     print(human)
        pg.draw.line(screen, bus_outline_color, bus.topleft, (bus.left, left_side_bus), 1)
        pg.draw.line(screen, bus_outline_color, bus.topleft, bus.topright, 1)
        pg.draw.line(screen, bus_outline_color, bus.bottomleft, bus.bottomright, 1)
        pg.draw.line(screen, bus_outline_color, bus.topright, bus.bottomright, 1)

        draw_statistics(screen, humans, speed, sleep, rest, nutrition, vaccination,
                        sit_horizont, sit_vertical, all_sit, bus, mouse_x, mouse_y, seats)

    pg.display.flip()
    clock.tick(140)
pg.quit()
