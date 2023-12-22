import pygame as pg

def draw_statistics(screen, humans, speed, sit_horizont, sit_vertical, all_sit, bus, mouse_x, mouse_y):
    small_font = pg.font.Font(None, 28)
    text_y = 10

    for idx, human in enumerate(humans):
        # Разделяем текст на несколько строк
        lines = [
            f"Человек {idx + 1} Позиция: (X{human.x}, Y{human.y})",
            f"Направление X: {human.direction_x},Направление Y: {human.direction_y}"
        ]

        # Создаем поверхности для каждой строки текста
        text_surfaces = [small_font.render(line, True, (255, 255, 255)) for line in lines]

        # Отрисовываем каждую строку текста поочередно с увеличением координаты Y
        for text_surface in text_surfaces:
            screen.blit(text_surface, (3, text_y))
            text_y += 21

    # Выводим общую статистику
    for key in ['speed', 'sit_horizont', 'sit_vertical', 'all_sit']:
        if key == 'speed':
            text = small_font.render(f"{key}: {speed}", True, (255, 255, 255))
        elif key == 'sit_horizont':
            text = small_font.render(f"{key}: {sit_horizont}", True, (255, 255, 255))
        elif key == 'sit_vertical':
            text = small_font.render(f"{key}: {sit_vertical}", True, (255, 255, 255))
        elif key == 'all_sit':
            text = small_font.render(f"{key}: {all_sit}", True, (255, 255, 255))
        screen.blit(text, (3, text_y))
        text_y += 21

    # Выводим статистику для автобуса
    bus_stats = ['top', 'bottom', 'left', 'right']
    for key in bus_stats:
        text = small_font.render(f"Bus - {key}: {getattr(bus, key)}", True, (255, 255, 255))
        screen.blit(text, (3, text_y))
        text_y += 20

    # Выводим координаты мыши
    mouse_text = small_font.render(f"X: {mouse_x} Y: {mouse_y}", True, (255, 255, 255))
    screen.blit(mouse_text, (3, text_y))
