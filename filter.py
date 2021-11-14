from PIL import Image
import numpy as np


def calculate_gray_cell(row, column):
    gray_cell = 0
    for x in range(row, min(row + cell_size, rows_count)):
        for y in range(column, min(column + cell_size, columns_count)):
            gray_cell += sum(pixels_matrix[x][y]) // 3
    return int(gray_cell // (cell_size ** 2))


def set_gray_in_cell(row, column):
    for x in range(row, min(row + cell_size, rows_count)):
        for y in range(column, min(column + cell_size, columns_count)):
            for channel in range(0, 3):
                pixels_matrix[x][y][channel] = int(gray // gradation) * gradation


input_data = input("Enter cell size and gradation\n").split()
image = Image.open("img2.jpg")
cell_size = int(input_data[0])
gradation = 255 // int(input_data[1])
pixels_matrix = np.array(image)
rows_count = len(pixels_matrix)
columns_count = len(pixels_matrix[1])

current_row = 0
while current_row < rows_count:
    current_column = 0
    while current_column < columns_count:
        gray = calculate_gray_cell(current_row, current_column)
        set_gray_in_cell(current_row, current_column)
        current_column = current_column + cell_size
    current_row = current_row + cell_size

Image.fromarray(pixels_matrix).save("res.jpg")
