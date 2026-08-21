import random
import time
from fileinput import filename

import arcade
from arcade import draw_texture_rectangle
from arcade.sprite_list import sprite_list

SCREEN_TITLE = ""
CUBE_HEIGHT = 100

CUBE_WIDTH = 100
ROW = 8
COLUMN = 14
SPEED_PLAYER_1 = 10
SPEED_PLAYER_2 = 10
SPEED_LASER_1 = 2
SPEED_LASER_2 = 5
DURABILITY=5

SCREEN_WIDTH = COLUMN * CUBE_WIDTH
SCREEN_HEIGHT = ROW * CUBE_HEIGHT

class Building(arcade.Sprite):
    def __init__(self, center_x, center_y,type_building):
        super().__init__(filename=("Pictures/pixilart-drawing (8).png" if type_building else "Pictures/pixilart-drawing (6).png"))
        if type_building:
            self.durability=DURABILITY

        else:
            self.durability=DURABILITY+1000000000000000
        self.type_building=type_building
        self.center_x=center_x
        self.center_y=center_y
        self.destroyed=False
    def update(self):
        if not self.destroyed:
            if self.durability<0:


                self.texture=arcade.load_texture("Pictures/Destoed building .png")
                self.destroyed=True
                self.remove_from_sprite_lists()



    """робота  колизии """






class  SecondGozila(arcade.Sprite):
    def __init__(self, center_x, center_y, speed,texture):
        super().__init__(texture,scale=0.75)
        self.center_x = center_x
        self.center_y = center_y

        self.speed = speed

        self.under_speed_effect = False
        self.under_len_effect = False

        self.speed_cd = time.time()
        self.lenght_cd = time.time()

    def update(self):
        old_x = self.center_x
        self.center_x += self.change_x

        if arcade.check_for_collision_with_list(self, window.buildings):

            if self.center_x >old_x:
                self.center_x-=10
            elif self.center_x <old_x:
                self.center_x+=10
        # Движение по Y
        old_y = self.center_y
        self.center_y += self.change_y

        if arcade.check_for_collision_with_list(self, window.buildings):

            if self.center_y >old_y:
                self.center_y-=10
            elif self.center_y <old_y:
                self.center_y+=10






        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left < 0:
            self.left = 0
        if self.top > SCREEN_HEIGHT:
            self.top = SCREEN_HEIGHT
        if self.bottom < 0:
            self.bottom = 0

        if  self.under_speed_effect and time.time() -self.speed_cd >=5:
            self.under_speed_effect = False
            self.speed=SPEED_PLAYER_1





""" класс клон нужны карденаты  текстура  таймер для цвета self.color"""
class FirstGodzilla (arcade.Sprite):
    def __init__(self, center_x, center_y, speed,texture):
        super().__init__(texture, scale=0.75)
        self.center_x = center_x
        self.center_y = center_y

        self.speed = speed

        self.under_speed_effect= False
        self.under_len_effect= False

        self.speed_cd=time.time()
        self.lenght_cd=time.time()

    def update(self):
        old_x = self.center_x
        self.center_x += self.change_x

        if arcade.check_for_collision_with_list(self, window.buildings):

            if self.center_x >old_x:
                self.center_x-=10
            elif self.center_x <old_x:
                self.center_x+=10
        # Движение по Y
        old_y = self.center_y
        self.center_y += self.change_y

        if arcade.check_for_collision_with_list(self, window.buildings):

            if self.center_y >old_y:
                self.center_y-=10
            elif self.center_y <old_y:
                self.center_y+=10






        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left < 0:
            self.left = 0
        if self.top > SCREEN_HEIGHT:
            self.top = SCREEN_HEIGHT
        if self.bottom < 0:
            self.bottom = 0

        if  self.under_speed_effect and time.time() -self.speed_cd >=5:
            self.under_speed_effect = False
            self.speed=SPEED_PLAYER_1

