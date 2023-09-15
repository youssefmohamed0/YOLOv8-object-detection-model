import ultralytics
from ultralytics import YOLO
import os
import shutil
from PIL import Image as im

###upload the desired image to the boundrymaker folder

img_name=input("enter image name with extension: ")
model=YOLO("model.pt")
result=model.predict(source=f"{img_name}",save=True)    #the model makes the boundaries on the image

pic=im.open(f"runs\\detect\\predict\\{img_name}")
pic.show(f"bounding-boxes-{img_name}")      #the image pops up in a window

shutil.move(f"runs\\detect\\predict\\{img_name}", f"predictions\\modified-{img_name}")  #asve predicted images into a prediction folder
os.rmdir("runs\\detect\\predict")










