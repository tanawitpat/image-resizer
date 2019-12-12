import os
from PIL import Image
 
def resize_image(file_name, input_image_path, output_image_path, size: tuple):
    original_image = Image.open(input_image_path)
    original_image_width = original_image.width
    original_image_height = original_image.height
    print('{file_name} - The original image size is {wide} wide x {height} '
          'high'.format(file_name=file_name, wide=original_image_width, height=original_image_height))
    bigside = find_bigside_size(original_image_width, original_image_height)
    background = Image.new('RGBA', (bigside, bigside), (255, 255, 255, 255))
    offset = (round((bigside - original_image_width) / 2), round((bigside - original_image_height) / 2))
    background.paste(original_image, offset)
    resized_image = background.resize((size[0], size[1]), Image.ANTIALIAS)
    resized_image.save(output_image_path)
    print('{file_name} - The resized image size is {wide} wide x {height} '
          'high'.format(file_name=file_name, wide=resized_image.width, height=resized_image.height))

def find_bigside_size(original_image_width, original_image_height):
    if original_image_width != original_image_height:
        bigside = original_image_width if original_image_width > original_image_height else original_image_height
    else:
        bigside = original_image_width
    return bigside

def remove_output_files():
    outputFileList = os.listdir('output')
    for file in outputFileList:
        os.unlink("output/{file_name}".format(file_name=file))
        print("{file_name} has been removed".format(file_name=file))

if __name__ == '__main__':
    target_width = 600
    target_height = target_width

    remove_output_files()

    inputFileList = os.listdir('input')
    for file in inputFileList:
        if not file[0] == ".":
            resize_image(
                file_name=file,
                input_image_path="input/{}".format(file),
                output_image_path='output/{}.png'.format(os.path.splitext(file)[0]),
                size=(target_width, target_height)
            )