class Lazer (arcade.Sprite):
    def __init__(self, center_x, center_y, speed,angle,under_effect, lazer_owener):
        super().__init__('Pictures/lazer.png', scale=1, )
        self.t = time.time()
        self.center_x = center_x
        self.center_y = center_y
        self.lazer_owener = lazer_owener



        if under_effect:
            self.lazer_lenght=4
        else:
            self.lazer_lenght=2
        spawn_position = 70

        if angle == 0:
            self.center_y += spawn_position
        if angle == 90:
            self.center_x -= spawn_position
        if angle == 180:
            self.center_y -= spawn_position
        if angle == 270:
            self.center_x += spawn_position


        self.width = CUBE_WIDTH*10
        self.height=CUBE_HEIGHT*2
        self.angle = angle
        self.speed=speed
        self.lazer_movement()

    def lazer_movement (self):
        if  self.angle ==0:
            self.change_y = self.speed
        if  self.angle ==90:
            self.change_x = -self.speed
        if  self.angle ==180:
            self.change_y = -self.speed
        if  self.angle ==270:
            self.change_x = self.speed

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        hit_list= arcade.check_for_collision_with_list(self,window.buildings )
        if hit_list:
            for building in hit_list:
                if building.type_building:
                    building.durability-=1
                else:
                    self.kill()


        if self.lazer_owener != window.player1:
            if arcade.check_for_collision(self, window.player1):
                print("PLAYER 1 HIT")
                self.kill()

        if self.lazer_owener != window.player2:
            if arcade.check_for_collision(self, window.player2):
                print("PLAYER 2 HIT")
                self.kill()



        if time.time() - self.t >= self.lazer_lenght:
            self.kill()


