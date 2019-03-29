import cv2
import numpy as np

def execute():
    input_img = cv2.imread("Img/img2.png", cv2.IMREAD_ANYCOLOR)
    target_img = cv2.imread("Img/t1-img2.png", cv2.IMREAD_ANYCOLOR)

    cv2.imshow("Input image", np.uint8(input_img))
    cv2.imshow("Target image", np.uint8(target_img))
    cv2.waitKey(0)

if __name__ == '__main__':
    execute()
