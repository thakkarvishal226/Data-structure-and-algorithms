import cv2


if __name__ == "__main__":
    img = cv2.imread(r"test.png")

    cv2.imshow("original",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()