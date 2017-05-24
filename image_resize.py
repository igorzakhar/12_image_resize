import os
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
    parser.add_argument('-p', '--path', default=os.getcwd(),
                        help="Set the directory paths for saving file ")
    return parser.parse_args()


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
        print(ratio)
        x_resize = width
        y_resize = y_size / ratio
    elif heigth:
        ratio = y_size / heigth
        x_resize = x_size / ratio
        y_resize = heigth
    elif scale:
        x_resize = x_size * scale
        y_resize = y_size * scale

    return (round(x_resize), round(y_resize))


def resize_image(path_to_original, path_to_result, width, heigth, scale):
    path_to_original = os.path.abspath(path_to_original.name)
    path_to_result = os.path.abspath(path_to_result)
    if not os.path.exists(path_to_result):
        os.mkdir(path_to_result)
    try:
        with Image.open(path_to_original) as image:
            xsize, ysize = image.size
            x_resize, y_resize = get_resize_value(image.size, 
                                                  width, 
                                                  heigth,
                                                  scale)
            
            filename = os.path.basename(image.filename).rsplit('.', 1)[0]
            new_filename = "{}_{}x{}.{}".format(filename,
                                                x_resize, 
                                                y_resize,
                                                image.format.lower())
            image = image.resize((x_resize, y_resize), Image.ANTIALIAS)
            image.save(os.path.join(path_to_result, new_filename))
    except IOError:
        print("File does not contain image data")


if __name__ == '__main__':
    args = process_args()
    resize_image(args.file, args.path, args.width, args.heigth, args.scale)
