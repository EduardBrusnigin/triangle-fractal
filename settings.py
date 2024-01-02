# main 

DOT_SIZE = 1

first_color = (255, 0, 0)
second_color = (0, 255, 0)
third_color = (0, 0, 255)

COLORS = (first_color, second_color, third_color)


# triangle

side = 500  # side size
space = 35

first_vertex = (0 + space, (3**0.5/2)*side + space)
second_vertex = (side/2 + space, 0 + space)
third_vertex = (side + space, (3**0.5/2)*side + space)

VERTEXES = (first_vertex, second_vertex, third_vertex)


# window

WIDTH = side + 2*space + DOT_SIZE
HEIGHT = (3**0.5/2)*side + 2*space + DOT_SIZE
