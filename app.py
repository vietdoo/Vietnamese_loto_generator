from random import randint
from time import sleep
import random
import cv2
import numpy as np

def get_st (a, b) :
    s = ""
    a = np.random.permutation(a)
    b = np.random.permutation(b)
    if (len(a) < len(b)) :
        for i in range (len(a)) :
            s += b[i] * '0'
            s += a[i] * '1'
        s += b[len(a)] * '0' 
    if (len(a) > len(b)) :
        for i in range (len(b)) :
            s += a[i] * '1'
            s += b[i] * '0'
        s += a[len(b)] * '1'
    if (len(a) == len(b)) :
        rr = randint(1,2)
        if (rr == 2) :
            for i in range (len(b)) :
                s += a[i] * '1'
                s += b[i] * '0'
        else :
            for i in range (len(b)) :
                s += b[i] * '0'
                s += a[i] * '1'
    return s   

def make_cell (number, color) :
    img = np.zeros((cell_y, cell_x, 3), np.uint8)
    img[:] = color
    if (len(number) == 1) :
        loca = (15, 45) 
    else :
        loca = (2, 45)
    blank = np.zeros((60, 60, 3), np.uint8)
    blank[:] = color
    cv2.putText(blank, number, loca, cv2.FONT_HERSHEY_TRIPLEX, 1.4, (0), 3)
    img = cv2.resize(blank, (cell_x, cell_y))
    cv2.line(img, (0, 0), (0, cell_y), (0, 0, 0), thick_cell)
    cv2.line(img, (0, 0), (cell_x, 0), (0, 0, 0), thick_cell)
    cv2.line(img, (0, cell_y - 1), (cell_x - 1, cell_y - 1), (0, 0, 0), thick_cell)
    cv2.line(img, (cell_x - 1, 0), (cell_x - 1, cell_y - 1), (0, 0, 0), thick_cell)
    return img

def make_loto (cl, id) :
    n = 98
    loto = np.zeros((loto_y + 120, loto_x, 3), np.uint8)
    loto[:] = (255, 255, 255)

    loto[0:100, 0:540] = yt
    loto[10:90,10:90] = logo

    loto[0 + cell_y * 10:120 + cell_y * 10,0:540] = head
    cv2.putText(loto,(4 - len(str(id))) * '0' + str(id), (410, 105 + cell_y * 10),cv2.FONT_HERSHEY_COMPLEX , 1.4, (216, 132, 116), 2)
    for i in range (0, 9) :
        r = randint(1,3)
        if (r == 1) :
            st = get_st (a2, b2[randint(0,len(b2)- 1)])
        else :
            st = get_st (a1, b1[randint(0,len(b1) -1)])
        for j in range (0, 9) :
            if (st[j] == '1') :
                color = (255, 255, 255)
                number = str(j * 10 + a[j][i])
            else :
                number = ""
                color = cl
                
            loto[i * cell_y + 100:(i + 1) * cell_y + 100, j * cell_x:(j + 1) * cell_x] = make_cell(number, color)
    cv2.line(loto, (0, 100), (0, loto_y + 120), (0, 0, 0), thick_cell * 2)
    cv2.line(loto, (0, 100), (loto_x, 100), (0, 0, 0), thick_cell * 2)
    cv2.line(loto, (0, loto_y + 120 - 1), (loto_x - 1, loto_y + 120 - 1), (0, 0, 0), thick_cell * 2)
    cv2.line(loto, (loto_x - 1, 100), (loto_x - 1, loto_y + 120 - 1), (0, 0, 0), thick_cell * 2)
    return loto
    
colors = [(216,167,76), (0, 150, 0), (0, 0, 255), 
(250, 0, 255), (0, 255, 250), (0, 190, 100), (168, 179, 255),
(216,169,222), (168, 179, 186)]

a = []
a1 = [2,2,1] 
b1 = [[1,1,1,1], [1,1,2], [1,3], [1,1,1,1], [1,1,2], [1,1,2], [1,1,1,1], [1,1,2]]
a2 = [1,1,1,2]
b2 = [[1,1,2],[1,1,1,1], [1,1,2]]

cell_y = 90
cell_x = 60
thick_cell = 2

loto_x = cell_x * 9
loto_y = cell_y * 10
#path = "E:/"

yt = cv2.imread("/content/drive/MyDrive/loto/yt.JPG")
yt = cv2.resize(yt, (540, 100))
head = cv2.imread("/content/drive/MyDrive/loto/head.jpg")
head = cv2.resize(head, (540, 120))
logo = cv2.imread("/content/drive/MyDrive/loto/LOGO.jpg")
logo = cv2.resize(logo, (80, 80))

def progess (n) :
    for i in range (1, n + 1) :
        a.clear()
        a.append(random.sample(range(1,10),9))
        for j in range (0, 7) :
            a.append(random.sample(range(0,10),10))
        a.append(random.sample(range(0,11),11))
        loto = make_loto(colors[randint(0, len(colors) - 1)], i)
        cv2.imwrite("/content/drive/MyDrive/Final_Loto/Loto_" + (4 - len(str(i))) * '0' + str(i) + ".jpg", loto)
        cv2.waitKey(1)

progess(1000)
cv2.waitKey(1)
cv2.destroyAllWindows()
