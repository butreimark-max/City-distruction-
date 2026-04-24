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
        self.map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
            [0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, ],
            [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, ],
        ]

        #self.spawn_4way()


        for row in range(ROW):
            for column in range(COLUMN):
                if self.map[row][column]==5:
                    # ---------- right ---------- #
                    amount_of_road_right=random.randint(1,3)
                    for numr in range(1,amount_of_road_right+1):
                        if column +numr <len(self.map[row]) :
                            self.map [row][column+numr]=2

                    # ---------- left ---------- #
                    # amount_of_road_left = random.randint(1, 3)
                    # for numl in range(1, amount_of_road_left + 1):
                    #     if column + numr < len(self.map[row]):
                    #         self.map[row][column - numr] = 2


                    break






        self.map.reverse()

    def spawn_4way(self):
        for way in range(self.amount_4way):
            self.map[random.randint(0,ROW-1)][random.randint(0,COLUMN-1)]=5

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            self.close()

    def on_key_release(self, symbol: int, modifiers: int):
        pass

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

    def on_update(self, delta_time):
        pass


window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
