#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 07:48:45 2017

@author: oskar
"""
BOARD = {}
COLORS = []
N = 3 #minimal length of the series
D = 3 #mininaml distance betwen elements to accept it as a series
L = 30 #length of the board
K = 0 #current number of elements in the series

def create_board(n):
    keys = list(range(n))
    values = [None]*n
    global BOARD
    BOARD = dict(zip(keys,values))

def pick_spot(spot_number):
    if int(spot_number) in BOARD.keys():
        return(int(spot_number))
    else:
        print('The number exceeds the length of the board')
        return None
    
def find_longest_series():
    for spot in BOARD:
        pass #how to find the longest series?! :O
        

def pick_color(spot_number, color):
    if int(spot_number) in BOARD.keys():
        BOARD[spot_number]=color
    else:
        print('The number exceeds the length of the board')

def player1_turn():
    ch = input('Choose the number of the spot [1:{}]: '.format(L))
    pick_spot(int(ch)-1)
        
def player2_turn():
    pick_color()
    
    
create_board(L)    
while K<N:
    player1_turn()
    player2_turn()
    K += 1