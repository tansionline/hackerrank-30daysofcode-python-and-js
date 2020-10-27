#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):

  
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())

    tip = meal_cost * tip_percent / 100
    
    tax = meal_cost * tax_percent / 100
    
    totalCost = int(round(meal_cost + tip + tax))
    
 
    return str(totalCost)
    solve(meal_cost, tip_percent, tax_percent)

print(solve(meal_cost=1, tip_percent= 1, tax_percent=1))
    

