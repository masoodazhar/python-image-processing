import cv2 #''' importing opencv '''

class ImageProccess():
    
    #contructor method take an argument for image path like.
    # while creating object of ImageProccess('image.jpg')
    def __init__(self, imgageUrl):
        #reading the image from current folder
        img = cv2.imread(imgageUrl) 

        #resizing the image and replacing (img) variable
        img = cv2.resize(img, (300,300))  
   
        # creating rectangle in img and replacing img again
        img = cv2.circle(img,(150,150),100, (0,0,255),3) 
       
        # creating circle on image and replacing img again
        img = cv2.rectangle(img, (0,300), (300, 250),(0,0,255),-1 ) 

        # showing the img in frame named (image)
        cv2.imshow("image", img) 

        # the frame wait until user press any key
        cv2.waitKey(0)     

        #destroying AllWindows and frames after pressing any key     
        cv2.destroyAllWindows()  


object = ImageProccess('b.jpg')
