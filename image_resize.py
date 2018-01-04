import os
import argparse

from PIL import Image


def process_args():
    parser = argparse.ArgumentParser(description="Resize image from file")
    parser.add_argument(
        'file',
        type=argparse.FileType('r'),
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
        default=os.getcwd(),
        help='Enter the path to the directory for saving file '
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


def resize_image(image_data, x_resize, y_resize):
    xsize, ysize = image_data.size
    resized_image = image_data.resize((x_resize, y_resize), Image.ANTIALIAS)

    return resized_image


def save_image(resized_image, original_image, x_size, y_size, path_to_save):
    path_to_save = os.path.abspath(path_to_save)

    if not os.path.exists(path_to_save):
        os.mkdir(path_to_save)

    filename = os.path.basename(original_image.filename).rsplit('.', 1)[0]
    new_filename = '{}_{}x{}.{}'.format(
        filename,
        x_size,
        y_size,
        original_image.format.lower()
    )
    resized_image.save(os.path.join(path_to_save, new_filename))
    string_for_output = 'File {} has been saved to {}'
    print(string_for_output.format(new_filename, path_to_save))


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

        resized_image = resize_image(image_data, x_resize, y_resize)
        save_image(
            resized_image,
            image_data,
            x_resize,
            y_resize,
            args.path
        )
    else:
        print("File does not contain image data")


if __name__ == '__main__':
    main()
