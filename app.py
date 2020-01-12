import os
from PIL import Image

TARGET_WIDTH = int(os.getenv('TARGET_WIDTH'))
TARGET_HEIGHT = int(os.getenv('TARGET_HEIGHT'))


def resize_image(file_name, input_image_path, output_image_path, target_width, target_height):
    original_image = Image.open(input_image_path)
    original_image_width = original_image.width
    original_image_height = original_image.height

    print('{file_name} - The original image size is {wide} wide x {height} '
          'high'.format(file_name=file_name, wide=original_image_width, height=original_image_height))

    bigside_size = find_bigside_size(
        original_image_width=original_image_width,
        original_image_height=original_image_height
    )
    background = generate_background(
        width=bigside_size,
        height=bigside_size
    )
    offset = find_offset(
        bigside_size=bigside_size,
        original_image_width=original_image_width,
        original_image_height=original_image_height
    )
    background.paste(original_image, offset)
    resized_image = background.resize(
        (target_width, target_height), Image.ANTIALIAS)
    resized_image.save(output_image_path)

    print('{file_name} - The resized image size is {wide} wide x {height} '
          'high'.format(file_name=file_name, wide=resized_image.width, height=resized_image.height))


def find_offset(bigside_size, original_image_width, original_image_height):
    return (round((bigside_size - original_image_width) / 2),
            round((bigside_size - original_image_height) / 2))


def generate_background(width, height):
    return Image.new(
        'RGBA', (width, height), (255, 255, 255, 255))


def find_bigside_size(original_image_width, original_image_height):
    if original_image_width != original_image_height:
        bigside = original_image_width if original_image_width > original_image_height else original_image_height
    else:
        bigside = original_image_width
    return bigside


def clear_output_directory():
    outputFileList = os.listdir('output')
    for file in outputFileList:
        os.unlink("output/{file_name}".format(file_name=file))
        print("{file_name} has been removed".format(file_name=file))


if __name__ == '__main__':
    if TARGET_WIDTH is None or TARGET_HEIGHT is None:
        print(
            "Environment variables named TARGET_WIDTH and TARGET_HEIGHT must be defined."
        )
        exit(1)
    print("TARGET_WIDTH={}px".format(TARGET_WIDTH))
    print("TARGET_HEIGHT={}px".format(TARGET_HEIGHT))

    clear_output_directory()
    input_file_list = os.listdir('input')
    for file in input_file_list:
        if not file[0] == ".":
            resize_image(
                file_name=file,
                input_image_path="input/{}".format(file),
                output_image_path='output/{}.png'.format(
                    os.path.splitext(file)[0]),
                target_width=TARGET_WIDTH,
                target_height=TARGET_HEIGHT
            )
