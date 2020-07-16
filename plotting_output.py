import xlrd
import xlwt
from xlutils.copy import copy
import math
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import pure_code
from pure_code import *

femur = 15
tibia = 15.5
hip = 0

a1 = 0  # length of link a1 in cm
a2 = 15  # length of link a2 in cm
a3 = 0  # length of link a3 in cm
a4 = 15.5  # length of link a4 in cm

list3 = []
list4 = []


def forwardK(theta_1, theta_2):
    # print(theta_1)  # theta 1 angle in degrees
    # print(theta_2)  # theta 2 angle in degrees

    theta_1 = (theta_1/180)*pi  # theta 1 in radians
    theta_2 = (theta_2/180)*pi  # theta 2 in radians

    R0_1 = [[cos(theta_1), -sin(theta_1), 0],
            [sin(theta_1), cos(theta_1), 0],
            [0, 0, 1]]

    R1_2 = [[cos(theta_2), -sin(theta_2), 0],
            [sin(theta_2), cos(theta_2), 0],
            [0, 0, 1]]

    R0_2 = dot(R0_1, R1_2)  # dot product

    # Displacement vectors
    d0_1 = [[a2*cos(theta_1)], [a2*sin(theta_1)], [a1]]
    d1_2 = [[a4*cos(theta_2)], [a4*sin(theta_2)], [a3]]

    # Homogeneous transformation matrix from Joint 0 to 1
    H0_1 = concatenate((R0_1, d0_1), 1)  # 1 appends to the right
    H0_1 = concatenate((H0_1, [[0, 0, 0, 1]]), 0)  # 0 appends to the bottom

    # print(matrix(H0_1))
    # print('\n')

    # Homogeneous transformation matrix from Joint 1 to 2
    H1_2 = concatenate((R1_2, d1_2), 1)  # 1 appends to the right
    H1_2 = concatenate((H1_2, [[0, 0, 0, 1]]), 0)  # 0 appends to the bottom

    # Homogeneous transformation matrix from Joint 1 to 2
    H0_2 = dot(H0_1, H1_2)
    print(H0_2[0, 3], H0_2[1, 3])  # final coordinates
    list3.append(H0_2[0, 3])
    list4.append(H0_2[1, 3])
    #print(H0_2[1, 3])


# range is defined as the number of rows generated in trotPoints.py
for x in range(len(list1)):
    forwardK(float(((list1[x]*150)/512)-60),  # the calculations are done to convert dynamixel write to degrees
             float(((list2[x]*150)/512)-60))

# wb.save("C:/Users/sachi/Documents/Arduino/U2D2/dxl_control-master/saved.xlsx")
# print(matrix(H0_2))
#print(H0_2[0, 3])
plt.plot(list3, list4)
plt.show()
