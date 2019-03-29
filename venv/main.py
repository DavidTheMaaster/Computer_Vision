import cv2
import numpy as np

def execute():
    input_img_path = "Img/img2.png"
    target_img_path = "Img/t1-img2.png"
    threshold = 0.1

    input_img = cv2.imread(input_img_path, cv2.COLOR_BGR2GRAY)
    target_img = cv2.imread(target_img_path,cv2.COLOR_BGR2GRAY)

    Irows, Icols = input_img.shape[:2]
    Trows, Tcols = target_img.shape[:2]

    Mrows = Irows - Trows + 1
    Mcols = Icols - Tcols + 1

    matching_img = np.zeros((Irows, Icols))

    # calculates the matchin map

    pixel_sum = 0

    for i in range(0, Mrows):
        for j in range(0, Mcols):
            pixel = matching_map_minimum(input_img, target_img, i, j)
            pixel_sum += pixel

            mathcing_img[i, j] = pixel_sum / matching_map_maximum(input_img, target_img, Trows, Tcols, i, j)

            if matching_img[i, j] < threshold:
                #detects when the value is less than the threshold (found taret image)
                print("patata")
            pixel_sum = 0

    cv2.imshow("Input image", np.uint8(input_img))
    cv2.imshow("Matching image", np.uint8(matching_img))
    cv2.imshow("Target image", np.uint8(target_img))
    cv2.waitKey(0)

def matching_map_minimum(input, target, i, j):
    #calculates the minimum value of the matching map

    Trows, Tcols = target.shape[:2]
    pixel_sum = 0
    for x in range(0, Trows):
        for y in range(0, Tcols):
            pixel = (target[x, y, 2] - input[i + x, j + y, 2]) ** 2
            pixel_sum += pixel

    return  pixel_sum


def matching_map_maximum(input, target, rows, cols, i, j):
    #calculates the maximum value of the matching map
    return np.sqrt(((target[i:i + rows, j:j + cols, 2]) ** 2).sum(axis=(0, 1)) - (((input[i:i + rows, j:j + cols, 2]) ** 2).sum(axis=(0, 1))))

if __name__ == '__main__':
    execute()
