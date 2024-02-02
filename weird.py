#!/bin/python3

import math
import os
import random
import re
import sys

def weirdness(number):
    if number%2 != 0:
        return "Weird"
    else:
        if 2 <= number <= 5:
             return "Not Weird" 
        elif 6 <= number <= 20:
             return "Weird"
        else:
             return "Not Weird"    
             
             
        
        

if __name__ == '__main__':
    n = int(input().strip())
    print(weirdness(n))
