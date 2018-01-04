import os
import argparse

from PIL import Image


def process_args():
    parser = argparse.ArgumentParser(description="Resize image from file")
    parser.add_argument(
        'file',
        type=argparse.FileType('r'),
        help='Input filename'
    )
    parser.add_argument(
        '-x',
        '--width',
        type=float,
        default=None,
        help='Input value width in px'
    )
    parser.add_argument(
        '-y',
        '--heigth',
        type=float,
        default=None,
        help='Input value heigth in px'
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
        default=os.getcwd(),
        help='Set the directory paths for saving file '
    )
    return parser.parse_args()


def get_image_data(path_to_original):
    path_to_original = os.path.abspath(path_to_original.name)
    try:
        image = Image.open(path_to_original)
    except IOError:
        return None
    return image


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
        return(x_size, y_size)

    return (round(x_resize), round(y_resize))


def resize_image(image_data, path_to_result, x_resize, y_resize):
    path_to_result = os.path.abspath(path_to_result)

    if not os.path.exists(path_to_result):
        os.mkdir(path_to_result)
    xsize, ysize = image_data.size
    filename = os.path.basename(image_data.filename).rsplit('.', 1)[0]
    new_filename = '{}_{}x{}.{}'.format(
        filename,
        x_resize,
        y_resize,
        image_data.format.lower()
    )
    image_new = image_data.resize((x_resize, y_resize), Image.ANTIALIAS)
    image_new.save(os.path.join(path_to_result, new_filename))
    print('File {} has been saved to {}'.format(new_filename, path_to_result))


def main():
    args = process_args()
    image_data = get_image_data(args.file)
    if image_data:
        x_resize, y_resize = get_resize_value(
            image_data.size,
            args.width,
            args.heigth,
            args.scale
        )

        resize_image(image_data, args.path, x_resize, y_resize)
    else:
        print("File does not contain image data")


if __name__ == '__main__':
    main()
