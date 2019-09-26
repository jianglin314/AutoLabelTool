from PIL import Image
import configparser
import glob


file_path = "configuration.ini"

def paste_image(template_image, image, left, upper, right, lower):
    template_image.paste(image, (left, upper, right, lower))
    return template_image

def load_configuration_file(path):
    config = configparser.ConfigParser()
    config.read(path)
    return config

def get_configuration_data():
    configuration = load_configuration_file(file_path)
    return configuration

output_dict = get_configuration_data()
template = output_dict['InputFiles']['Template']
images_to_paste_dir = output_dict['InputFiles']['ImagesToPasteDir']
outDir = output_dict['OutputFiles']['OutputFolder']

template_image = Image.open(template)
counter = 0
for filename in glob.glob(images_to_paste_dir + '/*.jpg'):
    im=Image.open(filename)
    width, height = im.size
    output_image = paste_image(template_image, im, 0, 0 , width, height)
    output_image.save(outDir + '/output_' + str(counter) + '.jpg')
    counter +=1
