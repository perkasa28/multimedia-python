from PIL import Image
from PIL import ImageFilter


# Memuat gambar
image = Image.open('jinwo.jpg')

# Menyimpan gambar
# image.save('jinwo.jpg')

##IMAGE CROPPING

cropped_image = image.crop((10, 10, 200, 200))
# cropped_image.save('cropped.jpg')

##IMAGE RESIZING

resized_image = cropped_image.resize((100, 100))
#resized_image.save('resize.jpg')


# ##FILTERING IMAGE
filtered_image = resized_image.filter(ImageFilter.BLUR)
# Jika gambar dalam mode RGBA, ubah menjadi RGB
if filtered_image.mode == 'RGBA':
    filtered_image = filtered_image.convert('RGB')
filtered_image.save('filtered.jpg')



