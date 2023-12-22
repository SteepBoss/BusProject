import pygame as pg
class Human:
    def __init__(self, x, y, direction_x, direction_y):
        self.x = x
        self.y = y
        self.direction_x = direction_x
        self.direction_y = direction_y
    def update_position(self, speed):
        self.x += speed * self.direction_x
        self.y += speed * self.direction_y
    def handle_collision(self, bus):
        if bus.colliderect(pg.Rect(self.x, self.y, 30, 30)):
            if self.direction_x == 1 and self.x + 30 > bus.right - 135:
                self.direction_y = -1
                self.direction_x = 0
                self.x = bus.right - 165
            if self.direction_x == 1 and self.x + 30 > bus.right:
                self.direction_y = -1
                self.x = bus.right - 30
            if self.direction_y == -1 and self.y < bus.top:
                self.direction_y *= -1
                self.direction_x = 0
            elif self.direction_y == 1 and self.y + 30 > bus.bottom:
                self.direction_y *= -1
                self.direction_x = 0