import cv2
import cv2.aruco as aruco
import numpy as np

# 创建空白图像，用于输出
output_size = (800, 600, 3)
output_image = np.zeros(output_size, dtype=np.uint8)

h = 800
w = 600
# 四个待选取的点坐标
src_points = np.float32([[125, 50], [645, 15], [170, 410], [635, 400]])
dst_points = np.float32([[0.0, 0.0], [w, 0.0], [0.0, h], [w, h]])

# 初始化摄像头
cap = cv2.VideoCapture(1)

# 设置 ArUco 字典
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_250)

# 创建 ArUco 参数
parameters = cv2.aruco.DetectorParameters_create()


while True:
    # 读取摄像头帧
    ret, frame = cap.read()

    matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    
    warped_image = cv2.warpPerspective(frame, matrix, (w, h))

    # 将仿射变换后的图像复制到输出图像中
    output_image[:warped_image.shape[0], :warped_image.shape[1]] = warped_image

    # 调整输出图像的大小
    output_image_resized = cv2.resize(output_image, (800, 600))

    gray = cv2.cvtColor(output_image_resized, cv2.COLOR_BGR2GRAY)

    # 检测 ArUco 标记
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    # 在图像上绘制检测到的标记
    if ids is not None:
        cv2.aruco.drawDetectedMarkers(output_image_resized, corners)
        for i in range(len(ids)):
            # 获取标记的中心坐标
            center_x = int(np.mean(corners[i][0][:, 0])) - 20
            center_y = int(np.mean(corners[i][0][:, 1]))

            # 在图像上绘制中心点
            cv2.circle(output_image_resized, (center_x, center_y), 5, (0, 255, 0), -1)

            # 在图像上显示坐标信息
            cv2.putText(output_image_resized, f"Center: ({center_x}, {center_y})", (center_x, center_y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # 计算方向向量
            direction_vector = (corners[i][0][1] - corners[i][0][0]) / np.linalg.norm(corners[i][0][1] - corners[i][0][0])
            cv2.putText(output_image_resized, f"Direction: {direction_vector}", (center_x, center_y + 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            print(direction_vector[0],direction_vector[1])
    else:
        center_x=150
        center_y=250
        direction_vector=[1,0]
        # 在图像上绘制中心点
        cv2.circle(output_image_resized, (center_x, center_y), 5, (0, 255, 0), -1)

        # 在图像上显示坐标信息
        cv2.putText(output_image_resized, f"Center: ({center_x}, {center_y})", (center_x, center_y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.putText(output_image_resized, f"Direction: {direction_vector}", (center_x, center_y + 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    # 显示帧
    cv2.imshow('ArUco Marker Detection', output_image_resized)
    
    # 检测键盘按键，如果是ESC键则退出循环
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
