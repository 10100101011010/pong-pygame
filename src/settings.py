import pygame
from os.path import join

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720 
SIZE = {'paddle': (40,100), 'ball': (30,30)}
POS = {'player': (WINDOW_WIDTH - 50, WINDOW_HEIGHT / 2), 'opponent': (50, WINDOW_HEIGHT / 2)}
SPEED = {'player': 560, 'opponent': 470, 'ball': 730} 
COLORS = {
    'paddle': '#ee322c',
    'paddle shadow': '#b12521',
    'ball': '#ee622c',
    'ball shadow': '#c14f24',
    'bg': '#085562',
    'bg detail': '#355d68'
}   