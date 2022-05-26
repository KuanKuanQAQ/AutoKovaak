import time
import math
from unittest.case import doModuleCleanups
import pydirectinput
import cv2
import numpy as np
import pyautogui
import random

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def good_thresh_img(img):
    #draw_img = img.copy() 
    gs_frame = cv2.GaussianBlur(img, (5, 5), 0) #高斯滤波
    hsv = cv2.cvtColor(gs_frame, cv2.COLOR_BGR2HSV) # 转化成HSV图像
    erode_hsv = cv2.erode(hsv, None, iterations=2)

    for i in target_color:
        mask = cv2.inRange(erode_hsv, color_dist[i]['Lower'], color_dist[i]['Upper'])
        if i == target_color[0]:
            inRange_hsv=cv2.bitwise_and(erode_hsv,erode_hsv,mask = mask)
             #cv_show('res',inRange_hsv)#不必要，用于调试
        else:
            inRange_hsv1=cv2.bitwise_and(erode_hsv,erode_hsv,mask = mask)
            #cv_show('res1',inRange_hsv1)#不必要，用于调试
            inRange_hsv=cv2.add(inRange_hsv,inRange_hsv1)
            #cv_show('res2',inRange_hsv)#不必要，用于调试
    
    inRange_gray = cv2.cvtColor(inRange_hsv, cv2.COLOR_BGR2GRAY)
    contours, _ = cv2.findContours(inRange_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    target_list = []
    for c in contours:
        if cv2.contourArea(c) < 0:
            continue
        else:
            target_list.append(c)
    #for i in target_list:
        #rect = cv2.minAreaRect(i)
        #box = cv2.boxPoints(rect)
        #cv2.drawContours(draw_img, [np.int0(box)], -1, (0, 255, 255), 2)

    dis_list = []
    center_list = []
    for c in target_list:
        M = cv2.moments(c) #计算中心点的x、y坐标
        try:
            center_x = int(M['m10']/M['m00'])
            center_y = int(M['m01']/M['m00'])
        except:
            continue
        dis_list.append((center_x - 1280)**2 + (center_y - 720)**2)
        center_list.append((center_x, center_y))
        #print('center_x:',center_x) #打印（返回）中心点的x、y坐标
        #print('center_y:',center_y)
        #cv2.circle(draw_img, (center_x, center_y), 7, 128, -1)
        #str1 = '('+str(center_x)+','+str(center_y)+')'
        #cv2.putText(draw_img, str1,(center_x-50,center_y+40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA)#绘制坐标点位
    #cv_show('final_img',draw_img)

    return center_list[dis_list.index(min(dis_list))]

###主函数部分
#创建颜色字典
color_dist = {
    'red': {'Lower': np.array([0, 43, 46]), 'Upper': np.array([10, 255, 255])},
    'yellow': {'Lower': np.array([15, 160, 50]), 'Upper': np.array([35, 255, 255])},
    'green': {'Lower': np.array([50, 50, 50]), 'Upper': np.array([130, 255, 255])},
}
#目标颜色
target_color = ['red']

#img = cv2.imread('red.png',cv2.COLOR_BGR2RGB) #读入图像（直接读入灰度图）
#img = cv2.imread('d.png',cv2.COLOR_BGR2RGB) #读入图像（直接读入灰度图）
#img = cv2.imread('example.jpg',cv2.COLOR_BGR2RGB) #读入图像（直接读入灰度图）
#print(good_thresh_img(img))
#exit()
pydirectinput.moveTo(1280,720)
time.sleep(3)
tot_x = 0
tot_y = 0
while True:
    
    start_time = time.time()
    #image = cv2.imread('c.png')
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
    (center_x,center_y) = good_thresh_img(image)
    #print('cal center time:', time.time() - start_time)
    if abs(center_x - 1280) < 5 and abs(center_y-720) < 5:
        start_time = time.time()
        pydirectinput.keyDown('shift')#按下shift
        pydirectinput.keyUp('shift')#弹起shift
        print('tot', tot_x, tot_y)
        #pydirectinput.move(-tot_x,-tot_y)
        print(pyautogui.position())
        if pyautogui.position()[1] == 0 or pyautogui.position()[1] == 1439:
            pydirectinput.moveTo(1280,720)
        tot_x = 0
        tot_y = 0
        #print('key time:', time.time() - start_time)
    print(center_x, center_y)
    t = 1
    x_move = int((center_x-1280)*t)
    y_move = int((center_y-720)*t)
    d_move = math.sqrt(x_move**2 + y_move**2)
    arch = math.atan(d_move / 983.412472) * 180 / math.pi
    inch = (arch / 360) * 4.09091
    d_acc_move = 800 * inch
    print(d_move, d_acc_move)
    if d_move == 0:
        continue
    t = d_acc_move / d_move
    x_move = int((center_x-1280)*t)
    y_move = int((center_y-720)*t)
    start_time = time.time()
    print(x_move, y_move)
    print(pyautogui.position())

    pydirectinput.move(x_move,y_move)
    tot_x += x_move
    tot_y += y_move
    #print('move time:', time.time() - start_time)






