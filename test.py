import numpy as np
from skimage import metrics as mt
from skimage.io import imread, imsave
from skimage.color import rgb2gray
from sewar import uqi, ssim
from skimage import img_as_float


def get_metrics(img_path_source,img_path_encoded):
    im_src = rgb2gray(imread(img_path_source))
    #im_src = (imread(img_path_source))
    im_enc = imread(img_path_encoded)

    float = img_as_float(im_src)

    psnr = mt.peak_signal_noise_ratio(im_src,im_enc)
    ssi = mt.structural_similarity(im_src,im_enc,data_range=float.max() - float.min())
    #ssi = ssim(im_src,im_enc)
    uq_index = uqi(im_src,im_enc)

    print("PSNR = ", psnr)
    print("SSIM = ",ssi )
    print("UI = ", uq_index)
    
    return psnr,ssi, uq_index