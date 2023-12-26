import pygame as pg


class Seat:
    count = 0

    def __init__(self, x, y):
        self.count = 0
        self.x = x
        self.y = y
        self.occupied = False

    def is_vacant(self):
        return not self.occupied

    def set_count(self, count):
        self.count = count

    def draw_rect(self, screen_param, rect_width_param, rect_height_param):
        color = (255, 0, 0) if not self.occupied else (0, 128, 0)
        pg.draw.rect(screen_param, color, (self.x, self.y, rect_width_param, rect_height_param))

    def occupy_seat(self):
        self.occupied = True

    def is_occupied(self):
        return self.occupied

    @staticmethod
    def draw_seats(seats, screen_param):
        font = pg.font.Font(None, 10)
        for seat in seats:
            seat_text = font.render(f"Seat at (X{seat.x}, Y{seat.y})", True, (255, 255, 255))
            screen_param.blit(seat_text, (seat.x, seat.y))

    def __str__(self):
        return f"[{self.count}, {self.x}, {self.y}, {self.occupied}]"
