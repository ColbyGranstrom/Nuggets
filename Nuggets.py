# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:35:09 2016

@author: colbygranstrom
"""
candidate = 0
in_a_row = 0
Largest = 0
def ismynug(candidate):
    for i in range (0,candidate):
        for j in range (0,candidate):
            for k in range (0,candidate):
                if (i*6 + j*9 + k*20) == candidate:
                    return True
    return False
while in_a_row < 7:
    if ismynug (candidate) == True:
        in_a_row += 1
    if ismynug (candidate) == False:
        Largest = candidate
        in_a_row = 0
    candidate += 1
    
print ("The largest number you cannot purchase is", Largest)







    