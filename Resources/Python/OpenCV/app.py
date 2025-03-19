import cv2 as cv # pip install opencv-python
from matplotlib import pyplot as pl
import numpy as np
<<<<<<< HEAD
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))



path = "imgs"
files = []


ext = ['.jpg', '.jpeg', '.png', '.bmp']


for file_name in os.listdir(path):
    if os.path.splitext(file_name)[1].lower() in ext:
        files.append(file_name)

k0 = np.array([[0, 0, 0],
               [0, 1, 0],
               [0, 0, 0]])

# k1 = np.array([[1, 1, 0],
#                [1,0, -1],
#                [0, -1, -1]])

k1 = np.array([[1, 1, 1, 0, 0],
               [1,0,0,0, -1],
               [1,0,0,0, -1],
               [1,0,0,0, -1],
               [0, -1, -1, -1, -1]])

k2 = np.array([[-1, -1, -1],
               [0, 0, 0],
               [1, 1, 1]])

k3 = k2.transpose()
#print (k)

kernels = [k0,k1,k2,k3]



print("Znalezione obrazy:")
for file in files:
    img = cv.imread(f"{path}/{file}")
    img = 255 - img
  
    f,s = pl.subplots(2,2,figsize=[10,10])
    s.shape = (1,4)
    i = 0
    s = s[0]

    for ax in s:
        nimg = cv.filter2D(src = img, ddepth = -1, kernel=kernels[i])
        ax.imshow(cv.cvtColor(nimg, cv.COLOR_BGR2RGB))
        ax.axis("off")
  
        i=i+1

    pl.show()
=======
print(cv.__version__)
>>>>>>> 9012e609eb9f290190bc6786cf9b97b64db5b570
