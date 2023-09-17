# YOLOv8 Object Detection Model
_______________________________
This is an object detection model created using the YOLOv8.
The dataset used for training the model was part obtained from roboflow (already annotated) and part obtained and annotated by myself

Links to the pre annotated datasets i cloned:
----------
		https://universe.roboflow.com/w0/shapess
 ----
		https://universe.roboflow.com/pusan-univ-agrqj/shpae-detect

_______________________________________________


## Guide
### The jupyter notebook contains the code used for traing the model
To train the model upload the dataset zip file into the runtime of the jupyter notebook (/content if in google collab)

Running all cells will unzip the dataset, train the model, validate the model, and then test the model with the test images provided within the dataset

If the training fails for any reason during runtime, there is a resume training cell

to test any images or mp4 videos, upload them into the run time and place their path into the prediction function

	model=YOLO("/content/runs/detect/train/weights/best.pt")
	result=model.predict(source="your/content/here",save=True)
----------------------------------
### The dataset contains 76 images with 476 annotations

* 47 training images
* 20 validation images
* 9 testing images

The dataset was annotated using [the Roboflow annotator](https://roboflow.com/annotate)
---------------------------------


### The boundarymaker folder contains the model, main.py file, adn a sample image
make sure the `predictions` folder and the `model.pt` file are both present within the boundarymaker folder

A `sample-image.jpg` is provided for testing

Upload any images to the boundarymaker folder and input its name when running the code
