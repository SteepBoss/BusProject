import pygame as pg

def draw_statistics(screen, human, speed, humans, sit_horizont, sit_vertical, all_sit, bus, mouse_x, mouse_y):
    small_font = pg.font.Font(None, 28)
    text_y = 10

    # Выводим статистику для человека
    for key in ['speed','humans', 'x', 'y', 'direction_x', 'direction_y', 'sit_horizont', 'sit_vertical', 'all_sit']:
        if key == 'speed':
            text = small_font.render(f"{key}: {speed}", True, (255, 255, 255))
        elif key == 'humans':
            text = small_font.render(f"{key}: {len(humans)}", True, (255, 255, 255))
        elif key == 'sit_horizont':
            text = small_font.render(f"{key}: {sit_horizont}", True, (255, 255, 255))
        elif key == 'sit_vertical':
            text = small_font.render(f"{key}: {sit_vertical}", True, (255, 255, 255))
        elif key == 'all_sit':
            text = small_font.render(f"{key}: {all_sit}", True, (255, 255, 255))
        else:
            text = small_font.render(f"{key}: {human[key]}", True, (255, 255, 255))
        screen.blit(text, (3, text_y))
        text_y += 21

    # Выводим статистику для автобуса
    bus_stats = ['top', 'bottom', 'left', 'right']
    for key in bus_stats:
        text = small_font.render(f"Bus - {key}: {getattr(bus, key)}", True, (255, 255, 255))
        screen.blit(text, (3, text_y))
        text_y += 20

    # Выводим координаты мыши
    mouse_text = small_font.render(f"Mouse X: {mouse_x}  Mouse Y: {mouse_y}", True, (255, 255, 255))
    screen.blit(mouse_text, (3, text_y))
