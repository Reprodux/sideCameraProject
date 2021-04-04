import cv2
import numpy as np



# mouse callback function

mode = False
drawing = False
ix,iy = -1,-1

def draw_circle(event,x,y,flags,param):
    #if event == cv2.EVENT_LBUTTONDBLCLK:
    #   cv2.circle(img,(x,y),100,(255,0,0),-1)
    global ix,iy, drawing, mode 
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)
                
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)
        
    
    
def onScreen(event, x, y, flags, param):
    global locations
    if(event == cv2.EVENT_LBUTTONDBLCLK):
        locations.append((x,y))


def recScreen(event, x, y, flags, param):
    global start, end, drawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if drawing == False:
            start = (x,y)
            drawing = not drawing
        else:
            drawing = not drawing
            
    
    elif event == cv2.EVENT_MOUSEMOVE:
       
        if drawing == True:
            end = (x,y)
    
    
    
def paint(event, x, y, flags, param):
    global start, end, drawing
    
    global locations
    if(event == cv2.EVENT_LBUTTONDOWN):
        drawing = not drawing
    elif(event == cv2.EVENT_MOUSEMOVE):
        if(drawing):
            locations.append((x,y))
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

while(1):
    ret, img = cam.read()
    img = cv2.flip(img,1)
    fps = cam.get(cv2.CAP_PROP_FPS)
    fpsTrack = str(fps) + " FPS"
    
    cv2.putText(img, fpsTrack, (50,50),font, 1, (0,255,0),2,cv2.LINE_8)
    
    #paint event
    for i in range(len(locations)):
        print(locations[i])
        cv2.circle(img,locations[i],5,(0,0,255),-1)
        
        
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
