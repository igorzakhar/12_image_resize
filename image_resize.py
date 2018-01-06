import os
import sys
import argparse

from PIL import Image


def process_args():
    parser = argparse.ArgumentParser(description="Resize image from file")
    parser.add_argument(
        'filename',
        type=str,
        help='Original image filename'
    )
    parser.add_argument(
        '-x',
        '--width',
        type=float,
        default=None,
        help='Input value width in pixels'
    )
    parser.add_argument(
        '-y',
        '--heigth',
        type=float,
        default=None,
        help='Input value heigth in pixels'
    )
    parser.add_argument(
        '-s',
        '--scale',
        type=float,
        default=None,
        help='Input value scale'
    )
    parser.add_argument(
        '-p',
        '--path',
        help='Enter the path to the directory for saving file '
    )
    return parser.parse_args()


def get_image_data(original_filename):
    try:
        return Image.open(os.path.abspath(original_filename))
    except OSError as error:
        return error


def get_resize_value(original_size, width=None, heigth=None, scale=None):
    x_size, y_size = original_size
    ratio = None
    x_resize = None
    y_resize = None

    if width and heigth:
        x_resize = width
        y_resize = heigth
    elif width:
        ratio = x_size / width
        x_resize = width
        y_resize = y_size / ratio
    elif heigth:
        ratio = y_size / heigth
        x_resize = x_size / ratio
        y_resize = heigth
    elif scale:
        x_resize = x_size * scale
        y_resize = y_size * scale
    else:
        return x_size, y_size

    return round(x_resize), round(y_resize)


def resize_image(image_data, x_resize, y_resize):
    return image_data.resize((x_resize, y_resize), Image.ANTIALIAS)


def save_image(resized_image, original_file, path_to_save):
    if path_to_save:
        path_to_save = os.path.abspath(path_to_save)
    else:
        filename, ext = os.path.splitext(original_file.filename)
        x_size, y_size = resized_image.size
        path_to_save = '{}_{}x{}{}'.format(filename, x_size, y_size, ext)

    try:
        resized_image.save(path_to_save, original_file.format)
    except OSError as error:
        return error


def main():
    args = process_args()
    image_data = get_image_data(args.filename)

    if isinstance(image_data, OSError):
        print("File open error: ", image_data.strerror)
        sys.exit(image_data.errno)

    x_size, y_size = get_resize_value(
        image_data.size,
        args.width,
        args.heigth,
        args.scale
    )
    resized_img = resize_image(image_data, x_size, y_size)
    error = save_image(
        resized_img,
        image_data,
        args.path
    )
    if isinstance(error, OSError):
        print("File save error: ", error.strerror)
        sys.exit(error.errno)


if __name__ == '__main__':
    main()
