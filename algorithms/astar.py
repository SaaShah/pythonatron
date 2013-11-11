#!/usr/bin/env python
"""
Maze solver using the A* algorithm. Uses pyglet for graphics.
Video demo here: https://vimeo.com/10207080

Key Commands
g: runs the solver
c: clears existing walls
ctrl+click: moves the target (green cell)
opt+click: moves the agent (blue cell)
"""

import math, pyglet, random, sys
from pyglet.window import Window
from pyglet.gl import *

class Cell():
    def __init__(self, x, y, x_coord, y_coord):
        self.x = x
        self.y = y
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.coords = (self.x_coord, self.y_coord)
        self.parent = None
        self.heuristic = 0
        
    def get_cumulative_distance_to_start(self):
        n = 0
        p = self.parent
        while p:
            ++n
            p = p.parent
        return n
    
    def get_path_to_orgin(self):
        p = self.parent
        result = []
        while p:
            result.append(p)
            p = p.parent
        result.reverse()
        return result
        
class Grid():
    def __init__(self, cell_width, cell_height, columns, rows):
        self.cell_count = int(rows * columns)
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.row_count = int(rows)
        self.column_count = int(columns)
        self.cells = {}
     
        for i in range(0, self.column_count):
            for j in range(0, self.row_count):
                c = Cell((i * self.cell_width), (j * self.cell_height), i, j)
                self.cells[ (c.x_coord, c.y_coord) ] = c
    
    def get_adjacent_cells(self, x_coord, y_coord):
        result = {}
        for x, y in [ (x_coord + i, y_coord + j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0 ]:
            if (x, y) in self.cells:
                result[ (x, y) ] = self.cells[ (x, y) ]
        return result
        
    def get_coord_distance(self, cell_a, cell_b):
        dx = abs(cell_a.x_coord - cell_b.x_coord)
        dy = abs(cell_a.y_coord - cell_b.y_coord)
        return  math.sqrt((dx * dx) + (dy * dy))
        
class GridRenderer():
    
    WIDTH = 960
    HEIGHT = 540
    
    def __init__(self):
        self.cell_size = 15
        self.grid = Grid(self.cell_size, self.cell_size, GridRenderer.WIDTH / self.cell_size, GridRenderer.HEIGHT / self.cell_size)
        self.obstacle_cells = []
        self.adjacent_cells = []
        self.target_cell = self.grid.cells[ (15, 5) ]
        self.agent_cell = self.grid.cells[ (0, 5) ]
        self.path = []
        self.cache = []
        
    def update(self):
      self.draw_background()
      self.draw_start_cell()
      self.draw_target_cell()
      self.draw_agent_cell()
      self.draw_grid()
      self.draw_obstacle_cells()

    def update_algorithm(self):
        if self.agent_cell == self.target_cell: return
        if self.agent_cell == None: return
        self.path_index = 0
        search_cell = self.agent_cell
        open_list = []
        closed_list = []
        open_list.append(search_cell)
        
        while len(open_list) > 0:
            adjacent_cells = self.grid.get_adjacent_cells(search_cell.x_coord, search_cell.y_coord)
            for n in adjacent_cells:
                cell = self.grid.cells[ n ]
                if cell == self.target_cell:
                    self.search_status_updated = True
                    cell.parent = search_cell
                    self.path = cell.get_path_to_orgin()
                    open_list = []
                    return
                
                if cell not in self.obstacle_cells:
                    if cell not in closed_list:
                        if cell not in open_list:
                            open_list.append(cell)
                            cell.parent = search_cell
                            cell.heuristic = cell.get_cumulative_distance_to_start() + self.grid.get_coord_distance(cell, self.target_cell)
            
            closed_list.append(search_cell)
            open_list.remove(search_cell)
            search_cell = None
            
            for cell in open_list:
                if search_cell == None:
                    search_cell = cell
                    continue
                if search_cell.heuristic > cell.heuristic:
                    search_cell = cell
                    
    def get_cell_at_point(self, x, y):
        coords = (x / self.cell_size, y / self.cell_size)
        if coords in self.grid.cells:
            return self.grid.cells[ coords ]
                    
    def draw_background(self):
        self.draw_rect(0, 0, GridRenderer.WIDTH, GridRenderer.HEIGHT, (.07, .07, .07 ))
        pass

    def draw_grid(self):
        
        glLineWidth(1.0)

        glBegin(GL_LINES)
        
        glColor4f(*(.2, .2, .2, 1))
        
        for i in range(1, self.grid.column_count):
            glVertex2i(int(i * self.grid.cell_width), int(0))
            glVertex2i(int(i * self.grid.cell_height), int(self.grid.row_count * self.grid.cell_width))
            
        for j in range(1, self.grid.row_count):
            glVertex2i(0, int(j * self.grid.cell_height))
            glVertex2i(int(self.grid.column_count * self.grid.cell_width), int(j * self.grid.cell_height))
            
        glEnd()
            
    def draw_obstacle_cells(self):
        for cell in self.obstacle_cells:
            if cell == self.agent_cell or cell == self.target_cell: continue
            self.draw_cell(cell, (.2, .2, .2))
            glBegin(GL_LINE_LOOP)
            glColor4f(*(.4, .4, .4, 255))
            glVertex2f(cell.x, cell.y)
            glVertex2f(cell.x + self.grid.cell_width, cell.y)
            glVertex2f(cell.x + self.grid.cell_width, cell.y + self.grid.cell_height)
            glVertex2f(cell.x, cell.y + self.grid.cell_height)
            glEnd()
            
    def draw_adjacent_cells(self):     
        for n in self.adjacent_cells:
            cell = self.adjacent_cells[n]
            self.draw_cell(cell, (0, 255, 0))
    
    def draw_start_cell(self):
        self.draw_cell(self.agent_cell, (41.0/255.0, 171.0 / 255.0 , 226.0/255.0))
        pass 
            
    def draw_agent_cell(self):
        if self.path and len(self.path) > 0:
            if self.agent_cell is not None:
                cell = self.path[0]
                self.draw_cell(cell, (237.0/255, 30.0/255, 121.0/255))
        
        if len(self.path) > 0:
            self.path.pop(0)
    
    def draw_target_cell(self):
        if self.target_cell is not None:
            cell = self.target_cell
            self.draw_cell(cell, (150.0/255.0, 245.0/255.0, 33.0/255.0))
    
    def draw_cell(self, cell, color):
        self.draw_rect(cell.x, cell.y, self.grid.cell_width, self.grid.cell_height, color)
    
    def draw_rect(self, x, y, w, h, color):
        glBegin(GL_QUADS)
        glColor3f(*color)
        glVertex2f(x, y)
        glVertex2f(x + w, y)
        glVertex2f(x + w, y + h)
        glVertex2f(x, y + h)
        glEnd()
    
    def push_pop_obstacle_cell(self, x, y, modifiers):
        cell = self.get_cell_at_point(x, y)
        if cell is not None:
            if modifiers == 0:
                if self.obstacle_cells.count(cell) == 0:
                    self.obstacle_cells.append(cell)
            if modifiers == 64:
                if self.obstacle_cells.count(cell) > 0:
                    self.obstacle_cells.remove(cell)

window = Window(GridRenderer.WIDTH, GridRenderer.HEIGHT, "A* Example")
renderer = GridRenderer()

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
        renderer.push_pop_obstacle_cell(x, y, modifiers)

@window.event
def on_mouse_press(x, y, buttons, modifiers):
        renderer.push_pop_obstacle_cell(x, y, modifiers)
        c = renderer.get_cell_at_point(x, y)
        renderer.adjacent_cells = renderer.grid.get_adjacent_cells(c.x_coord, c.y_coord)
        if c is not None:
            print modifiers
            if modifiers == 132 and c is not renderer.target_cell:    
                renderer.agent_cell = c
            
            if modifiers == 2 and c is not renderer.agent_cell:
                renderer.target_cell = c
                
@window.event            
def on_key_press(symbol, modifiers):
        if symbol == pyglet.window.key.C:
            renderer.obstacle_cells = []
        if symbol == pyglet.window.key.G:
            pyglet.clock.unschedule(update)
            renderer.update_algorithm()
            pyglet.clock.schedule_interval(update, 1/10.0)

def update(param):
    window.clear()
    renderer.update()
    
pyglet.options['debug_gl'] = False
pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()
