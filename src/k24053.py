import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()
    # カメラキャプチャ画像をファイルに保存
    try:
        app.write_img('images/camera_capture.png')
    except ValueError as e:
        print(f"エラー: {e}")
        return
    

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    # 【重要】google_imgがNoneの場合はここで終了 (ファイルパスのエラーに対応)
    if google_img is None:
        print("致命的なエラー: 'images/google.png' が見つかりませんでした。ファイルパスと存在を確認してください。")
        return
    
    capture_img : cv2.Mat = cv2.imread('images/camera_capture.png') # 動作テスト用なので提出時にこの行を消すこと
    # capture_img : cv2.Mat = "implement me"
    # capture_imgがNoneの場合も終了
    if capture_img is None:
        print("エラー: 'images/camera_capture.png' の読み込みに失敗しました。キャプチャが成功したか確認してください。")
        return  

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    print(google_img.shape)
    print(capture_img.shape)

    capture_resized : cv2.Mat = cv2.resize(capture_img, (g_width, g_hight), interpolation=cv2.INTER_LINEAR)
    print(capture_resized.shape)
    
    for x in range(g_width):
        for y in range(g_hight):
            g, b, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                tile_x = x % c_width  # xは0-1279 -> 0-639, 0-639, ...
                tile_y = y % c_hight # yは0-639 -> 0-479, 0-159, ...
                google_img[y, x] = capture_img[tile_y, tile_x]

                #implement me

    # 書き込み処理
    # 新たな画像として保存
    cv2.imwrite('output_images/lecture05_01_k24053.png', google_img)
    print("\n合成結果を 'output_images/lecture05_01_k24053.png' に保存しました。")
    