import math

import cv2
import numpy as np

def gray_scale_average(r, g, b):
    return np.uint8((int(r) + int(g) + int(b))/3)

def gray_scale_norm(r, g, b):
    norm = math.sqrt(int(r)**2 + int(g)**2 + int(b)**2)
    max_normalize = (norm/442)*255
    return np.uint8(max_normalize)

def gray_scale_max(r, g, b):
    return np.uint8(max(int(r), int(g), int(b)))

def gray_scale_min(r, g, b):
    return np.uint8(min(int(r), int(g), int(b)))

if __name__ == "__main__":

    img = cv2.imread('gatito.jpg')

    height, width, channels = img.shape
    gray_img = np.zeros((height, width), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            r,g,b = img[i,j]
            value = gray_scale_average(r,g,b)
            gray_img[i, j] = value
    cv2.imwrite('gatito_grey_average.jpg', gray_img)

    for i in range(height):
        for j in range(width):
            r,g,b = img[i,j]
            value = gray_scale_norm(r,g,b)
            gray_img[i, j] = value
    cv2.imwrite('gatito_grey_norm.jpg', gray_img)

    for i in range(height):
        for j in range(width):
            r,g,b = img[i,j]
            value = gray_scale_max(r,g,b)
            gray_img[i, j] = value
    cv2.imwrite('gatito_grey_max.jpg', gray_img)

    for i in range(height):
        for j in range(width):
            r,g,b = img[i,j]
            value = gray_scale_min(r,g,b)
            gray_img[i, j] = value
    cv2.imwrite('gatito_grey_min.jpg', gray_img)
