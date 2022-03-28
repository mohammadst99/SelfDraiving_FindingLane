import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
def Canny(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    canny = cv.Canny(blur, 50, 150)
    return canny
def make_cordination(image,line_parameters): #y=mx+b  and x = (y-b)/m
    m, b = line_parameters
    y1 = image.shape[0]
    y2 = int(y1*(3/5))
    x1 = int((y1-b)/m)
    x2 = int((y2-b)/m)
    return np.array([x1,y1,x2,y2])



def average_slope_intercept(image,lines):
    left_fit=[]
    right_fit=[]
    for line in lines :
        x1,y1,x2,y2 = line.reshape(4)
        m , b = np.polyfit((x1,x2),(y1,y2),1) # y=mx+b
        if m<0:
            left_fit.append((m,b))
        else :
            right_fit.append(((m,b)))
    left_fit_average = np.average(left_fit,axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    leftLine = make_cordination(image,left_fit_average)
    rightLine = make_cordination(image,right_fit_average)
    return np.array([leftLine,rightLine])




def region(image):
    height = image.shape[0]
    polygons = np.array([[(200,height), (1100,height),(550,250)]])
    mask = np.zeros_like(image)
    cv.fillPoly(mask,polygons,255)
    newIMAGE = cv.bitwise_and(image, mask)
    return newIMAGE

def Lines(image , lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            print(line)
            x1,y1,x2,y2 = line.reshape(4)
            cv.line(line_image,(x1,y1),(x2,y2),(0,255,0),thickness=6)
    return line_image







#image = cv.imread("test_image.jpeg")
#lane_image = image.copy()
#canny = Canny(lane_image)
#maskedImage = region(canny)
#lines  = cv.HoughLinesP(maskedImage,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5) #how much precision we need for bins? 2,1
                                                                                                #thereshould min number of intersecion you need to detect the lines
#averagedLines =average_slope_intercept(lane_image,lines)
#lineImage = Lines(lane_image,averagedLines)
#comboImage = cv.addWeighted(lane_image,0.8,lineImage,1,1)
#cv.imshow("result",maskedImage)
#cv.imshow("lines",lineImage)
#cv.imshow("linesdetect",comboImage)


##plt.imshow(canny)
##plt.show()
#cv.waitKey(0)

cap = cv.VideoCapture("test2.mp4")
while (cap.isOpened()):
    sucess,img = cap.read()
    canny = Canny(img)
    maskedImage = region(canny)
    lines = cv.HoughLinesP(maskedImage, 2, np.pi / 180, 100, np.array([]), minLineLength=40,maxLineGap=5)  # how much precision we need for bins? 2,1
                                            # thereshould min number of intersecion you need to detect the lines
    averagedLines = average_slope_intercept(img, lines)
    lineImage = Lines(img, averagedLines)
    comboImage = cv.addWeighted(img, 0.8, lineImage, 1, 1)
    cv.imshow("result", maskedImage)
    cv.imshow("lines", lineImage)
    cv.imshow("linesdetect", comboImage)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv.destroyAllWindows()