# 任务一：识别敌方机器人颜色

## 思路说明
1. **图像加载**  
   - 使用 OpenCV 读取输入的测试图片 `test_red_armor.jpg`。  

2. **颜色空间转换**  
   - 将图像从 BGR 转换为 HSV 色彩空间。  
   - HSV 空间比 BGR 更容易做颜色分割。  

3. **阈值分割**  
   - 设定红色的 HSV 范围（因为红色跨越 HSV 的 0° 和 180°，所以设定两个区间）。  
   - 使用 `cv2.inRange` 生成红色区域的二值化掩码。  

4. **结果显示**  
   - 显示原始图片。  
   - 显示提取出的红色区域掩码。  

---

## 运行方法
进入 `task5.1_red_detect` 文件夹后执行：

```bash
python3 detect_red.py ./test_red_armor.jpg
