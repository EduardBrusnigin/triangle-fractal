import pygame as pg

from settings import WIDTH, HEIGHT

from main import Main


pg.init()


window = pg.display.set_mode((WIDTH, HEIGHT))

main = Main()
main.prepare(window)


while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			exit()

	main.update(window)

	pg.display.set_caption(f"counter = {main.dots_counter}")

	pg.display.update()
