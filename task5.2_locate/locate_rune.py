import cv2
import numpy as np
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python locate_rune.py path/to/test_rune.png")
        sys.exit(1)

    img_path = sys.argv[1]
    image = cv2.imread(img_path)

    if image is None:
        print("Error: Could not load image", img_path)
        sys.exit(1)

    # 转灰度
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 自适应阈值，比固定100更鲁棒
    binary = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 35, 5
    )

    # 查找轮廓（使用 TREE 可以拿到所有层级）
    contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    best_contour = None
    best_score = 0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt, True)
        if perimeter == 0 or area < 100:
            continue
        circularity = 4 * np.pi * (area / (perimeter * perimeter))

        # 筛选条件：圆度接近1，面积不能太小
        if 0.7 < circularity <= 1.2 and area > best_score:
            best_score = area
            best_contour = cnt

    if best_contour is not None:
        x, y, w, h = cv2.boundingRect(best_contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, "Rune", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    else:
        print("No circular contour found.")

    # 显示结果
    cv2.imshow("Original with ROI", image)
    cv2.imshow("Binary", binary)

    print("Press any key to close windows...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
