import pygame as pg
from human import Human
import random
pg.init()
clock = pg.time.Clock()
paused = False
spawn_timer = pg.time.get_ticks()
pg.display.set_caption("SimulationVirus")
screen_width, screen_height = 1720, 920
screen = pg.display.set_mode((screen_width, screen_height))
bus_outline_color = (255, 0, 0)

humans = [Human(0, 800, 1, 0, random.randint(0, 100),
                random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))]
sleep = 0
rest = 0
nutrition = 0
vaccination = 0
speed = 2
rect_width = 30
rect_height = 30
sit_horizont = 2
sit_vertical = 11
mouse_x, mouse_y = 0, 0
all_sit = (sit_horizont * sit_vertical)
bus = pg.Rect(1000, 100, 300, 740)
time_spawn = 2000
left_side_bus = 780
