# SelfDraiving_FindingLane
in this prj we will find and detect the lane and we are able to find the area that the car should be in 

# Download Video 
you have to download the video blow and put it in the folder of prj in your system 

the name of video must be : test2.mp4

(https://file.io/1Vl6PKHVysjO)

# Video test 
 ![](https://github.com/mohammadst99/SelfDraiving_FindingLane/blob/main/test.gif)
 
 
 # Code Explain
first we need to add our video or camera with cv2

then we need to apply filter ( gray , blur , canny) so that we can find the contours

then we need apply a mask to just get the area that we need and it is more likely to be lane here . for example in this video we put a triangle with these polyIndex "(200,height),(1100,height),(550,250)" and we use the bitwise(AND) to apply this triangel mask 

then we use cv2.HoughLinesP to find the lines in our image 

then in order to crash and having continuously lane we need to apply average method 

we know that each line is " Y = mX + b " so we need the 'm' and 'b' parameter

we know thet right side line is like '/' and the m is posetive and in the left side we have negative m so we can seprate them to two diffrent list

then we need to average our 'm' and 'b' in each line

and finally we can draw the line in the image
