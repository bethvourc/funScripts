from PIL import Image, ImageFilter, ImageEnhance
import os

path = 'imageProcessor/img'
pathOut = 'imageProcessor/eImg'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN).rotate(-90).convert('RGB')

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]
    edit.save(f"{pathOut}/{clean_name}_edited.jpg")

