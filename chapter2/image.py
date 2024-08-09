from PIL import Image
from PIL import ImageFilter


# Memuat gambar
image = Image.open('jinwo.jpg')

# Menyimpan gambar
image.save('jinwo.jpg')

##IMAGE CROPPING

cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('jinwo.jpg')

##IMAGE RESIZING

resized_image = cropped_image.resize((100, 100))
resized_image.save('jinwo.jpg')


##FILTERING IMAGE

filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('jinwo.jpg')



