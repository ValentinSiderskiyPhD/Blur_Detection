import cv2

Threshold=100 #notime


#images and threshold for how blurry is really blurry
#sepereate main function?
def variance_of_laplacian(image):
    path = r'C:\Users\prashanthi\GitHub\Blur_Detection\Capture.png' #notime
    image = cv2.imread(path)
    #put checkpoint for finding time after this and after image is outputted
        #make constants start w/ capital(use pylint to make sure)

        #might need to change, put in beginning of code/before function
        #converts to gray
        #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #let erin handle this?? **
        #variance of laplacian
#bluriness = cv2.Laplacian(gray, cv2.CV_64F).var()#second partial derivative of x/y direction
#replacement for .var()?
#make image smaller? crop image to just the pupil/ approximately
#CONTOURS= SLOW.
#resize+make threshold lower or crop out (u can control during data collectio)
#code that finds estimated circles???
    bluriness = cv2.Laplacian(gray, cv2.CV_64F).var()
    text = "Not Blurry"
        # if the focus measure is less than the supplied threshold,
        # then the image should be considered "blurry"
    if bluriness < Threshold:
        text = "Blurry"
    #output number + boolean

                # show the image
#put text on after this function (return the stuff)
    cv2.putText(gray, "{}: {:.2f}".format(text, bluriness), (10, 30),
    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
        cv2.imshow("Image", gray)
        key = cv2.waitKey(0)
        return bluriness
        #`how long does this take to do
