import cv2
import numpy as np
from RS_toolkit import RS_read
from RS_toolkit import cordinate_3D
from RS_toolkit import euclidean_distance_between_2_points

start_point = (0,0)
end_point = (0,0)

cord1 = []
cord2 = []

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY,start_point,end_point,cord2,cord1
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(frame,(x,y),5,(255,0,0),-1)
        mouseX,mouseY = x,y
        print(mouseX,mouseY)

        if end_point != (0,0) and start_point != (0,0):
            end_point = (0,0)
            start_point = (0,0)
            cord1 = []
            cord2 = []

        if end_point == (0,0) and start_point != (0,0):
            end_point = (mouseX,mouseY)
            cord2 = cordinate_3D(df, cint, mouseX, mouseY)
            print(cord1)
            dis = euclidean_distance_between_2_points(cord1, cord2)
            print(dis)

        if start_point == (0, 0):
            start_point = (mouseX,mouseY)
            cord1 = cordinate_3D(df, cint, mouseX, mouseY)
            print(cord1)







cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
#vid = cv2.VideoCapture(0)

while(1):
    #ret, frame = vid.read()
    df, dci, ci, cint = RS_read()

    frame = ci
    depth_frame = dci

    if(start_point != (0,0) and end_point != (0, 0)):
        frame = cv2.line(frame, start_point, end_point, (0,0,255), 2)
        depth_frame = cv2.line(depth_frame, start_point, end_point, (255, 0, 255), 2)
        cord1 = cordinate_3D(df, cint, 100, 100)

    if(start_point != (0,0)):
        frame = cv2.circle(frame, start_point, 5, (255, 0, 0), -1)
        depth_frame = cv2.circle(depth_frame, start_point, 5, (0, 0, 0), -1)

    if (end_point != (0, 0)):
        frame = cv2.circle(frame, end_point, 5, (0, 255, 0), -1)
        depth_frame = cv2.circle(depth_frame, end_point, 5, (0, 0, 0), -1)





    cv2.imshow('image', frame)
   # cv2.imshow('depth_map',depth_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break