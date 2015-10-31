## 概述

這個範例展示如何透過OpenCV控制相機


## 使用方法

這個範例包含了一隻程式，內含一個名為OpenCV_Cam的Class，呼叫以控制相機各種功能。


### 執行範例

	> python cam.py


### OpenCV_Cam呼叫範例

    cam = OpenCV_Cam()
    cam.size = (640, 480)

    info = cam.info
    for i in info:
        print i,'=', info[i]
    
    cam.cam_loop()


### OpenCV_Cam 的函數

- cam_count() 取得電腦上攝影機的數量
- read() 取得一張影像
- set(property, value) 設定攝影機相關屬性
- camera_loop(func = lambda x:x , params = ())　持續抓取影像，經過 func 函數處理並且顯示出來。按p印出攝影機資訊；按s設定屬性，請先用p顯示屬性名稱接著輸入；按f取得實際的FPS。


### OpenCV_Cam 的屬性

- .size 設定或取得攝影機畫面大小
- .frame_rate 取得攝影機每秒禎數
- .info 取得攝影機資訊



