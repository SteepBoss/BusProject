from settings import *
import random

class Human:
    def __init__(self, x, y, direction_x, direction_y, sleep, rest, nutrition, vaccination):
        self.x = x
        self.y = y
        self.sleep = sleep
        self.rest = rest
        self.nutrition = nutrition
        self.vaccination = vaccination
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.in_bus = False
    def enter_bus(self):
        self.in_bus = True
    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def update_position(self, speed):
        self.x += speed * self.direction_x
        self.y += speed * self.direction_y

    def handle_collision(self, bus):
        if bus.colliderect(pg.Rect(self.x, self.y, 30, 30)):
            if self.direction_x == 0 and self.direction_y == 0:
                self.direction_x = 1
                self.direction_y = 0
                print("Condition 1 is true")
            elif self.direction_x == 1 and self.direction_y == 0 and self.x >= 1135:
                print("направление вверх при ударе 1135 с права")
                print(self.x, self.y)
                self.x = 1135
                self.direction_x = 0
                self.direction_y = -1
            elif self.direction_x == 0 and self.direction_y == -1 and self.y <= bus.top:
                print("Направление вниз")
                print(self.x, self.y)
                self.direction_y = 1  # Изменение направления на вниз
                self.direction_x = 0
            elif self.direction_x == 0 and self.direction_y == 1 and self.y + 30 >= bus.bottom:
                print("Направление вверх")
                print(self.x, self.y)
                self.direction_y = -1  # Изменение направления на вверх
                self.direction_x = 0
