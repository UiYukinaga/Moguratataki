# moguratataki v2

import os
import pyautogui as pg
import time

def moguratataki():
    hit_count = 0
    start_time = time.time()
    
    cur_dir = os.getcwd()
    print(cur_dir)

    field_img = os.getcwd() + "/img/field.png"
    
    # Search to Center position of Battle field.
    try:
        center_x, center_y = pg.locateCenterOnScreen(field_img, grayscale=True, confidence=0.8)
    except TypeError:
        print("ERROR: Battle Field NOT found.")
        print("FINISH")
        return 1
    else:
        print("System Standby...Success!")
        
    # マウスポインタの位置が真ん中の穴の中心にくるようにオフセット値を調整してください
    offset_x = 0
    offset_y = 25

    pg.moveTo(center_x + offset_x, center_y + offset_y, duration= 0.5)
    col = pg.pixel(int(center_x + offset_x), int(center_y + offset_y))
    res = isTarget(col)
    if res > 0:
        print("ERROR: The center coordinates are out of alignment.")
        print("Please, Calibrate offsets.")
    
    # キャリブレーション時は下のreturnをコメントアウト解除すること！
#    return 0

    print("スタンバイOK!「ゲーム開始」をクリックしてね！")

    # Set Attack Points
    points = [[center_x - 150, center_y - 150],
              [center_x - 0, center_y - 150],
              [center_x + 150, center_y - 150],
              [center_x - 150, center_y + 0],
              [center_x - 0, center_y + 0],
              [center_x + 150, center_y + 0],
              [center_x - 150, center_y + 150],
              [center_x - 0, center_y + 150],
              [center_x + 150, center_y + 150]]

    while True:
    
        for i in range(9):            
            x, y = points[i]
            x = x + offset_x
            y = y + offset_y
            col = pg.pixel(int(x), int(y))
            res = isTarget(col)
            if res > 0:
                pg.moveTo(int(x), int(y), duration=0.1)
                pg.click()
                hit_count += 1
                print("おりゃ！")
            
        if hit_count == 1:
            start_time = time.time()
        
        cur_time = time.time()
        d_t = cur_time - start_time
        if d_t > 65:
            break


    
# Is the cursor on the target?
# Return: Yes=1, No=0
def isTarget(rgb):
    # Set Target Color
#    target_rgb = (247, 150, 70)
    
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    
    if r < 10 and g < 10 and b < 10:
        return 0
    else:
        return 1

if __name__ == '__main__':
    moguratataki()
