from settings import *


class Human:
    def __init__(self, x, y, direction_x, direction_y, sleep_param, rest_param, nutrition_param, vaccination_param):
        self.x = x
        self.y = y
        self.sleep = sleep_param
        self.rest = rest_param
        self.nutrition = nutrition_param
        self.vaccination = vaccination_param
        self.direction_x = direction_x
        self.direction_y = direction_y

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def update_position(self, speed_param):
        self.x += speed_param * self.direction_x
        self.y += speed_param * self.direction_y

    def handle_collision(self, bus_param):
        if bus_param.colliderect(pg.Rect(self.x, self.y, 30, 30)):
            if self.direction_x == 1 and self.direction_y == 0 and self.x >= 1135:
                print("направление вверх при ударе 1135 справа")
                print(self.x, self.y)
                self.x = 1135
                self.direction_x = 0
                self.direction_y = -1
            elif self.direction_x == 0 and self.direction_y == -1 and self.y <= 700:
                print("стоп")
                self.x = 1030
                self.y = 130
                self.direction_x = 0
                self.direction_y = 0

                print(self.x, self.y)
            # elif self.direction_x == 0 and self.direction_y == -1 and self.y <= bus.top:
            #     print("Направление вниз")
            #     print(self.x, self.y)
            #     self.direction_y = 1# Изменение направления на вниз
            #     self.direction_x = 0
            # elif self.direction_x == 0 and self.direction_y == 1 and self.y + 30 >= bus.bottom:
            #     print("Направление вверх")
            #     print(self.x, self.y)
            #     self.direction_y = -1# Изменение направления на вверх
            #     self.direction_x = 0
