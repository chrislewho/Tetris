import pygame
import pygame.freetype
import numpy as np
from random import randint


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

class Tetromino:
    def __init__(self):
        self.coordinates = []
        self.orientation = 0

    def define_coordinates(self):
        if self.shape == "L":
            if self.orientation ==0 or self.orientation ==2:
                self.coordinates = [[0,0],[0,1],[0,2],[0,3]]
            elif self.orientation==1 or self.orientation ==3:
                self.coordinates = [[0, 0], [1, 0], [2, 0], [3, 0]]

    def rotate(self):
        self.orientation +=1
        if self.orientation>3:
            self.orientation = 0
        self.define_coordinates(self)

class L_tet(Tetromino):
    def __init__(self):
        self.coordinates = np.array([[0,0],[0,1],[0,2],[1,0]])
        self.orientation = 0
        self.position = np.array([5,5])

    def define_coordinates(self):
        if self.orientation == 0 or self.orientation == 2:
            self.coordinates = np.array([[0, 0], [0, 1], [0, 2], [0, 3]])
        elif self.orientation == 1 or self.orientation == 3:
            self.coordinates = np.array([[0, 0], [1, 0], [2, 0], [3, 0]])

class Tetris:

    def __init__(self):
        self.display = pygame.display.set_mode(dispbound)
        self.game_window = [200,200]
        self.quit_game = False
        self.block_size =10
        self.velocity = np.array([0,-1])

    def displaypiece(self,piece):
        size_arr = np.array([self.block_size,self.block_size])
        for coord in piece.coordinates:
            coord_pos = (piece.position + coord) * self.block_size
            block_Rect = [coord_pos, size_arr]
            pygame.draw.rect(self.display, BLUE, block_Rect)


    def mainloop(self):
        my_piece = L_tet()
        while not self.quit_game:
            pygame.time.delay(2000)
            self.display.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game = True

            self.displaypiece(my_piece)

            my_piece.position -= self.velocity
            pygame.display.update()


        pygame.quit()




if __name__ == '__main__':
    pygame.init()  # Initialize display
    pygame.font.init()
    stdfont = pygame.freetype.SysFont("timesnewroman", 20)
    # Display variables
    dispbound = [800, 600]
    gamebound = list(np.subtract(dispbound, [10, 10]))
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    GREEN = (0, 128, 0)

    clock = pygame.time.Clock()

    shapelist = ["T","L","L_inv","Line","Square","Z","Z_inv"]
    game_instance = Tetris()
    game_instance.mainloop()


