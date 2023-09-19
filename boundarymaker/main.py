import ultralytics
from ultralytics import YOLO
import os
import shutil
from PIL import Image as im
import cv2
import time
###upload the desired image to the boundrymaker folder
print("Do you want to upload an image or use camera?")
choice=int(input("1)Image\n2)Camera"))
model=YOLO("final-model.pt")    #assigning the model
if choice==2:
    print("Smile to the camera :)")
    time.sleep(2)
    cam=cv2.VideoCapture(0)    #if this doesn't work try changing the '0' to '1' or '2', '0' should work on integrated webcams
    if cam.isOpened():    #check to see if camera can be opened
        ret, frame = cam.read()      #frame is the captured picture
        result = model.predict(source=frame, save=True)    #add the bounding boxes using the model for prediction
        pic = im.open(f"runs\\detect\\predict\\image0.jpg")    #pic is the captured picture after the boundiong boxes were added
        pic.show()
        shutil.move(f"runs\\detect\\predict\\image0.jpg",f"predictions\\modified-camera-capture.jpg")  # asve predicted images into a prediction folder
        os.rmdir("runs\\detect\\predict")    #removing extra directories
    else:
        print("Cannot open camera")

elif choice==1:

    img_name=input("enter image name with extension: ")    #searches for an image of the same name in the boundarymaker folder

    result=model.predict(source=f"{img_name}",save=True)    #the model makes the boundaries on the image

    pic=im.open(f"runs\\detect\\predict\\{img_name}")
    pic.show()      #the image pops up in a window

    shutil.move(f"runs\\detect\\predict\\{img_name}", f"predictions\\modified-{img_name}")  #save predicted images into a prediction folder
    os.rmdir("runs\\detect\\predict")
else:
    print("Inavlid input")
os.rmdir("runs\\detect")    #removing extra directories
os.rmdir("runs")
