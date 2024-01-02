import pygame as pg

from random import randint

from settings import VERTEXES, DOT_SIZE, COLORS


class Main:
	def __init__(self):
		self.vertexes = VERTEXES

		self.cursor = {'x': None, 'y': None}

		self.dots_counter = 0


	def prepare(self, surface):
		for i in range(3):
			color = COLORS[i]
			
			x = VERTEXES[i][0]
			y = VERTEXES[i][1]

			pg.draw.rect(surface, color, (x, y, DOT_SIZE, DOT_SIZE))

		start_vertex = VERTEXES[randint(0, 2)]

		self.cursor['x'] = start_vertex[0]
		self.cursor['y'] = start_vertex[1]


	def update(self, surface):
		random_vertex = randint(0, 2)

		color = COLORS[random_vertex]

		vertex_x = VERTEXES[random_vertex][0]
		vertex_y = VERTEXES[random_vertex][1]

		x = self.cursor['x'] = (self.cursor['x'] + vertex_x)/2
		y = self.cursor['y'] = (self.cursor['y'] + vertex_y)/2

		pg.draw.rect(surface, color, (x, y, DOT_SIZE, DOT_SIZE))

		self.dots_counter += 1
		
