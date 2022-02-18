from glob import glob                                                           
import cv2 
Path='PATH_TO_PNG_IMAGES_FOLDER'
pngs = glob(Path+'/*.png')

for j in pngs:
    img = cv2.imread(j)
    cv2.imwrite(j[:-3] + 'jpg', img)