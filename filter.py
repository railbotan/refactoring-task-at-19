from PIL import Image
import numpy as np


def calculate_gray_cell(row, column):
    mosaic = pixels_matrix[row:min(row + cell_size, rows_count), column:min(column + cell_size, columns_count)]
    return int((np.sum(mosaic) // 3) // (cell_size ** 2))


def set_gray_in_cell(row, column):
    mosaic = pixels_matrix[row:min(row + cell_size, rows_count), column:min(column + cell_size, columns_count)]
    np.place(mosaic[:, ], mosaic >= 0, int(gray // gradation) * gradation)


input_data = input("Enter cell size and gradation\n").split()
image = Image.open(input("Enter source file name\n"))
result = input("Enter result file name\n")
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

Image.fromarray(pixels_matrix).save(f"{result}")
