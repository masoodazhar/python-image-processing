# python-image-process
its an image process. in python

first importing cv2. installed from (  pip install opencv-python ) command
2) created a class with constructor which take a parameter as imagePath
3) image will be read by cv2.imread(imagePath)
4)resizing the image size as 300x300
    and creating a circle of (250x250)
    and creating a rectangle of (50x50) 
    at the end showing the image    using cv2.imshow("frame name", image)
5) last waiting for a key pressed by user then destroy all windows and frames
