import cv2
import numpy as np

def execute():
    input_img_path = "Img/img1.png"
    target_img_path = "Img/t1-img1.png"
    threshold = 0.1

    input_img = cv2.imread(input_img_path)
    target_img = cv2.imread(target_img_path)

    #get the images on grey scale for better performance
    input_grey = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
    target_grey = cv2.cvtColor(target_img, cv2.COLOR_BGR2GRAY)

    #scaled the images for better performance
    input_grey = cv2.resize(input_grey, (0, 0), fx=0.5, fy=0.5);
    target_grey = cv2.resize(target_grey, (0, 0), fx=0.5, fy=0.5);

    Irows, Icols = input_grey.shape
    Trows, Tcols = target_grey.shape

    Mrows = Irows - Trows + 1
    Mcols = Icols - Tcols + 1

    matching_img = np.zeros((Irows, Icols))

    # calculates the matchin map

    match = []
    pixel_min = 0

    for i in range(0, Mrows):
        for j in range(0, Mcols):
            pixel = squared_difference(input_grey, target_grey, i, j)
            pixel_min += pixel
            pixel_max = normalized_squared_difference(input_grey, target_grey, Trows, Tcols, i, j)

            matching_img[i, j] = pixel_min / pixel_max

            if matching_img[i, j] < threshold:
                #detects when the value is less than the threshold (found taret image)
                print("patata")
                match = [0]
                pix_min_x = j * 2
                pix_min_y = i * 2
                pix_max_x = (j + Tcols) * 2
                pix_max_y = (i + Trows) * 2
                cv2.rectangle(input_img, (pix_min_x, pix_min_y), (pix_max_x, pix_max_y), (0, 255, 0), 2, 8)
            pixel_min = 0

    matching_img = cv2.resize(matching_img, (0, 0), fx=2, fy=2);

    imgFound = np.zeros((40, 245, 3), np.uint8)

    font = cv2.FONT_HERSHEY_SIMPLEX

    if match == [0]:
        cv2.putText(imgFound, "TARGET FOUND", (5, 30), font, 0.75, (0, 255, 0), 2)

    else:
        cv2.putText(imgFound, "TARGET NOT FOUND", (5, 30), font, 0.75, (0, 0, 255), 1)

    cv2.imshow("Input image", np.uint8(input_img))
    cv2.imshow("Matching image", np.uint8(matching_img))
    cv2.imshow("Target image", np.uint8(target_img))
    cv2.imshow("Result", np.uint8(imgFound))
    cv2.waitKey(0)

def squared_difference(input, target, i, j):
    #calculates the squared diference

    Trows, Tcols = target.shape[:2]
    pixel_sum = 0
    for x in range(0, Trows):
        for y in range(0, Tcols):
            pixel = (target[x, y] - input[i + x, j + y]) ** 2
            pixel_sum += pixel

    return  pixel_sum


def normalized_squared_difference(input, target, rows, cols, i, j):
    #calculates normalized_squared diference
    return np.sqrt(((target[i:i + rows, j:j + cols]) ** 2).sum(axis=(0, 1)) - (((input[i:i + rows, j:j + cols]) ** 2).sum(axis=(0, 1))))


if __name__ == '__main__':
    execute()
