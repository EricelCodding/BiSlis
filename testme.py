
import cv2

# 创建 VideoCapture 对象，0 表示使用计算机上的第一个摄像头
cap = cv2.VideoCapture(0)

while True:
    # 从摄像头读取一帧图像
    ret, frame = cap.read()

    # 判断是否读取成功
    if not ret:
        print('Failed to read frame from camera')
        break

    # 显示图像
    cv2.imshow('Camera', frame)

    # 按下 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头资源
cap.release()
cv2.destroyAllWindows()