import os
from PIL import Image
 
def resize_image(file_name, input_image_path, output_image_path, size: tuple):
    original_image = Image.open(input_image_path)
    print('{file_name} - The original image size is {wide} wide x {height} '
          'high'.format(file_name=file_name, wide=original_image.width, height=original_image.height))
    
    image_ratio_width, image_ratio_height = width / original_image.width, height / original_image.height

    if image_ratio_width < image_ratio_height:
        resize_width = size[0]
        resize_height = round(image_ratio_width * original_image.height)
    else:
        resize_width = round(image_ratio_height * original_image.width)
        resize_height = size[1]

    resized_image = original_image.resize((resize_width, resize_height), Image.ANTIALIAS)
    background = Image.new('RGBA', (size[0], size[1]), (255, 255, 255, 255))
    offset = (round((size[0] - resize_width) / 2), round((size[1] - resize_height) / 2))
    background.paste(resized_image, offset)

    print('{file_name} - The resized image size is {wide} wide x {height} '
          'high'.format(file_name=file_name, wide=resized_image.width, height=resized_image.height))
    resized_image.save(output_image_path)
 
def remove_output_files():
    outputFileList = os.listdir('output')
    for file in outputFileList:
        os.unlink("output/{file_name}".format(file_name=file))
        print("{file_name} has been removed".format(file_name=file))

if __name__ == '__main__':
    width = 600
    height = int(width * 3 / 4)

    remove_output_files()

    inputFileList = os.listdir('input')
    for file in inputFileList:
        if not file[0] == ".":
            resize_image(
                file_name=file,
                input_image_path="input/{}".format(file),
                output_image_path='output/{}'.format(file),
                size=(width, height)
            )