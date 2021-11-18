from argparse import ArgumentParser

from PIL import Image
import numpy as np


def pixelate(image_array, gradation_number=5, pixel_size=10):
    """
    convert input image array to pixelated image array
    :param image_array: array to transform
    :param gradation_number: number of grey colour
    :param pixel_size: pixel size
    :return: None
    """
    height = len(image_array)
    width = len(image_array[0])
    grey_step = 256 // gradation_number
    for i in range(0, height, pixel_size):
        for j in range(0, width, pixel_size):
            summa = np.sum(image_array[i:i + pixel_size, j:j + pixel_size])
            summa = int(summa // 3 // pixel_size // pixel_size)

            image_array[i:i + pixel_size, j:j + pixel_size] = summa // grey_step * grey_step


def callback_parser(args):
    """parser callback"""
    process_parser(args.input, args.output, int(args.gradation), int(args.size))


def process_parser(input_filepath, output_filepath, gradation, size):
    """parser process"""
    img = Image.open(input_filepath)
    arr = np.array(img)
    pixelate(arr, gradation_number=gradation, pixel_size=size)
    res = Image.fromarray(arr)
    res.save(output_filepath)


def setup_parser(parser):
    """parser setup"""

    parser.add_argument(
        "-i", "--input", dest="input",
        help="path to input image",
        required=True,
    )

    parser.add_argument(
        "-o", "--output", dest="output",
        help="path to output image",
        required=True,
    )

    parser.add_argument(
        "-s", "--size", dest="size",
        help="pixel size",
        default=10,
        required=False,
    )

    parser.add_argument(
        "-g", "--gradation", dest="gradation",
        help="gradation number",
        default=8,
        required=False,
    )
    parser.set_defaults(callback=callback_parser)


def main():
    """ main program """
    parser = ArgumentParser(description="Pixelate CLI")
    setup_parser(parser)
    args = parser.parse_args()
    args.callback(args)


if __name__ == "__main__":
    main()
