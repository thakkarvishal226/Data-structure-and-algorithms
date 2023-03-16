import cv2
import numpy as np


def filtering(img,filter):
    pass


if __name__ == "__main__":
    img = cv2.imread(r"C:\Users\vthakkar\Documents\Vthakkar_python\CV\Ben10.png")
    img = cv2.resize(img,((1024,1024)),img)
    cv2.imshow("original", img)
    
    filter = np.array([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]) / 50
    averagefilter = cv2.filter2D(img,0,filter)
    gueassianblur = cv2.GaussianBlur(img.copy(),(25,25),cv2.BORDER_DEFAULT)
    cv2.imshow("average_filtering", averagefilter)
    cv2.imshow("gaussian_filtering", gueassianblur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
