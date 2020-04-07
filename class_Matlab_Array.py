# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 09:20:55 2020

@author: ZhanLF
"""
import numpy as np

class MatlabArray(object):
    def __init__(self, nparray):
        self._array = np.array(nparray)
    def __setitem__(self, index, value):
        iy, ix = index
        previous_array = self._array
        piy, pix = self._array.shape
        if (iy+1 > piy) or (ix+1 > pix):
            niy = (iy+1 if iy+1 > piy else piy)
            nix = (ix+1 if ix+1 > pix else pix)
            self._array = np.full((niy, nix), np.nan)
        
        self._array[iy][ix] = value
        self._array[:piy,:pix] = previous_array
    def __getitem__(self, index):
        return self._array[index]

# ------------test---------------
arr = MatlabArray(np.array([[1,2],[3,4]]))
arr[4,5] = 88
print(arr[:])
