# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 08:34:03 2020

@author: Venkata Kolla

Requirement - Calculate Ecludeian or Manhattan Distance between two points
"""

# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass

class CoordinateNotSame(Error):
    """Raised when the input coordinate is different from coordinate1"""
    pass



#Ecludian Distance is SQRT((POINT1 - POINT2) SQUARE)
def ecludeian_distance(pt1,pt2):
    distance = 0
    for i in range(len(pt1)):
        distance += ((int(pt1[i]) - int(pt2[i]))** 2)
    return (distance ** 0.5)

#Manhattan Distance is ABSOLUTE(POINT1 - POINT2)
def manhattan_distance(pt1,pt2):
    distance = 0
    for i in range(len(pt1)):
        distance += (abs(int(pt1[i]) - int(pt2[i])))
    return distance


print("Please enter numbers with space between two Numbers. Example:1 2")

#This is to check for entered input value and if it is number
while True:
    try:
        ##co1=tuple(input("Please enter Value of 1st coordinate"))
        input_string = input("Enter a list elements separated by space ")
        print("\n")
        userList = input_string.split()
        print("user list is ", userList)
        
        sum1 = 0
        for num in userList:
            sum1 += int(num)        
    except ValueError:
        print("You may enter a string.Please enter a number for coordinate - 1")
    else:
        print("Number entered is:",userList)
        break
    
while True:
    try:
        
        input_string = input("Enter second coordinate elements separated by space ")
        print("\n")
        userList1 = input_string.split()
        print("user list is ", userList)
        
        #To check entered values are integers
        sum1 = 0
        for num in userList1:
            sum1 += int(num)
        
        #To check entered list is same length as coordinate-1
        if(len(userList) != len(userList1)):
            raise CoordinateNotSame     
        
    except ValueError:
        print("You may enter a string.Please enter a number for coordinate - 2 again")
    except CoordinateNotSame:
        print("Coordinate-2 is not same size of coordinate-1")
    else:
        print("Number entered is:",userList1)
        break


#if proper number is entered then we will calculate Ecludeian and Manhattan Distance    
print("Ecludeian distance ",userList," and ", userList1," is:" ,ecludeian_distance(userList,userList1))

print("Manhattan distance ",userList," and ", userList1," is:" ,manhattan_distance(userList,userList1))