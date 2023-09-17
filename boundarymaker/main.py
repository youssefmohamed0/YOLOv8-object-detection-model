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
model=YOLO("model.pt")
if choice==2:
    print("Smile to the camera :)")
    time.sleep(2)
    cam=cv2.VideoCapture(0)    #if this doesn't work try changing the '0' to '1' or '2', '0' should work on integrated webcams
    if cam.isOpened():
        ret, frame = cam.read()
        result = model.predict(source=frame, save=True)
        pic = im.open(f"runs\\detect\\predict\\image0.jpg")
        pic.show()
        shutil.move(f"runs\\detect\\predict\\image0.jpg",f"predictions\\modified-camera-capture.jpg")  # asve predicted images into a prediction folder
        os.rmdir("runs\\detect\\predict")
    else:
        print("Cannot open camera")

elif choice==1:

    img_name=input("enter image name with extension: ")

    result=model.predict(source=f"{img_name}",save=True)    #the model makes the boundaries on the image

    pic=im.open(f"runs\\detect\\predict\\{img_name}")
    pic.show()      #the image pops up in a window

    shutil.move(f"runs\\detect\\predict\\{img_name}", f"predictions\\modified-{img_name}")  #asve predicted images into a prediction folder
    os.rmdir("runs\\detect\\predict")
else:
    print("Inavlid input")
