import cv2
import cvzone
from pygame import mixer
from cvzone.HandTrackingModule import HandDetector
mixer.init()
mixer.music.load("music.mp3")
cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

Shiv=cv2.imread("Shivling.png",cv2.IMREAD_UNCHANGED)
Shiv=cv2.resize(Shiv,(600,600))
detector=HandDetector(detectionCon=0.85)
mixer.music.play(-1)
mixer.music.pause()
class Bell:
    def __init__(self):
        self.pos="C"
        self.img=cv2.imread("bell.png",cv2.IMREAD_UNCHANGED)
    def update(self,pos):
        self.pos=pos
        if(pos=="L"):
            self.img=cv2.imread("bellL.png",cv2.IMREAD_UNCHANGED)
        else:
            self.img=cv2.imread("bellR.png",cv2.IMREAD_UNCHANGED)

obj=Bell()
while True:
    succ,img=cap.read()
    img=cv2.flip(img,1)
    img=cvzone.overlayPNG(img,Shiv,[670,30])
    img=cvzone.overlayPNG(img,obj.img,[10,10])
    img=cvzone.overlayPNG(img,obj.img,[10,230])
    img=cvzone.overlayPNG(img,obj.img,[10,460])
    hands, img=detector.findHands(img)
    if hands:
        lmList=hands[0]["lmList"]
        length,info,img=detector.findDistance(lmList[8],lmList[12],img)
        if length<60:
            mixer.music.unpause()
            if(obj.pos=="C"):
                obj.update("L")
            elif(obj.pos=="R"):
                obj.update("L")
            else:
                obj.update("R")
        else:
            mixer.music.pause()
    else:
        mixer.music.pause()

    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.imshow("window",img)
    cv2.waitKey(1)