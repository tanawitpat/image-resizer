import os
from PIL import Image
 
def resize_image(input_image_path, output_image_path, size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))
 
    resized_image = original_image.resize(size)
    width, height = resized_image.size
    print('The resized image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))
    resized_image.save(output_image_path)
 
def remove_output_files():
    outputFileList = os.listdir('output')
    for file in outputFileList:
        os.unlink("output/{}".format(file))
        print("{} has been removed".format(file))

if __name__ == '__main__':
    width = 600
    height = int(width * 3 / 4)

    remove_output_files()

    inputFileList = os.listdir('input')
    for file in inputFileList:
        if not file[0] == ".":
            resize_image(
                input_image_path="input/{}".format(file),
                output_image_path='output/{}'.format(file),
                size=(width, height)
            )