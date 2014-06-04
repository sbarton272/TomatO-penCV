from cv2.cv import *

img = LoadImage("/path/to/the/testimage.jpeg")
NamedWindow("opencv")
ShowImage("opencv",img)
WaitKey(0)
