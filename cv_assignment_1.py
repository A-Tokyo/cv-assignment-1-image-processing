import cv2
import numpy as np

guc = cv2.imread("inputs/GUC.png",0)
for i in range (len(guc)):
    for j in range (len(guc[i])):
        if (guc[i][j]<40):
            guc[i][j]=0
        else:
            guc[i][j]=guc[i][j]-40

cv2.imwrite("outputs/GUCNew.png", guc)


calculator = cv2.imread("inputs/calculator.png",0)
for i in range (len(calculator)):
    for j in range (len(calculator[i])):
        if (calculator[i][j]>130):
            calculator[i][j]=130

cv2.imwrite("outputs/calculatorNew.png", calculator)


cameraman = cv2.imread("inputs/cameraman.png",0)
for i in range (len(cameraman)):
    for j in range (len(cameraman[i])):
        if (cameraman[i][j]<70):
            cameraman[i][j]=cameraman[i][j]*2

cv2.imwrite("outputs/cameramanNew.png", cameraman)


lake = cv2.imread("inputs/lake.png",0)
lake_replacement = np.zeros((len(lake),len(lake[0]),1),np.int8)
for i in range (len(lake)):
    for j in range (len(lake[i])):
        avg=0
        if i==0 or j==0 or i==len(lake)-1 or j==len(lake[i])-1:
            continue
        avg=avg+(int(lake[i][j])+int(lake[i][j]))+(int(lake[i+1][j])+int(lake[i-1][j]))+(int(lake[i][j+1])+int(lake[i][j-1]))
        avg=avg/9.0
        avg2=(lake[i][j]-avg)**2
        if avg2<800:
            lake_replacement[i][j]=0
        else:
            lake_replacement[i][j]=lake[i][j]

cv2.imwrite("outputs/lakeNew.png", lake_replacement)


james = cv2.imread("inputs/james.png",0)
london1 = cv2.imread("inputs/london1.png",0)
london2 = cv2.imread("inputs/london2.png",0)

for i in range (len(james)):
    for j in range (len(james[i])):
        if (james[i][j]<200):
            london1[i][j-180]=james[i][j]

cv2.imwrite("outputs/jamesNew1.png", london1)
img= np.flip(james,1)
for i in range (len(img)):
    for j in range (len(img[i])):
        if (img[i][j]<200):
            london2[i][j]=img[i][j]

cv2.imwrite("outputs/jamesNew2.png", london2)
