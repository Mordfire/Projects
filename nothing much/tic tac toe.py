import datetime
import pygame, sys
from PIL import ImageGrab
from PIL import ImageOps
import time
import pyautogui as pg
import numpy as np
import random
import datetime as dt

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! not exactly mine!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




pygame.init()

WIDHT = 600
HEIGHT = 600
BLUE = (120,200,200)
RED = (255,0,0)
Board_rows = 3
bord_cols = 3
player = 1
game_over = False

screen = pygame.display.set_mode( (WIDHT,HEIGHT))
pygame.display.set_caption("tica tac toe")
screen.fill( BLUE)

board = np.zeros( (Board_rows,bord_cols))
def draw_lines():
    pygame.draw.line(screen, RED,(0,200) , (600,200) , 20)
    pygame.draw.line(screen, RED,(0,400) , (600,400) , 20)
    pygame.draw.line(screen, RED,(200,0) , (200,600) , 20)
    pygame.draw.line(screen, RED,(400,0) , (400,600) , 20)

def draw():
    for row in range(Board_rows):
        for col in range(bord_cols):
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (int( col * 200 + 100) , int( row * 200 + 100 )), 60 ,15)
            elif board[row][col] == 2:
                pygame.draw.line(screen, RED, (col * 200, row * 200 + 200),(col * 200 + 200, row *200), 20 )

def mark_square(row,col,player):
    board[row][col] = player

def available_square(row,col):
    if board[row][col] == 0:
        return True
    else:
        return False

def is_board_full():
    for row in range(Board_rows):
        for col in range(bord_cols):
            if board[row][col] == 0:
                return False
            else:
                return True


def check_win(player):
    for col in range(bord_cols):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col,player)
            return True
    for row in range(Board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row,player)
            return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_dioganal(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_dioganal(player)
        return True

def draw_vertical_winning_line(col,player):
    posX = col * 200 + 100
    if player == 1:
        color2 = RED
    elif player == 2:
        color2 = RED
    pygame.draw.line(screen , color2, (posX,15), (posX, HEIGHT-15), 15)

def draw_horizontal_winning_line(row,player):
    posY = row * 200 + 100
    if player == 1:
        color1 = RED
    elif player == 2:
        color1 = RED

    pygame.draw.line(screen, color1, (15, posY), (WIDHT-15, posY), 15)

def draw_asc_dioganal(player):
    if player == 1:
        color = RED
    elif player == 2:
        color = RED
    pygame.draw.line(screen,color, (15, HEIGHT - 15), (WIDHT-15, 15), 15)

def draw_desc_dioganal(player):
    if player == 1:
        color = RED
    elif player == 2:
        color = RED
    pygame.draw.line(screen, color, (15,15), (WIDHT - 15, HEIGHT - 15), 15)

def restart():
    screen.fill(BLUE)
    draw_lines()
    player = 1
    for row in range(Board_rows):
        for col in range(bord_cols):
            board[row][col] = 0

draw_lines()

#main loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)
            if available_square(clicked_row,clicked_col):
                if player == 1:
                    mark_square(clicked_row,clicked_col,1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row,clicked_col,2)
                    if check_win(player):
                        game_over = True
                    player = 1
                draw()
                print(board)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

    pygame.display.update()



