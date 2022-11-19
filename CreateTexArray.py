import sys
import cv2 as cv
import numpy as np
import argparse

def create2DImageArray(image_paths):
    n = len(image_paths)

    # read all input images into an array
    imgs = []
    for img_path in image_paths:
        img = cv.imread(img_path)
        imgs.append(img)
    
    #determine size, channels and datatype of new array image
    rows, cols, ch = imgs[0].shape
    dt = imgs[0].dtype

    #initialize empty array image
    array = np.zeros((rows*n, cols, ch), dt)

    #add padding to each image so that they will all line up during addition
    for i in range(n):
        img = cv.copyMakeBorder(imgs[i], i*rows, (n-i-1)*rows, 0, 0, cv.BORDER_CONSTANT, value=[0,0,0])
        array = array + img 

    return array

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('paths', type=str, nargs='+')
    parser.add_argument('output', type=str)
    args = parser.parse_args()
    array = create2DImageArray(args.paths)
    cv.imwrite(args.output, array)
    









        
        




