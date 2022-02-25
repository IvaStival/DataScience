# Cars Recognition Study Using RCNN


The goal of this project is found cars in aerial images. To humans this is simple but for machine it is not that simple.
To resolve this problem I choose the RCNN method, it is not the best, but is simple to implement and is a good initial computer vision programming.

Well how this method works?
Briefly we can separate the method in some parts:
- Data acquisition;
- Data catalog;
- Selective Search (using OpenCv) to found the images objects;
- Calculate the IOU (Intersection Over Union) and generate the images to train;
- Training;
- Prediction test;

Now some explanation about each step.

## Data acquisition and Data catalog
In this steps we need to take the photos and catalog each car in each image.
Yes a big task, but I found a dataset with all ready.
You can find here: <Link to car dataset>

The dataset is a group of images .jpg and .png of aerial images of cars on roads and files .txt with car bound box coordinates in the following configuration:
class, x, y, width and height.

## Selective Search
This step we will find possible images that will be used to train your model. I use a OpenCv method that use mathematical formulas to find objects inside the image.
First introduced by Uijlings et al. in their 2012 paper, Selective Search for Object Recognition, is used a lot in computer vision, object detection and deep learning.
I won't go into details about this, but if you want to learn more, go to this link: https://www.pyimagesearch.com/2020/06/29/opencv-selective-search-for-object-detection/

It go through the image and return all bounding box that it found. We use this bounding box to compare with the original bounding box (IOU, next item) and to save the founded image to train. These images can be a true image or a false image, both will be used to train.

(These bounding box are only the x and y position on image and width and height of the next x2 and y2 points.)

## IOU
Another method that uses mathematic to solve some problem. The concept of IOU (Intersection Oven Union) is simple, it return 1 is the founded bounding box image (in selective search) is on the perfectly same place the original bounding box, and 0 if not, the bound box is far from the original bound box.
The results vary between 0 and 1, depending on the predicted bounding box position.
We set a threshold value to determine if is a true image or if it is a false image class, in this case if is a car or not.
After we know the class image, we save this piece of image using the bounding box to train the model. Now we know why save true and not true images, to the model can learn with all possibilities.

<IMAGE>

## Training
Before to init the training we need to configure the model. I can setup a model from scratch, but my machine is not so powerful, and the training process is to take a long time, than I decide to use a pre-trained model, that is the VGG16.

### VGG16
Is a famous object recognition model that achieves 92.7% top 5 test accuracy in the ImageNet, which is a dataset of over 14 million images belonging to 1000 classes.
(https://neurohive.io/en/popular-networks/vgg16/)

<image>

The model has as default an input of 224x244 and an output of 2 nodes, car or not car.

## Training setup
I use the ImageGenerator with "horizontal_flip=True", "vertical_flip=True", and "rotation_range=90", to generate more images for training.
The "fit" method uses as "steps_per_epoch=20", "epochs=300", and "validation_steps=2".

## Training Results
The execution time was: <EXECUTION TIME>

<Accuracy plots>

## Prediction Results
![alt text](https://github.com/IvaStival/DataScience/blob/208a4f761f9d1b6817fd87715438706e59e6322c/CarsRecognition/images/pred1.jpg?raw=true)
![alt text](https://github.com/IvaStival/DataScience/blob/208a4f761f9d1b6817fd87715438706e59e6322c/CarsRecognition/images/pred2.jpg?raw=true)
![alt text](https://github.com/IvaStival/DataScience/blob/208a4f761f9d1b6817fd87715438706e59e6322c/CarsRecognition/images/pred3.jpg?raw=true)
![alt text](https://github.com/IvaStival/DataScience/blob/edc0a32ffab42a1b0a24d0b06fcfd80fe0ec8250/CarsRecognition/images/pred4.JPG?raw=true)

## Conclusion
As we can see the model found several cars, but return wrong results as cars.
The conclusion is that this problem is difficult because of some environment similarities with cars. A idea is to use modern methods as YOLO to see if it can resolve this problems and improve the results, and increasing the dataset size so the model can have more sample to learn from.
