import cv2
import numpy as np


#hello world
# mouse callback function

mode = False
drawing = False
ix,iy = -1,-1

pinkbuttonCoord = [0,100,100,200]
bluebuttonCoord = [0,200,100,300]
greenbuttonCoord = [0,300,100,400]
bgr = [0,0,255]

color = (bgr[0],bgr[1],bgr[2])

pink = [255,0,255]
blue = [255,0,0]
green = [0,255,0]


def rectChec(coor, x, y):
    pressed = coor[0] <= x <= coor[2] and coor[1] <= y <= coor[3]
    return pressed
    
def paint(event, x, y, flags, param):
    global start, end, drawing, pinkbuttonCoord, bluebuttonCoord, bgr
    
    global locations
    if(event == cv2.EVENT_LBUTTONDOWN):
        if(rectChec(pinkbuttonCoord, x, y)):
            print(x,y)
            print("Clicked pink")
            bgr = pink
        
        elif(rectChec(bluebuttonCoord, x, y)):
            print(x,y)
            print("Clicked blue")
            bgr = blue
            
        elif(rectChec(greenbuttonCoord, x, y)):
            print(x,y)
            print("Clicked green")
            bgr = green
            
        drawing = not drawing
    elif(event == cv2.EVENT_MOUSEMOVE):
        if(drawing):
            locations.append((x,y))
            colors.append(color)
    elif(event == cv2.EVENT_LBUTTONUP):
        drawing = not drawing
        



start = () 
end = ()
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',paint)
font = cv2.FONT_HERSHEY_SIMPLEX
cam = cv2.VideoCapture(0)
locations = []
colors = []
ret, img = cam.read()

#buttonCoord = [(100,100),(200,200)]

while(1):
    ret, img = cam.read()
    img = cv2.flip(img,1)
    fps = cam.get(cv2.CAP_PROP_FPS)
    fpsTrack = str(fps) + " FPS"

    cv2.putText(img, fpsTrack, (50,50),font, 1, (0,255,0),2,cv2.LINE_8)
    cv2.rectangle(img,(pinkbuttonCoord[0],pinkbuttonCoord[1]),(pinkbuttonCoord[2],pinkbuttonCoord[3]),(255,0,255),-1)
    cv2.rectangle(img,(bluebuttonCoord[0],bluebuttonCoord[1]),(bluebuttonCoord[2],bluebuttonCoord[3]),(255,0,0),-1)
    cv2.rectangle(img,(greenbuttonCoord[0],greenbuttonCoord[1]),(greenbuttonCoord[2],greenbuttonCoord[3]),(0,255,0),-1)
    color = (bgr[0],bgr[1],bgr[2])
    #paint event
    for i in range(len(locations)):
        #print(locations[i])
        
        cv2.circle(img,locations[i],5,colors[i],-1)
        
        
    #recScreen
    #if(start and end):
    #    img = cv2.rectangle(img,start,end,(0,255,0),-1)
    
    
    #img = cv2.flip(img,1)
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        mode = not mode
        if(mode):
            print("rectangle mode")
        else:
            print("circle mode")
    if cv2.waitKey(20) & 0xFF == ord('f'):
        break
cv2.destroyAllWindows()
