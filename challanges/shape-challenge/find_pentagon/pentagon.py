'''
find_parallelograms.py
=========
Spot all the pentagon by webcam

Usage
-----
python find_parallelograms.py

'''


import numpy as np
from numpy import linalg as LA

import cv2
from cam import OpenCV_Cam


def contour_proc(frame, debug=False):
    
    # convert color to gray scale and show it
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if debug: cv2.imshow('gray', gray)
    
    # blur the result from edge detection to ensure continuity
    edge = cv2.Canny(gray, 30, 100)
    edge = cv2.blur(edge, (2,2))
    if debug: cv2.imshow('blured edge', edge)
    
    
    # convert image to black and white and show it
    thresh1, thresh = cv2.threshold(edge, 60, 255, cv2.THRESH_BINARY)
    if debug: cv2.imshow('thresh', thresh)
    
    # find contours!
    contours, hry = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # draw all the contours
    cpframe = frame.copy()
    cv2.drawContours(cpframe, contours, -1, (0,255,0), 3)
    if debug: cv2.imshow('cpframe', cpframe)
    
    # ================== TODO ===================
    
    # Modify these code to suit your need
    
    parallelograms = find_pentagons(contours)
        
    # ============================================
    
    # draw on the frame
    cv2.drawContours(frame, parallelograms, -1, (0,255,0), 3)
    
    return frame

    
def find_pentagons(contours):
    pentagons = []
    for ctr in contours:
        area = cv2.contourArea(ctr)
        
        # area test
        if area < 400: continue
        
        simp_ctr = cv2.approxPolyDP(ctr, 3, True)
        simp_area = cv2.contourArea(simp_ctr)
        if simp_area < 400: continue
        if len(simp_ctr) != 5: continue
        
        edges = [LA.norm(a-b) for a, b in zip(simp_ctr, np.roll(simp_ctr, 2))]
        
        ratios = [(1 - e/edges[0])** 2 for e in edges]
        
        passr = [r for r in ratios if r > 0.2]
        if len(passr) > 0: continue
        
        pentagons.append(simp_ctr)
        
    return pentagons

    
if __name__ == "__main__":
    cam = OpenCV_Cam()
    cam.cam_loop(contour_proc)