#import numpy as np
import pywt as pywt
from timeflux.core.node import Node


class Dwt(Node):
    def __init__(self, levels=1, funct='db4'):
     
        self._levels = levels
        self._funct= funct
        #self._start = None
     
    def update(self):
        #timestamp = now()
        #float = time_to_float(timestamp)
        # if self._start is None:
        #     self._start = float
        if not self.i.ready():
            return
        cA, cD = pywt.dwt(self.i.data, self._funct,self._levels)
        self.o.data = cA
