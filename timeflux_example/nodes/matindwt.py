import numpy as np
import pywt as pywt
from timeflux.core.node import Node


class Dwt(Node):
    
 def __init__(self, levels= 1, funct='db4'):
     
     self._levels = levels
     self._funct= funct
     self._start = None
def update(self):
        timestamp = now()
        float = time_to_float(timestamp)
        if self._start is None:
            self._start = float
        self.o= pywt.dwt(self.i, mode='symmetric', self._funct,self._levels)
