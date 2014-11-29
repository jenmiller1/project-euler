#!/usr/bin/env python
# encoding: utf-8
"""
euler_11.py
Last Modified: Sat Nov 22, 2014  07:59PM
"""
import numpy as np
import operator

grid = []
length = 20
width = 20
with open('euler_11_grid.txt') as f:
    for line in f:
        grid.append([int(i) for i in line.split()])
print grid
largest_product = 0

max_prod = 0
for i in range(0,20):
    for j in range(0, 16):
        #print row, col, horiz
        horiz = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
        max_prod = max(max_prod, horiz)

        vert = grid[j][i] + grid[j+1][i] + grid[j+2][i] + grid[j+3][i]
        max_prod = max(vert, max_prod)
for i in range(0,16):
    for j in range(0, 16):
        prod = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
        max_prod = max(prod, max_prod)

for i in range(3,20):
    for j in range(0, 16):
        prod = grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3]
        print i, j, prod, grid[i][j] , grid[i-1][j+1] , grid[i-2][j+2] , grid[i-3][j+3]
        max_prod = max(prod, max_prod)

print max_prod


