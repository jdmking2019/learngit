from keras.preprocessing.image import ImageDataGenerator
from PIL import Image
from keras_preprocessing import image
import os
import numpy as np
from scipy.misc import imshow,imsave

# Image_dir = "/home/jdmking/AnGang_work/0524_classfier/person"
Image_dir = "/home/jdmking/AnGang_work/DATA/0524_classfier/background"
Image_dir1 = "/home/jdmking/background/"
image_name = os.listdir(Image_dir)
Image_path = [os.path.join(Image_dir,image_name1) for image_name1 in image_name]
i = 16404
for Image_path1 in Image_path:
    Img = Image.open(Image_path1)
    Img1 = np.float32(Img)
    #imshow(Img1)
    #Rotation_img = image.random_rotation(Img1, rg=90,row_axis=0,col_axis=1,channel_axis=2)
    #Rotation_img = image.random_shift(Img1,wrg=0.3, hrg=0.3,row_axis=0,col_axis=1,channel_axis=2)
    #imshow(Rotation_img)
    #Rotation_img = image.apply_brightness_shift(Img1,brightness=0.1)
    #imshow(Rotation_img)
    imsave(Image_dir1 + "0000" + str(i) + ".jpg" ,arr=Img1)
    print("Create %d picture" % i)
    i = i + 1
