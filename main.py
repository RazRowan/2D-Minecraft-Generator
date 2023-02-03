import random
import sys
from PIL import Image

# Variables
img_dimension = 48

# Creates a list containing 5 lists, each of 8 items, all set to 0
rows, columns = 25, 25
Map = [[0 for x in range(rows)] for y in range(columns)]

def generate_random_map():
    print_map()
    for i in range(len(Map)):
        for j in range(len(Map[i])):
            if rng(i, j, Map[i][j], 4, 0) == 1:
                Map[i][j] = 1
    print_map()


def rng(x, y, blocktype, denominator, depth):
    # check_perimeter
    # num_in_perimeter = check_perimeter(x, y, blocktype)
    # match(num_in_perimeter):
    #     case 0:
    #         denominator = denominator
    #     case 1:
    #         denominator = 4


    return random.randint(1, denominator)

# def check_perimeter(x, y, blocktype):
#     num_in_perimeter = 0
#     # Check top-left
#     if Map[x-1][y-1] is not None and Map[x-1][y-1] == blocktype:
#         num_in_perimeter += 1
#     # Check top
#     if Map[x][y-1] is not None and Map[x][y-1] == blocktype:
#         num_in_perimeter += 1
#     # Check top-right
#     if Map[x+1][y-1] is not None and Map[x+1][y-1] == blocktype:
#         num_in_perimeter += 1
#     # Check left
#     if Map[x-1][y] is not None and Map[x-1][y] == blocktype:
#         num_in_perimeter += 1
#     # Check right
#     if Map[x+1][y] is not None and Map[x+1][y] == blocktype:
#         num_in_perimeter += 1
#     # Check bottom-left
#     if Map[x-1][y+1] is not None and Map[x-1][y+1] == blocktype:
#         num_in_perimeter += 1
#     # Check bottom
#     if Map[x][y+1] is not None and Map[x][y+1] == blocktype:
#         num_in_perimeter += 1
#     # Check bottom-right
#     if Map[x+1][y+1] is not None and Map[x+1][y+1] == blocktype:
#         num_in_perimeter += 1
#
#     return num_in_perimeter


def print_map():
    # Print the map in text
    lines = []
    for row in Map:
        lines.append(' '.join(str(x) for x in row))
    print('\n'.join(lines))

def create_image():
    # Open all images
    images = [Image.open(x) for x in ['./sprites/sky.png', './sprites/cloud.png', './sprites/grass.png',
                                      './sprites/dirt.png', './sprites/stone.png', './sprites/coal.png',
                                      './sprites/iron.png', './sprites/gold.png', './sprites/diamond.png',
                                      './sprites/bedrock.png', './sprites/log.png', './sprites/leaves.png']]

    # Create a new image as big as our Map
    new_im = Image.new('RGB', (img_dimension * rows, img_dimension * columns))

    # Create image
    x_offset = 0
    y_offset = 0
    for i in range(columns):
      x_offset = 0
      for j in range(rows):
          new_im.paste(images[Map[i][j]], (x_offset, y_offset))
          x_offset += images[Map[i][j]].size[0]
      y_offset += images[Map[i][j]].size[1]


    # Save new image
    new_im.save('test.png')

generate_random_map()
create_image()