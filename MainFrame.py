import pygame
import random
import copy
import os
import time


class MainFrame:
    def __init__(self, row, column):
        self.GameMap = [[0 for i in range(column)] for j in range(row)]
        self.NextMap = [[0 for i in range(column)] for j in range(row)]
        self.GameStatus = 0
        self.Row = row
        self.Column = column

    def random_init(self):
        for i in range(self.Row):
            for j in range(self.Column):
                self.GameMap[i][j] = random.randint(0, 2) % 2

    def get_neighbor(self, x, y):
        num = 0
        for i in range(3):
            for j in range(3):
                if i == j and i == 1:
                    continue
                else:
                    num += self.GameMap[(x - 1 + i) % self.Row][(y - 1 + j) % self.Column]
        return num

    def change_status(self, x, y):
        num = self.get_neighbor(x, y)
        if num == 3:
            self.NextMap[x][y] = 1
        elif num != 2:
            self.NextMap[x][y] = 0
        else:
            self.NextMap[x][y] = self.GameMap[x][y]

    def next_phrase(self):
        for i in range(self.Row):
            for j in range(self.Column):
                self.change_status(i, j)
        self.GameMap = copy.deepcopy(self.NextMap)

    def reset(self):
        for i in range(self.Row):
            for j in range(self.Column):
                self.GameMap[i][j] = 0


'''   def show_cmd(self):
        for tmp in range(1000):
            os.system("cls")
            for i in range(self.Row):
                for j in range(self.Column):
                    if self.GameMap[i][j] == 1 :
                        print("■",end="")
                    else :
                        print("□", end="")
                print("")
            time.sleep(0.5)
            self.next_phrase()'''

# frame = MainFrame(30,30)
# frame.GameMap[1][2] = 1
# frame.GameMap[2][3] = 1
# frame.GameMap[3][1] = 1
# frame.GameMap[3][2] = 1
# frame.GameMap[3][3] = 1
# frame.show_cmd()
