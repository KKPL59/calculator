import cv2
import numpy as np
from time import sleep



img = cv2.imread("white_board.png")

drawing=False
mode=True

def paint_draw(event,former_x,former_y,flags,param):
    global current_former_x,current_former_y,drawing, mode

    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        current_former_x,current_former_y=former_x,former_y

    elif event==cv2.EVENT_MOUSEMOVE:

        if drawing==True:
            if mode==True:

                # cv2.line(img,(current_former_x,current_former_y+8),(former_x,former_y),(0,0,0),1)
                # cv2.line(img,(current_former_x,current_former_y+4),(former_x,former_y),(50,50,50),3)
                cv2.line(img,(current_former_x,current_former_y),(former_x,former_y),(0,0,0),12)
                # cv2.line(img,(current_former_x,current_former_y-4),(former_x,former_y),(50,50,50),3)
                # cv2.line(img,(current_former_x,current_former_y+8),(former_x,former_y),(0,0,0),1)


                current_former_x = former_x
                current_former_y = former_y

    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False

        if mode==True:

            # cv2.line(img, (current_former_x, current_former_y + 8), (former_x, former_y), (0, 0, 0), 1)
            # cv2.line(img, (current_former_x, current_former_y + 4), (former_x, former_y), (50, 50, 50), 3)
            cv2.line(img, (current_former_x, current_former_y), (former_x, former_y), (0,0,0), 12)
            # cv2.line(img, (current_former_x, current_former_y - 4), (former_x, former_y), (50, 50, 50), 3)
            # cv2.line(img, (current_former_x, current_former_y + 8), (former_x, former_y), (0, 0, 0), 1)

            current_former_x = former_x
            current_former_y = former_y


    return former_x,former_y




cv2.namedWindow("OpenCV Paint Brush")
cv2.setMouseCallback('OpenCV Paint Brush',paint_draw)


while(1):
    cv2.imshow('OpenCV Paint Brush',img)
    k=cv2.waitKey(1)& 0xFF
    if k==27: #Escape KEY
        # cv2.destroyAllWindows()
        img = img
        # cv2.imshow("JD", img)
        # cv2.waitKey(0)
        break

