import random

import arcade

SCREEN_TITLE = ""
CUBE_HEIGHT = 100

CUBE_WIDTH = 100
ROW = 8
COLUMN = 14

SCREEN_WIDTH = COLUMN * CUBE_WIDTH
SCREEN_HEIGHT = ROW * CUBE_HEIGHT


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, fullscreen=False)

        print(self.width, self.height)
        """ background """
        self.background_picture = arcade.load_texture("Pictures/загрузка (1).jpg")
        self.background_weak_building = arcade.load_texture("Pictures/pixilart-drawing (8).png")
        self.background_strong_building = arcade.load_texture("Pictures/pixilart-drawing (6).png")
        self.background_road_vertical = [
            arcade.load_texture("Pictures/pixilart-drawing (10).png "),
            arcade.load_texture("Pictures/pixilart-drawing (10) without car.png"),
            arcade.load_texture("Pictures/pixilart-drawing (10) without car red.png"),
        
        ]
        self.background_road_horizontal  = [
            arcade.load_texture("Pictures/pixilart-drawing (10).png"),
            arcade.load_texture("Pictures/pixilart-drawing (10) without car.png"),
            arcade.load_texture("Pictures/pixilart-drawing (10) without car red.png"),
        ]

        self.background_4way = arcade.load_texture("Pictures/pixilart-drawing (11).png")
        """all generations """

        self.amount_4way=random.randint(4,7)
        # 0 - background (default)
        # 1 -road vertical
        # 2 -road horizontal
        # 3 -weak building
        # 4 - Strong building
        # 5 - 4way
        # 6 - t turn left
        # 7 - t turn up
        # 8 t turn right
        #9 t turn down

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
        self.spawn_road()





        for row in range(ROW):
            for column in range(COLUMN):
                if self.map[row][column]==5:
                    # ---------- right ---------- #
                    amount_of_road_right=random.randint(1,3)
                    for numr in range(1,amount_of_road_right+1):
                        if column +numr <len(self.map[row]) :
                            self.map [row][column+numr]=2

                    # ---------- left ---------- #
                    amount_of_road_left = random.randint(1, 3)
                    for numl in range(1, amount_of_road_left + 1):

                             if column-numl >= 0:
                                self.map[row][column - numl] = 2

                             # ---------- up ---------- #
                    amount_of_road_up = random.randint(1, 3)
                    for numu in range(1, amount_of_road_up + 1):
                        if row - numu >= 0:
                            self.map[row-numu][column ] = 1

                        # ---------- down  ---------- #
                    amount_of_road_down = random.randint(1, 3)
                    for numd in range(1, amount_of_road_down + 1):

                        if row + numd < len(self.map):
                            self.map[row+numd][column] = 1





        self.map.reverse()

    def spawn_4way(self):
        self.map = [
            [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        # for way in range(self.amount_4way):
        #     self.map[random.randint(0,ROW-1)][random.randint(0,COLUMN-1)]=5
        column_spawn = 0
        filled_rows = [(0, 1), (4, 1),]#  что бы не попадались на одинаковом row


        for x in range(0,COLUMN+1,4):   # срезаем по 4
            if column_spawn ==3:
                column_spawn=random.randint(1,3)
            else:
                column_spawn=random.randint(0,3) # сколько блоков внутри после...
            if x + column_spawn>=COLUMN:    # не выходил за пределы окна
                column_spawn=random.randint(1,COLUMN-1-x)

            row_spawn=random.randint(1,3)   # либо внизу, либо вверху, либо в двух местах

            if row_spawn==1:    # заспавнить только вверху
                self.map[random.randint(0,ROW//2-1)][x+column_spawn] = 5
                print(x)
            if row_spawn == 2: # заспавнить только внизу
                self.map[random.randint( ROW // 2 ,ROW-1)][x+column_spawn] = 5
            if row_spawn == 3: # заспавнить только в двух местах
                spawn_rule_up=random.randint(0,ROW//2-1 )
                self.map[spawn_rule_up][x+column_spawn] = 5
                if ROW-1//2==spawn_rule_up: # чтобы не заходил за карту
                    self.map[random.randint( ROW // 2 +1,ROW-1)][x+column_spawn] = 5
                else:
                    self.map[random.randint( ROW // 2 ,ROW-1)][x+column_spawn] = 5

        self.spawn_road()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            x_cell = SCREEN_WIDTH // CUBE_WIDTH
            y_cell = SCREEN_WIDTH // CUBE_WIDTH
            print(x_cell, y_cell)
            self.map[y_cell][x_cell] = self.hand
        else:
            if self.hand < 9:
                self.hand += 1
            else:
                self.hand = 0
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.close()

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.spawn_4way()

    def on_draw(self):
        self.clear((255, 255, 255))
        for y in range(ROW):
            for x in range(COLUMN):

                if self.map [y][x]==0:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2, y * CUBE_HEIGHT + CUBE_HEIGHT / 2,
                                                CUBE_WIDTH, CUBE_HEIGHT, self.background_picture, )
                if self.map[y][x] ==1 :
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2, y * CUBE_HEIGHT + CUBE_HEIGHT / 2,
                                                  CUBE_WIDTH, CUBE_HEIGHT, self.background_road_vertical[random.randint(0, 0)], )
                    # TODO: CHECK IT LATER
                if self.map[y][x] == 2:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2, y * CUBE_HEIGHT + CUBE_HEIGHT / 2,
                                                  CUBE_WIDTH, CUBE_HEIGHT, self.background_road_horizontal[random.randint(0,0)], angle= 90)
                if self.map[y][x] == 3:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2, y * CUBE_HEIGHT + CUBE_HEIGHT / 2,
                                                  CUBE_WIDTH, CUBE_HEIGHT, self.background_weak_building, )
                if self.map[y][x] == 4:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2, y * CUBE_HEIGHT + CUBE_HEIGHT / 2,
                                                  CUBE_WIDTH, CUBE_HEIGHT, self.background_strong_building, )
                if self.map[y][x] == 5:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2, y * CUBE_HEIGHT + CUBE_HEIGHT / 2,
                                                  CUBE_WIDTH, CUBE_HEIGHT, self.background_4way, )

                if self.map[y][x] == 6:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2, y * CUBE_HEIGHT + CUBE_HEIGHT / 2,
                                                  CUBE_WIDTH, CUBE_HEIGHT, self.background_t_turn_left, angle=0)
                if self.map[y][x] == 7:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2, y * CUBE_HEIGHT + CUBE_HEIGHT / 2,
                                                  CUBE_WIDTH, CUBE_HEIGHT, self.background_t_turn_up, angle=270)
                if self.map[y][x] == 8:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2, y * CUBE_HEIGHT + CUBE_HEIGHT / 2,
                                                  CUBE_WIDTH, CUBE_HEIGHT, self.background_t_turn_right,angle=180 )
                if self.map[y][x] == 9:
                    arcade.draw_texture_rectangle(x * CUBE_WIDTH + CUBE_WIDTH / 2, y * CUBE_HEIGHT + CUBE_HEIGHT / 2,
                                                  CUBE_WIDTH, CUBE_HEIGHT, self.background_t_turn_down, angle=90)


    def on_update(self, delta_time):
        pass


window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
