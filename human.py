from settings import *
import random


class Human:
    def __init__(self, x, y, direction_x, direction_y, sleep_param, rest_param, nutrition_param, vaccination_param,
                 radius=26):
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
        self.is_moving_to_point = False
        self.radius = radius
        self.color = (0, 0, 0)
        self.health = 0

    def draw_circle(self, screen_param):
        # Нормализуем параметры, чтобы они были в пределах от 0 до 255
        self.health = int((self.sleep + self.rest + self.nutrition + self.vaccination) / 4)
        if self.health <= 40:
            color = (255, 0, 0)
        else:
            color = (0, 125, 0)
        pg.draw.circle(screen_param, color, (self.x + 30 // 2, self.y + 30 // 2), self.radius, 1)

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
            if not self.target_seat or self.target_seat.is_occupied():
                # Если у человека нет текущего целевого места или оно занято, выбираем новое место
                available_seats = [seat for seat in seats if not seat.is_occupied()]
                if available_seats:
                    self.target_seat = random.choice(available_seats)

    @staticmethod
    def get_available_seats(all_seats):
        # Возвращает список доступных мест
        return [seat for seat in all_seats if seat.is_vacant()]

    def move_towards_target(self, all_seats, seat_radius=1):
        if not self.on_seat:
            if not self.target_seat:
                # Если у человека нет текущего целевого места, выбираем новое внутри автобуса
                available_seats = [seat for seat in all_seats if not seat.is_occupied()]
                if available_seats:
                    self.target_seat = random.choice(available_seats)
                    self.is_moving_to_point = True  # Устанавливаем флаг в True, чтобы начать движение к точке

            if self.target_seat and self.is_moving_to_point:
                # Двигаемся к точке (например, (1135, 800))
                target_point = (1135, 800)
                distance_to_point = ((self.x - target_point[0]) ** 2 + (self.y - target_point[1]) ** 2)

                if distance_to_point <= seat_radius:
                    # Дошли до точки, меняем состояние
                    self.is_moving_to_point = False
                else:
                    # Продолжаем двигаться к точке только по оси X
                    x_difference = target_point[0] - self.x
                    self.direction_x = 1 if x_difference > 0 else -1
                    self.direction_y = 0  # Устанавливаем направление по оси Y в 0

            elif self.target_seat and not self.is_moving_to_point:
                # Ваш текущий код для движения к месту
                target_x, target_y = self.target_seat.x, self.target_seat.y
                distance_to_target = ((self.x - target_x) ** 2 + (self.y - target_y) ** 2)

                if distance_to_target <= seat_radius:
                    print("Человек пришел на свое место!")
                    self.target_seat.occupy_seat()
                    self.on_seat = True
                    self.direction_x = 0
                    self.direction_y = 0
                else:
                    x_difference = target_x - self.x
                    y_difference = target_y - self.y
                    if abs(y_difference) > 0:
                        self.direction_x = 0
                        self.direction_y = 1 if y_difference > 0 else -1
                    elif abs(x_difference) > 0:
                        self.direction_x = 1 if x_difference > 0 else -1
                        self.direction_y = 0

    def check_collision_with_circles(self, other_human):
        # Проверка столкновения кругов
        distance = ((self.x - other_human.x) ** 2 + (self.y - other_human.y) ** 2) ** 0.5
        if distance <= self.radius + other_human.radius:
            if self.color == (255, 0, 0) and (other_human.color == (255, 255, 0) or other_human.color == (0, 125, 0)):
                # Если текущий круг красный, а другой - желтый или зеленый, меняем цвет обоих кругов на красный
                self.change_color((255, 0, 0))
                other_human.change_color((255, 0, 0))
            return True
        else:
            return False

    def change_color(self, new_color):
        # Меняем цвет на новый
        self.color = new_color

    def __str__(self):
        return (f"[{self.x}, {self.y}, {self.sleep}, {self.rest}, {self.nutrition}, {self.vaccination}, "
                f"{self.direction_x}, {self.direction_y}, {self.sit_on_seat_available}, {self.target_seat}, "
                f"{self.on_seat}]")
