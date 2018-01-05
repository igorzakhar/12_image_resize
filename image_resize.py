import os
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
        default=os.getcwd(),
        help='Enter the path to the directory for saving file '
    )
    return parser.parse_args()


def get_image_data(original_filename):
    try:
        image = Image.open(os.path.abspath(original_filename))
        return image
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
    xsize, ysize = image_data.size
    resized_image = image_data.resize((x_resize, y_resize), Image.ANTIALIAS)
    return resized_image


def save_image(resized_image, original_file, x_size, y_size, path_to_save):
    filename = os.path.splitext(os.path.basename(original_file))[0]
    new_filename = '{}_{}x{}.{}'.format(
        filename,
        x_size,
        y_size,
        original_file.lower()
    )
    try:
        path_to_save = os.path.abspath(path_to_save)
        resized_image.save(os.path.join(path_to_save, new_filename))
        return new_filename
    except OSError as error:
        return error


def main():
    args = process_args()
    image_data = get_image_data(args.filename)

    if isinstance(image_data, OSError):
        print("File open error: ", image_data.strerror)
        return

    x_size, y_size = get_resize_value(
        image_data.size,
        args.width,
        args.heigth,
        args.scale
    )
    resized_img = resize_image(image_data, x_size, y_size)
    save_message = save_image(
        resized_img,
        args.filename,
        x_size,
        y_size,
        args.path
    )

    if isinstance(save_message, OSError):
        print("File save error: ", save_message.strerror)
    else:
        string_for_output = 'File {} has been saved to {}'
        path_to_save = os.path.abspath(args.path)
        print(string_for_output.format(save_message, path_to_save))


if __name__ == '__main__':
    main()
