from settings import *


class Seat:
    count = 0

    def __init__(self, x, y):
        self.count = 0
        self.x = x
        self.y = y

    def set_count(self, count):
        self.count = count

    def __str__(self):
        return f"[{self.count}, {self.x}, {self.y}]"

    def draw_rect(self, screen, rect_width, rect_height):
        pg.draw.rect(screen, (255, 0, 0), (self.x, self.y, rect_width, rect_height))

    def draw_seats(seats, screen):
        font = pg.font.Font(None, 10)
        for seat in seats:
            seat_text = font.render(f"Seat at (X{seat.x}, Y{seat.y})", True, (255, 255, 255))
            screen.blit(seat_text, (seat.x, seat.y))

