# Przykład użycia filtrów krawędziowych do rozpoznawania obiektów ...

# import wymaganych bibliotek

import cv2 as cv # pip install opencv-python
from matplotlib import pyplot as pl
import numpy as np
import math

import os

# Normalizacja obrazu (resize 512x512)
# Wejście: obraz w postaci tablicy numpy
# Wyjście: znormalizowany obraz jako tablica umpy

def Normalize(img, destSize = 512, threshold = 127):
    ret = cv.resize(img, (destSize, destSize))
    ret = cv.cvtColor(ret, cv.COLOR_BGR2GRAY)
    _, ret = cv.threshold(ret, threshold, 255, cv.THRESH_BINARY)    
    ret = cv.bitwise_not(ret)
    return ret

#  Wyświetlanie list obrazów 

def PlotImageList(imgList, limit=2, titles = [], figsize=(8, 8)):
    if not isinstance(imgList, list):
        raise ValueError("Input is not a list.")
    if not imgList:
        raise ValueError("List is empty.")
    
    nCount = len(imgList)
    h = min(nCount, limit) 
    v = math.ceil(nCount / limit)
    
    _, axes = pl.subplots(v, h, figsize=figsize)
    axes = axes.flatten() if nCount > 1 else [axes]  

    for i, ax in enumerate(axes):
        if i < nCount:
            ax.imshow(cv.cvtColor(imgList[i], cv.COLOR_BGR2RGB))
            if i < len(titles): ax.set_title(titles[i])
            ax.axis('on')
        else:
            ax.axis('off')  

    pl.tight_layout()
    pl.show()



# Ładowanie obrazów z określonej lokalizacji

def ListImages(path, extensions =  ['.jpg', '.jpeg', '.png', '.bmp']):
    ret = []
    for file_name in os.listdir(path):
        if os.path.splitext(file_name)[1].lower() in extensions:
            ret.append(file_name)            
    return ret


# Zastosowanie filtrów

def Filtering(imgList, filterList):
    filtered = []
    vals = []
    for train in imgList:
        ref = Normalize(train)
        refVal = ref.sum() / 255
        filtered.append(ref)
        vals.append(refVal)
        for filter in filterList:
            fimg = cv.filter2D(src = ref, ddepth = -1, kernel=filter)
            filtered.append(fimg)
            vals.append(f"{(fimg.sum() / 255 / refVal):.5}") 

    return filtered, vals


# Średnia wariancja dla danych z wszystkich pomiarów klasy
# wyrzucanie co 5 elementu - oryginalny obraz a nie przefiltrowany

def MeanVar(vals, nFilters = 4):
    vals = [float(v) for i, v in enumerate(vals) if i % (nFilters + 1) != 0]
    matrix = np.reshape(vals, (-1, 4))
    vars = [row.var() for row in matrix]
    return np.mean(vars)




# zmiana domyślnej lokalizacji na bieżący katalog

os.chdir(os.path.dirname(os.path.abspath(__file__)))

path = "train_xo"

imageFiles = ListImages(path)


train_k = [cv.imread(f"{path}/{file}") for file in imageFiles if file.startswith('k')]
train_o = [cv.imread(f"{path}/{file}") for file in imageFiles if file.startswith('o')]


# PlotImageList(train_k)
# PlotImageList(train_o)

# Przygotowanie filtrów krawędziowych

filters = [np.array([[1,  0, -1],
                     [1,  0, -1],
                     [1,  0, -1]]),
           np.array([[1,  1,  0],
                     [1,  0, -1],
                     [0, -1, -1]]),
           np.array([[1,  1,  1],
                     [0,  0,  0],
                     [-1, -1, -1]]),
           np.array([[0, -1, -1],
                     [1,  0, -1],
                     [1,  1,  0]])]



filtered_k, vals_k = Filtering(train_k, filters)
filtered_o, vals_o = Filtering(train_o, filters)


PlotImageList(filtered_k, 5, vals_k)
PlotImageList(filtered_o, 5, vals_o)


print(f"Średnia wariancja dla krzyżyków wynosi: {MeanVar(vals_k):.3}")
print(f"Średnia wariancja dla okręgów wynosi: {MeanVar(vals_o):.3}")


