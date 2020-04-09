import numpy as np
from PIL import ImageGrab
import cv2
import time


def roi(img, vertices):
    mask=np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked


def process_img(original_image):
    # convert to gray
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    vertices = np.array([[10,280],[10,230],[130,130],[290,130],[500,260],[500,280]], np.int32)
    processed_img = roi(processed_img, [vertices])
    return processed_img

def main():

 last_time = time.time()
while(True):
       
        # 800x600 windowed mode
        screen =  np.array(ImageGrab.grab(bbox=(0,40,500,430)))
       # print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
