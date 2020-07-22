#Aref pourhashemi
import numpy as np
import cv2

def mousecall(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK: #condition for double click
        zoomin(x,y)

        
        
def mousecall2(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK: #condition for double click
        gussi()  

def mousenone(event,x,y,flags,param):

    return 0
    
def zoomin(x,y):
    
    cv2.setMouseCallback('apple', mousenone)
    
    x1 = x - 160
    
    if x1 < 0:
        x1 = 0
    
    x2 = x + 160
    
    if x2 > 640:
        x2 = 640
        
    y1 = y - 96
    
    if y1 < 0:
        y1 = 0
    
    y2 = y + 96
        
    if y2 > 480:
        y2 = 480
    
    pts1 = np.float32([[x1,y1],[x2,y1],[x1,y2],[x2,y2]])
    pts2 = np.float32([[0,0],[320,0],[0,192],[320,192]]) #make matrix for zoom

    M = cv2.getPerspectiveTransform(pts1,pts2)

    dst = cv2.warpPerspective(apple,M,(320,192))  #use matrix for zoom

    cv2.imshow('zoom picture',dst) #show zoomed picture


def gussi():
    blurred = cv2.GaussianBlur(apple, (11, 11), 0)  #use gussian filter
    cv2.imshow("blurred picture",blurred)

###############################
apple=cv2.imread("apple.jpg")

cv2.imshow('pic',apple)
cv2.imshow("zoom picture",apple)

cv2.setMouseCallback('pic', mousecall) #call mouse for zoom
cv2.setMouseCallback('zoom picture', mousecall2) #call mouse for blur


cv2.waitKey(0)
cv2.destroyAllWindows()