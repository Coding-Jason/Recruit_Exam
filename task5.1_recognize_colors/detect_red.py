import cv2
import numpy as np
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python detect_red.py path/to/test_red_armor.jpg")
        sys.exit(1)

    img_path = sys.argv[1]
    image = cv2.imread(img_path)

    if image is None:
        print("Error: Could not load image", img_path)
        sys.exit(1)

    # BGR → HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 红色在HSV空间有两个区间
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])

    # 生成掩码
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    # 显示
    cv2.imshow("Original", image)
    cv2.imshow("Red Mask", mask)

    print("Press any key to close windows...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
