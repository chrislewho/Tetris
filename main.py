import pygame
import pygame.freetype
import numpy as np
from random import randint


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

class Tetromino:
    def __init__(self):
        self.block_coordinates = []
        self.orientation = 0

    def define_block_coordinates(self):
        if self.shape == "L":
            if self.orientation ==0 or self.orientation ==2:
                self.block_coordinates = [[0,0],[0,1],[0,2],[0,3]]
            elif self.orientation==1 or self.orientation ==3:
                self.block_coordinates = [[0, 0], [1, 0], [2, 0], [3, 0]]

    def rotate(self):
        self.orientation +=1
        if self.orientation>3:
            self.orientation = 0
        self.define_block_coordinates(self)

class L_tet(Tetromino):
    def __init__(self):
        self.block_coordinates = np.array([[0,0],[0,1],[0,2],[1,0]])
        self.orientation = 0
        self.position = np.array([5,5])

    def define_block_coordinates(self):
        if self.orientation == 0 or self.orientation == 2:
            self.block_coordinates = np.array([[0, 0], [0, 1], [0, 2], [0, 3]])
        elif self.orientation == 1 or self.orientation == 3:
            self.block_coordinates = np.array([[0, 0], [1, 0], [2, 0], [3, 0]])

class Tetris:

    def __init__(self):
        self.display = pygame.display.set_mode(dispbound)
        self.game_window = [200,200]
        self.quit_game = False
        self.velocity = np.array([0,-1])
        self.board_dimensions = np.array([10, 20])
        self.board_position = np.array([50,50])

    def displaypiece(self,piece):
        size_arr = np.array([block_size,block_size])
        for coord in piece.block_coordinates:
            coord_pos = (piece.position + coord) * block_size
            block_Rect = [coord_pos, size_arr]
            pygame.draw.rect(self.display, BLUE, block_Rect)


    def drawboard(self):
        board_bounds = self.board_dimensions *block_size
        boundary_rect = [self.board_position ,board_bounds]
        pygame.draw.rect(self.display,BLACK,boundary_rect,3)
        for x_idx in range(0,self.board_dimensions[0]):
            start = [self.board_position[0]+x_idx *block_size, self.board_position[1]]
            end = [self.board_position[0] + x_idx *block_size, self.board_position[1] + block_size*self.board_dimensions[1]]
            pygame.draw.line(self.display,BLACK,start,end)
        for y_idx in range(0,self.board_dimensions[1]):
            start = [self.board_position[0],self.board_position[1] + y_idx*block_size]
            end = [self.board_position[0]+ block_size*self.board_dimensions[0],
                   self.board_position[1]+y_idx*block_size]
            pygame.draw.line(self.display, BLACK, start, end)

    def detectcollision(self,piece):
        return

    def mainloop(self):
        my_piece = L_tet()
        while not self.quit_game:
            pygame.time.delay(2000)
            self.display.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        return
                    if event.key == pygame.K_RIGHT:
                        return
                    if event.key == pygame.K_UP:
                        return
                    if event.key == pygame.K_DOWN:
                        return

            self.displaypiece(my_piece)
            self.drawboard()
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
    block_size = 10

    clock = pygame.time.Clock()

    shapelist = ["T","L","L_inv","Line","Square","Z","Z_inv"]
    game_instance = Tetris()
    game_instance.mainloop()


