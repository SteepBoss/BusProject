from settings import *


def draw_statistics(screen, humans, speed, sleep, rest, nutrition, vaccination,
                    sit_horizont, sit_vertical, all_sit, bus, mouse_x, mouse_y, seats):
    small_font_left = pg.font.Font(None, 28)
    small_font_right = pg.font.Font(None, 20)
    text_y_left = 1
    text_y_right = 1
    all_text_surfaces_left = []  # Создаем список для хранения текстовых поверхностей слева
    all_text_surfaces_right = []  # Создаем список для хранения текстовых поверхностей справа

    for key in ['speed', 'sit_horizont', 'sit_vertical', 'all_sit']:
        if key == 'speed':
            text = small_font_left.render(f"{key}: {speed}", True, (255, 255, 255))
            all_text_surfaces_left.append(text)
        elif key == 'sit_horizont':
            text = small_font_left.render(f"{key}: {sit_horizont}", True, (255, 255, 255))
            all_text_surfaces_left.append(text)
        elif key == 'sit_vertical':
            text = small_font_left.render(f"{key}: {sit_vertical}", True, (255, 255, 255))
            all_text_surfaces_left.append(text)
        elif key == 'all_sit':
            text = small_font_left.render(f"{key}: {all_sit}", True, (255, 255, 255))
            all_text_surfaces_left.append(text)

    bus_stats = ['top', 'bottom', 'left', 'right']
    for key in bus_stats:
        text = small_font_left.render(f"Bus - {key}: {getattr(bus, key)}", True, (255, 255, 255))
        all_text_surfaces_left.append(text)

    mouse_text = small_font_left.render(f"Pos Mouse - X: {mouse_x} Y: {mouse_y}", True, (255, 255, 255))
    all_text_surfaces_left.append(mouse_text)
    for idx, human in enumerate(humans):
        lines = [
            f"Human {idx + 1} Pos: (X{human.x}, Y{human.y})",
            f"Direct X: {human.direction_x}, Direct Y: {human.direction_y}",
            f"Sleep-{human.sleep}, rest-{human.rest}, nutrition-{human.nutrition}, vaccination-{human.vaccination}"
        ]
        text_surfaces = [small_font_right.render(line, True, (255, 255, 255)) for line in lines]
        all_text_surfaces_left.extend(text_surfaces)

        text_x_inside = human.x + rect_width // 2
        text_y_inside = human.y + rect_height // 2
        seat_text_inside = small_font_right.render(f"{idx + 1}", True, (255, 255, 255))
        text_rect_inside = seat_text_inside.get_rect(center=(text_x_inside, text_y_inside))
        screen.blit(seat_text_inside, text_rect_inside)


    for text_surface in all_text_surfaces_left:
        text_width, text_height = text_surface.get_size()
        screen.blit(text_surface, (3, text_y_left))
        text_y_left += text_height + 2

    for text_surface in all_text_surfaces_right:
        text_width, text_height = text_surface.get_size()
        screen.blit(text_surface, (screen.get_width() - text_width - 3, text_y_right))
        text_y_right += text_height + 2
    text_y = 10
    for idx, seat in enumerate(seats):
        seat.draw_rect(screen, rect_width, rect_height)
        seat_text = small_font_right.render(f"Seat {idx + 1}: X{seat.x}, Y{seat.y}", True, (255, 255, 255))
        text_rect = seat_text.get_rect(right=screen.get_width() - 10, top=text_y)
        screen.blit(seat_text, text_rect)
        text_y += text_rect.height + 2

        text_x_inside = seat.x + rect_width // 2
        text_y_inside = seat.y + rect_height // 2
        seat_text_inside = small_font_right.render(f"{idx + 1}", True, (255, 255, 255))
        text_rect_inside = seat_text_inside.get_rect(center=(text_x_inside, text_y_inside))
        screen.blit(seat_text_inside, text_rect_inside)


