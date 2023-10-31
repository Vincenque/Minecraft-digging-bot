import pytesseract
import numpy as np
from mss import mss
import cv2
import time
import keyboard
from PIL import Image as im
import matplotlib.pyplot as plt
import win32api, win32con
import sys
import pyautogui

# Required Tesseract-OCR link
# https://github.com/UB-Mannheim/tesseract/wiki

# Minecraft required Font link
# https://www.curseforge.com/minecraft/texture-packs/tech-rpg-font/download/4455712

# Run minecraft in full sized window (not full screen) with screen resolution 1920x1080

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
left_coordinates = 2; right_coordinates = 500
top_coordinates = 296; bottom_coordinates = 322;
bounding_box_coordinates = {'top': top_coordinates, 'left': left_coordinates, 'width': right_coordinates-left_coordinates, 'height': bottom_coordinates-top_coordinates}

left_angles = 2; right_angles = 650;
top_angles = 374; bottom_angles = 404;
bounding_box_angles = {'top': top_angles, 'left': left_angles, 'width': right_angles-left_angles, 'height': bottom_angles-top_angles}

left_targeted_block = 1500; right_targeted_block = 1918;
top_targeted_block = 458; bottom_targeted_block = 484;
bounding_box_targeted_block = {'top': top_targeted_block, 'left': left_targeted_block, 'width': right_targeted_block-left_targeted_block, 'height': bottom_targeted_block-top_targeted_block}


def check_coordinates():
    num_coordinates = np.array(sct.grab(bounding_box_coordinates))
    #ret,num_coordinates = cv2.threshold(num_coordinates,127,255,cv2.THRESH_BINARY_INV)
    num_coordinates = cv2.resize(num_coordinates, None, fx = 3, fy = 3)
    #cv2.imshow('coordinates', num_coordinates)
    #plt.imshow(num_coordinates)
    recognised_string = pytesseract.image_to_string(num_coordinates)
    #print("\n\nrecognised_string=",recognised_string)
    recognised_list = recognised_string.split("/")
    #print("recognised_list=",recognised_list)
    global x_coordinate; global y_coordinate; global z_coordinate;
    try:
        x_coordinate = float(recognised_list[0].split(":")[1])
        y_coordinate = float(recognised_list[1])
        z_coordinate = float(recognised_list[2])
    except ValueError:
        check_coordinates()
    print("x_coordinate = ", x_coordinate, ", y_coordinate = ", y_coordinate, ", z_coordinate = ", z_coordinate)

def check_angles():
    num_angles = np.array(sct.grab(bounding_box_angles))
    num_angles = cv2.resize(num_angles, None, fx = 3, fy = 3)
    #cv2.imshow('coordinates', num_angles)
    recognised_string = pytesseract.image_to_string(num_angles)
    #print("\n\nrecognised_string=",recognised_string)
    recognised_list = recognised_string.replace(")","").replace("D","0").replace("O","0").split("(")[2].split("/")
    print("recognised_list=",recognised_list)
    global x_angle; global y_angle; global z_angle;
    try:
        x_angle = float(recognised_list[0])
        y_angle = float(recognised_list[1])
    except ValueError:
        check_angles()
    print("x_angle = ", x_angle, ", y_angle = ", y_angle)

def check_targeted_block():
    num_targeted_block = np.array(sct.grab(bounding_box_targeted_block))
    num_targeted_block = cv2.resize(num_targeted_block, None, fx = 3, fy = 3)
##    cv2.imshow('targeted_block', num_targeted_block)
    recognised_string = pytesseract.image_to_string(num_targeted_block)
    print("\n\nrecognised_string=",recognised_string)
    recognised_list = recognised_string.split(":")[1].split(",")
    print("recognised_list=",recognised_list)
    global x_targeted_block; global y_targeted_block; global z_targeted_block;
    try:
        x_targeted_block = float(recognised_list[0])
        y_targeted_block = float(recognised_list[1])
        z_targeted_block = float(recognised_list[2])
    except ValueError:
        check_targeted_block()
    print("x_targeted_block = ", x_targeted_block, ", y_targeted_block = ", y_targeted_block, ", z_targeted_block = ", z_targeted_block)


def set_angle(x_angle_new, y_angle_new):
    #print("set_angle(",x_angle_new," ",y_angle_new,")")
    check_angles()
    #print("x_angle_new = ",x_angle_new,",  x_angle = ", x_angle)
    #print("y_angle_new = ",y_angle_new,",  y_angle = ", y_angle,"\n")
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,int(round((-x_angle+x_angle_new)*1000/35,0)),int(round((- y_angle+y_angle_new)*1000/35,0)))
    check_angles()
    while(round(abs(x_angle_new - x_angle),2) > 0.1 or round(abs(y_angle_new - y_angle),2) > 0.1):
        #print("Repeating setting angle")
        set_angle(x_angle_new, y_angle_new)
        check_angles()

time_to_dig_one_block_with_diamond_pickaxe = 0.82
sct = mss()
print("Script is ready. Press F7")
dig = False
while 1:
    if keyboard.is_pressed("F7"):
        print("F7 pressed. Starting script. Press F6 to stop.")
        dig = True
    while dig == True:
        if keyboard.is_pressed("F6"):
            print("F6 pressed. Stopping script.")
            dig = False
            sys.exit()

            
        set_angle(0,30)
        pyautogui.mouseDown(button="left")
        pyautogui.keyDown('w')
        time.sleep(6*time_to_dig_one_block_with_diamond_pickaxe)
        #pyautogui.mouseUp(button="left")

        set_angle(-90,0)
        time.sleep(5*time_to_dig_one_block_with_diamond_pickaxe)

        set_angle(90,0)
        time.sleep(5*time_to_dig_one_block_with_diamond_pickaxe)
        pyautogui.mouseUp(button="left")
        pyautogui.keyUp('w')
        

##        #Check if you can step one block forward
##        set_angle(0,60)
##        check_coordinates()
##        check_targeted_block()
        
    
        #sys.exit()
        
            
