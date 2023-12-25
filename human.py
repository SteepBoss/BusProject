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
        self.sit_on_seat_available = False
        self.target_seat = None
        self.on_seat = False

    def sit_on_seat(self, seat):
        if self.sit_on_seat_available:
            self.x, self.y = seat.x + rect_width // 2, seat.y + rect_height // 2
            seat.occupy_seat()
            self.sit_on_seat_available = False  # Человек сел на место, теперь оно недоступно

    def update_position(self, speed_param):
        self.x += speed_param * self.direction_x
        self.y += speed_param * self.direction_y

    def handle_collision(self, bus_param, seats):
        if bus_param.colliderect(pg.Rect(self.x, self.y, 30, 30)):
            target_seat = self.find_next_seat(seats)
            if target_seat:
                self.target_seat = target_seat

    def find_next_seat(self, seats):
        min_distance = float('inf')  # Используем бесконечность для сравнения расстояний
        target_seat = None

        for seat in seats:
            if not seat.is_occupied():
                distance = ((self.x - seat.x) ** 2 + (self.y - seat.y) ** 2) ** 0.5
                if distance < min_distance:
                    min_distance = distance
                    target_seat = seat

        return target_seat

    def move_towards_target(self, seat_radius=15):  # Параметр seat_radius - радиус места
        if self.target_seat and not self.on_seat:  # Проверяем флаг on_seat
            target_x, target_y = self.target_seat.x, self.target_seat.y
            distance_to_target = ((self.x - target_x) ** 2 + (self.y - target_y) ** 2)

            if distance_to_target <= seat_radius:  # Если человек пришел на свое место
                print("Человек пришел на свое место!")
                self.target_seat.occupy_seat()  # Занимаем место
                self.on_seat = True  # Устанавливаем флаг on_seat в True, чтобы остановить движение
                self.direction_x = 0
                self.direction_y = 0
            else:
                x_difference = target_x - self.x
                y_difference = target_y - self.y
                if abs(x_difference) > 0:
                    # Двигаемся вдоль оси X
                    self.direction_x = 1 if x_difference > 0 else -1
                    self.direction_y = 0
                elif abs(y_difference) > 0:
                    # Двигаемся вдоль оси Y только если разница по оси X равна 0
                    self.direction_x = 0
                    self.direction_y = 1 if y_difference > 0 else -1
