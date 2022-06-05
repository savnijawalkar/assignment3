# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 13:15:33 2022

@author: Dell
"""

numh=int(input("enter the numberof hydrogen:"))
numc=int(input("enter the numberof carbon:"))
numo=int(input("enter the numberof oxygen:"))
molecular_weight=1.00794*numh+12.0107+15.9994*numo
print("the molecular weight of moleculenis",molecular_weight)