import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    # capture_img : cv2.Mat = cv2.imread('images/camera_capture.png') # 動作テスト用なので提出時にこの行を消すこと
    capture_img : cv2.Mat = app.get_img()

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    print(google_img.shape)
    print(capture_img.shape)

    for x in range(g_width):
        for y in range(g_hight):
            g, b, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                if (g_hight > c_hight and g_width >= c_width):
                    google_img[y + g_hight, x] = capture_img[y, x]
                if (g_width > c_width and g_hight <= c_hight):
                    google_img[y, x + g_width] = capture_img[y, x]
                pass
                #implement me

    # 書き込み処理
    # implement me
    app.write_img('output_images/lecture05_01_k24039.png')

if __name__ == "__main__":
    app = MyVideoCapture()
    # app.run()
    # app.write_img()