class Boost  (arcade.Sprite):
    def __init__(self, center_x, center_y,type,texture):
        super().__init__(texture, scale=0.5)
        self.center_x = center_x
        self.center_y = center_y
        self.type = type

    def update(self):
        ...

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, fullscreen=False)

        print(self.width, self.height)
        """ background """
        self.destroyed_texture =arcade.load_texture("Pictures/Destoed building .png")
        self.background_picture = arcade.load_texture("Pictures/загрузка (1).jpg")
        self.background_weak_building = arcade.load_texture("Pictures/pixilart-drawing (8).png")
        self.background_strong_building = arcade.load_texture("Pictures/pixilart-drawing (6).png")
        self.background_road_vertical = [
            arcade.load_texture("Pictures/pixilart-drawing (10).png "),
            arcade.load_texture("Pictures/pixilart-drawing (10) without car.png"),
            arcade.load_texture("Pictures/pixilart-drawing (10) without car red.png"),
        ]
        self.background_t_turn_left = arcade.load_texture("Pictures/new-road-pixilart.png")
        self.background_t_turn_up = arcade.load_texture("Pictures/new-road-pixilart.png")
        self.background_t_turn_right = arcade.load_texture("Pictures/new-road-pixilart.png")
        self.background_t_turn_down = arcade.load_texture("Pictures/new-road-pixilart.png")
        self.background_turn = arcade.load_texture("Pictures/turn.png")


        self.background_road_horizontal = [
            arcade.load_texture("Pictures/pixilart-drawing (10).png"),
            arcade.load_texture("Pictures/pixilart-drawing (10) without car.png"),
            arcade.load_texture("Pictures/pixilart-drawing (10) without car red.png"),
        ]

        self.hand = None

        self.buildings= arcade.SpriteList()
        self.buildings = arcade.SpriteList()
        self.destroyed_buildings = arcade.SpriteList()
        self.background_4way = arcade.load_texture("Pictures/pixilart-drawing (11).png")
        """all generations """

        self.amount_4way = random.randint(6, 8)
        # 0 - background (default)
        # 1 -road vertical
        # 2 -road horizontal
        # 3 -weak building
        # 4 - Strong building
        # 5 - 4way
        # 6 - t turn left
        # 7 - t turn up
        # 8 t turn right
        # 9 t turn down

        self.map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        ]

        self.spawn_4way()
        # self.spawn_road()
        """ players """
        coord1, coord2 = self.godzilla_spawn()
        x1,y1 = coord1
        x2,y2 = coord2

        self.player1 = FirstGodzilla(center_x=self.find_center(CUBE_WIDTH,x1+1), center_y=SCREEN_HEIGHT-self.find_center(CUBE_HEIGHT,y1+1), speed=SPEED_PLAYER_1,texture="Pictures/blue-godzila-pixilart.png")
        self.player2 = SecondGozila(center_x=self.find_center(CUBE_WIDTH,x2+1), center_y=SCREEN_HEIGHT-self.find_center(CUBE_HEIGHT,y2+1), speed=SPEED_PLAYER_2,texture="Pictures/pixilart-drawing (9).png")



        """ sprite lists """
        self.lasers = arcade.SpriteList()
        self.boost_speed = arcade.SpriteList()
        self.boost_range_laser = arcade.SpriteList()

        self.time=time.time()
    def find_center(self,side,coord):
        return (side*coord-side/2)

    def player1_and_player2_collision_boost(self):


        for boost in self.boost_speed:
            if arcade.check_for_collision(self.player1, boost):
                if boost.type==1:
                    self.player1.speed+=6
                    self.player1.under_speed_effect=True
                    self.player1.speed_cd=time.time()

                if boost.type==2:
                    self.player1.under_len_effect=True
                    self.player1.lenght_cd=time.time()

                boost.kill()

            if arcade.check_for_collision(self.player2, boost):
                if boost.type == 1:
                    self.player2.speed += 6
                    self.player2.under_speed_effect = True
                    self.player2.speed_cd = time.time()

                if boost.type == 2:
                    self.player2.under_len_effect = True
                    self.player2.lenght_cd = time.time()
                boost.kill()




    def spawn_road(self):
        for row in range(ROW):
            for column in range(COLUMN):
                if self.map[row][column] == 5:

                    # ---------- right ---------- #
                    amount_of_road_right = random.randint(2, 5)
                    for numr in range(1, amount_of_road_right + 1):
                        if column + numr < len(self.map[row]):
                            self.map[row][column + numr] = 2

                    # ---------- left ---------- #
                    amount_of_road_left = random.randint(2, 5)
                    for numl in range(1, amount_of_road_left + 1):

                        if column - numl >= 0:
                            self.map[row][column - numl] = 2

                        # ---------- up ---------- #
                    amount_of_road_up = random.randint(2, 5)
                    for numu in range(1, amount_of_road_up + 1):
                        if row - numu >= 0:
                            self.map[row - numu][column] = 1

                        # ---------- down  ---------- #
                    amount_of_road_down = random.randint(2, 5)
                    for numd in range(1, amount_of_road_down + 1):

                        if row + numd < len(self.map):
                            self.map[row + numd][column] = 1

        for row in range(1,ROW-1):
            for column in range(1,COLUMN-1):

                    # ставим перекрёсток
                    if self.map[row][column] in [1, 2] and self.map[row][column - 1] == 2 and self.map[row][
                        column + 1] == 2 and self.map[row + 1][column] == 1 and self.map[row + -1][column] == 1:
                        self.map[row][column] = 5

                    # t нижнюю сторону
                    elif self.map[row - 1][column] == 1 and self.map[row][column - 1] == 2 and self.map[row][
                        column + 1] == 2  and (not  self.map[row+1][column] == 1 or  row==1):
                        self.map[row][column] = 9

                    # t правую сторону
                    elif self.map[row][column + 1] == 2 and self.map[row + 1][column] == 1 and self.map[row - 1][
                        column] == 1 and not self.map[row][column-1] == 2:
                        self.map[row][column] = 8


                    # t верхнюю сторону
                    elif self.map[row + 1][column] == 1 and self.map[row][column - 1] == 2 and self.map[row][
                        column + 1] == 2 and not  self.map[row-1][column] ==1:

                        self.map[row][column] = 7

                    # t левую сторону
                    elif self.map[row][column - 1] == 2 and self.map[row - 1][column] == 1 and self.map[row + 1][
                        column] == 1   and not self.map[row][column+1] == 2:
                        self.map[row][column] = 6

                    elif (  self.map[row][column] in [1, 2] and
                            self.map[row + 1][column] == 1 and
                            self.map[row][column - 1] == 2 and
                            self.map[row - 1][column] != 1 and
                            self.map[row][column + 1] != 2
                    ):
                        self.map[row][column] = 10

                    # Поворот вверх + вправо
                    elif (  self.map[row][column] in [1, 2] and
                            self.map[row +1][column] == 1 and
                            self.map[row][column + 1] == 2 and
                            self.map[row - 1][column] != 1 and
                            self.map[row][column - 1] != 2

                    ):
                        self.map[row][column] = 11

                    # Поворот вниз + вправо
                    elif (  self.map[row][column] in [1, 2] and
                            self.map[row - 1][column] == 1 and
                            self.map[row][column + 1] == 2 and
                            self.map[row +1][column] != 1 and
                            self.map[row][column - 1] != 2
                    ):
                        self.map[row][column] = 12

                    # Поворот вниз + влево
                    elif (  self.map[row][column] in [1, 2] and
                            self.map[row - 1][column] == 1 and
                            self.map[row][column - 1] == 2 and
                            self.map[row + 1][column] != 1 and
                            self.map[row][column + 1] != 2
                    ):
                        self.map[row][column] = 13



        self.map.reverse()
        for cell in self.map:
            print(cell)
        self.spawn_buildings()
    def spawn_4way(self, spawn_rule_up=None):
        self.map = [

            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        # all_points = [(2, 3), (4, 5), (7, 6), (4, 2)]
        #
        # point_y = random.randint(0, ROW - 1)
        # point_x = random.randint(0, COLUMN - 1)
        # all_points.append((point_y, point_x))
        # print(all_points)
        # self.map[point_y][point_x] = 5
        #
        # point_y = random.randint(0, ROW - 1)  # 0
        # point_x = random.randint(0, COLUMN - 1)  # 1


        # if self.map[point_x][point_y] == 0 and self.map[point_x + 1][point_y] == 0 and self.map[point_x - 1][point_y] == 0 and self.map[point_x][point_y + 1] == 0 and self.map[point_x][point_y - 1]:
        #     all_points.append((point_y, point_x))
        #     self.map[point_y][point_x] = 5


        #points=random.randint(5,5)
        #for y in range(ROW):
        #   for x in range(COLUMN):
        #        self.map[x][y] =

        four_way_row_cordinate=random.randint(0,1)

        column_spawn = 0
        for x in range(0,COLUMN+1,4):   # срезаем по 4
            if column_spawn ==3:
                column_spawn=random.randint(1,3)
            else:
                column_spawn=random.randint(0,3) # сколько блоков внутри после...
            if x + column_spawn>=COLUMN:    # не выходил за пределы окна
                column_spawn=random.randint(1,COLUMN-1-x)
                print("wrok")
            row_spawn=random.randint(1,3)   # либо внизу, либо вверху, либо в двух местах

            if row_spawn==1:    # заспавнить только вверху
                while True:
                    choose_y=random.randint(0,ROW//2-1)

                    if choose_y%2==four_way_row_cordinate:
                        self.map[choose_y][x+column_spawn] = 5
                        break
                print(x)
            if row_spawn == 2: # заспавнить только внизу
                while True:
                    choose_y=random.randint( ROW // 2 ,ROW-1)

                    if choose_y%2==four_way_row_cordinate:
                        self.map[choose_y][x+column_spawn] = 5
                        break

            if row_spawn == 3: # заспавнить только в двух местахa
                
                while True:
                    choose_y = random.randint(0,ROW//2-1 )

                    if choose_y % 2 == four_way_row_cordinate:
                        spawn_rule_up = choose_y
                        self.map[spawn_rule_up][x + column_spawn] = 5
                        break
                
                
                self.map[spawn_rule_up][x+column_spawn] = 5


        self.spawn_road()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        # if button == arcade.MOUSE_BUTTON_LEFT:
        #     x_cell = SCREEN_WIDTH // CUBE_WIDTH
        #     y_cell = SCREEN_WIDTH // CUBE_WIDTH
        #     print(x_cell, y_cell)
        #     self.map[y_cell][x_cell] = self.hand
        # else:
        #     if self.hand < 9:
        #         self.hand += 1
        #     else:
        #         self.hand = 0

        if button == arcade.MOUSE_BUTTON_LEFT:
            laser=Lazer(
                center_x=self.player1.center_x,
                center_y=self.player1.center_y,
                speed=SPEED_LASER_1,
                angle=self.player1.angle,
                under_effect=self.player1.under_len_effect,
                lazer_owener=self.player1
            )
            self.lasers.append(laser)


        if button == arcade.MOUSE_BUTTON_RIGHT:
            laser = Lazer(
                center_x=self.player2.center_x,
                center_y=self.player2.center_y,
                speed=SPEED_LASER_1,
                angle=self.player2.angle,
                under_effect=self.player2.under_len_effect,
                lazer_owener = self.player2
            )

            self.lasers.append(laser)


    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.close()

        if symbol == arcade.key.SPACE:
            self.spawn_4way()


        if symbol == arcade.key.W:
            self.player1.change_y = self.player1.speed
            self.player1.angle=0
        if symbol == arcade.key.A:
            self.player1.change_x = -self.player1.speed
            self.player1.angle = 90
        if symbol == arcade.key.S:
            self.player1.change_y = -self.player1.speed
            self.player1.angle = 180
        if symbol == arcade.key.D:
            self.player1.change_x = self.player1.speed
            self.player1.angle = 270

        if symbol == arcade.key.UP:
            self.player2.change_y = self.player2.speed
            self.player2.angle = 0
        if symbol == arcade.key.LEFT:
            self.player2.change_x = -self.player2.speed
            self.player2.angle = 90
        if symbol == arcade.key.DOWN:
            self.player2.change_y = -self.player2.speed
            self.player2.angle = 180

        if symbol == arcade.key.RIGHT:
            self.player2.change_x = self.player2.speed
            self.player2.angle = 270


    def on_key_release(self, symbol: int, modifiers: int):

        if symbol == arcade.key.W:
            self.player1.change_y = 0
        if symbol == arcade.key.A:
            self.player1.change_x = 0
        if symbol == arcade.key.S:
            self.player1.change_y = 0
        if symbol == arcade.key.D:
            self.player1.change_x = 0

        if symbol == arcade.key.UP:
            self.player2.change_y = 0
        if symbol == arcade.key.LEFT:
            self.player2.change_x = 0
        if symbol == arcade.key.DOWN:
            self.player2.change_y = 0
        if symbol == arcade.key.RIGHT:
            self.player2.change_x = 0
    def spawn_buildings(self):
        self.clear((255, 255, 255))
        for y in range(ROW):
            for x in range(COLUMN):
                if self.map[y][x] == 0:

                    new_building = Building(center_x=x * CUBE_WIDTH + CUBE_WIDTH / 2,
                                            center_y=SCREEN_HEIGHT - (y * CUBE_HEIGHT + CUBE_HEIGHT / 2),
                                            type_building=random.randint(0, 1))
                    self.buildings.append(new_building)

    def on_draw(self):
        self.clear((0,0 ,0 ))
        self.draw_background()
        self.buildings.draw()
        for y in range(ROW):
            for x in range(COLUMN):
                if self.map[y][x] == 0:
                  pass

                elif self.map[y][x] == 1:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2,  SCREEN_HEIGHT-(y * CUBE_HEIGHT + CUBE_HEIGHT / 2),
                                                  CUBE_WIDTH, CUBE_HEIGHT,
                                                  self.background_road_vertical[random.randint(0, 0)], )
                elif self.map[y][x] == 2:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2,  SCREEN_HEIGHT-(y * CUBE_HEIGHT + CUBE_HEIGHT / 2),
                                                  CUBE_WIDTH, CUBE_HEIGHT,
                                                  self.background_road_horizontal[random.randint(0, 0)], angle=90)
                elif self.map[y][x] == 3:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2,  SCREEN_HEIGHT-(y * CUBE_HEIGHT + CUBE_HEIGHT / 2),
                                                  CUBE_WIDTH, CUBE_HEIGHT, self.background_weak_building, )
                elif self.map[y][x] == 4:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2,  SCREEN_HEIGHT-(y * CUBE_HEIGHT + CUBE_HEIGHT / 2),
                                                  CUBE_WIDTH, CUBE_HEIGHT, self.background_strong_building, )
                elif self.map[y][x] == 5:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2,  SCREEN_HEIGHT-(y * CUBE_HEIGHT + CUBE_HEIGHT / 2),
                                                  CUBE_WIDTH, CUBE_HEIGHT, self.background_4way, )

                elif self.map[y][x] == 6:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2,  SCREEN_HEIGHT-(y * CUBE_HEIGHT + CUBE_HEIGHT / 2),
                                                  CUBE_WIDTH, CUBE_HEIGHT, self.background_t_turn_left, angle=0)
                elif self.map[y][x] == 7:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2,  SCREEN_HEIGHT-(y * CUBE_HEIGHT + CUBE_HEIGHT / 2),
                                                  CUBE_WIDTH, CUBE_HEIGHT, self.background_t_turn_up, angle=270)
                elif self.map[y][x] == 8:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2,  SCREEN_HEIGHT-(y * CUBE_HEIGHT + CUBE_HEIGHT / 2),
                                                  CUBE_WIDTH, CUBE_HEIGHT, self.background_t_turn_right, angle=180)
                elif self.map[y][x] == 9:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2, SCREEN_HEIGHT- (y * CUBE_HEIGHT + CUBE_HEIGHT / 2),
                                                  CUBE_WIDTH, CUBE_HEIGHT, self.background_t_turn_down, angle=90)
                elif self.map[y][x] == 10:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2,
                                    SCREEN_HEIGHT - (y * CUBE_HEIGHT + CUBE_HEIGHT / 2),width=CUBE_WIDTH,height=CUBE_HEIGHT, angle=0,
                                    texture=self.background_turn)


                elif self.map[y][x] == 11:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2,
                                    SCREEN_HEIGHT - (y * CUBE_HEIGHT + CUBE_HEIGHT / 2),width=CUBE_WIDTH,height=CUBE_HEIGHT, angle=270,
                                    texture=self.background_turn)


                elif self.map[y][x] == 12:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2,
                                    SCREEN_HEIGHT - (y * CUBE_HEIGHT + CUBE_HEIGHT / 2),width=CUBE_WIDTH,height=CUBE_HEIGHT, angle=180,
                                    texture=self.background_turn)

                elif self.map[y][x] == 13:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2,
                                    SCREEN_HEIGHT - (y * CUBE_HEIGHT + CUBE_HEIGHT / 2),width=CUBE_WIDTH,height=CUBE_HEIGHT, angle=90,
                                    texture=self.background_turn)






        self.player1.draw()
        self.player2.draw()
        self.lasers.draw()
        self.boost_range_laser.draw()
        self.boost_speed.draw()
        self.buildings.draw()

    def draw_background(self):
        for x in range(COLUMN):
            for y in range(ROW):
                arcade.draw_texture_rectangle(self.find_center(CUBE_WIDTH,x+1),self.find_center(CUBE_HEIGHT,y+1),CUBE_WIDTH,CUBE_HEIGHT
                                              ,self.destroyed_texture)


    def godzilla_spawn(self):
        coords=[]
        for x in range(COLUMN):
            for y in range(ROW):
                if self.map[y][x]==5:
                    coords.append((x,y))
        godzilla_1_spawn =random.choice(coords)

        coords.remove(godzilla_1_spawn)
        godzilla_2_spawn = random.choice(coords)
        return godzilla_1_spawn,godzilla_2_spawn






    def update(self, delta_time):

        self.player1.update()
        self.player2.update()
        self.lasers.update()
        self.boost_range_laser.update()
        self.boost_speed.update()
        self.player1_and_player2_collision_boost()

        self.buildings.update()



        if time.time() - self.time >= 2:
            x_random = random.randint(0,COLUMN-1)
            y_random  = random.randint(0,ROW-1)
            type_random =random.randint(1,2)


            if type_random == 1:
                boost = Boost(center_x=x_random * CUBE_WIDTH + CUBE_HEIGHT / 2,
                              center_y=y_random * CUBE_HEIGHT + CUBE_HEIGHT / 2, type=1,
                              texture="Pictures/Speed_potion.png")


            if type_random == 2:
                boost = Boost(center_x=x_random * CUBE_WIDTH + CUBE_HEIGHT / 2,
                              center_y=y_random * CUBE_HEIGHT + CUBE_HEIGHT / 2, type=2,
                              texture="Pictures/lengght potion.png")
            self.boost_speed.append(boost)
            self.time = time.time()



window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()