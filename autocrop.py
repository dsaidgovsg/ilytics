import cv2
import glob


def display(img, frameName="OpenCV Image"):
    h, w = img.shape[0:2]
    neww = 700
    newh = int(neww * (h / w))
    img = cv2.resize(img, (neww, newh))
    #cv2.imshow(frameName, img)
    cv2.imwrite("test.jpg", img)


def autocrop(file):
    ori = cv2.imread(file)
    #display(ori, "thresh")
    image = ori[:]

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #display(hsv, "hsv")
    hsv = hsv[:, :, 1]
    #display(hsv, "1")

    hsv[hsv < 100] = 0
    #display(hsv, "blackwhite")

    # xfirst = np.argmax(new_image_y > 100)
    # xlast = len(new_image_y) - np.argmax(new_image_y[::-1] > 100) - 1
    # yfirst = np.argmax(new_image_x > 100)
    # ylast = len(new_image_x) - np.argmax(new_image_x[::-1] > 100) - 1
    # cv2.rectangle(ori, (xfirst, yfirst), (xlast, ylast), (250), 3)

    contours, hierarchy = cv2.findContours(hsv, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    c = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(c)
    g = ori.copy()
    # x, y, w, h = cv2.boundingRect(i)
    cv2.rectangle(g, (x, y), (x + w, y + h), (250), 3)



    # display(opening, "rotifer")
    #display(g, "cntr")

    crop_img = ori[y:y + h, x:x + w]
    #return crop_img
    cv2.imwrite(file, crop_img)
    #display(crop_img, "cropped")

    #cv2.waitKey(0)
    #cv2.destroyAllWindows()