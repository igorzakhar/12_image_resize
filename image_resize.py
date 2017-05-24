import argparse

from PIL import Image


def process_args():
    parser = argparse.ArgumentParser(description="Resize image from file")
    parser.add_argument('file', type=argparse.FileType('r'), 
                        help="Input filename")
    parser.add_argument('-x', '--width', type=float, default=None, 
                        help="Input value width in px")
    parser.add_argument('-y', '--heigth', type=float, default=None, 
                        help="Input value heigth in px")
    parser.add_argument('-s', '--scale', type=float, 
                        default=None, help="Input value scale")
    return parser.parse_args()


def resize_image(path_to_original, path_to_result):
    pass


if __name__ == '__main__':
    pass
