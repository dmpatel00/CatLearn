import numpy as np
from .constant import Prior_constant

class Prior_first(Prior_constant):
    def __init__(self,yp=0.0,add=0.0,**kwargs):
        "The prior uses a baseline of the target values if given else it is at 0"
        Prior_constant.__init__(self,yp,add,**kwargs)
    
    def update(self,X,Y):
        "The prior will use the first of the target values"
        self.dim=len(Y[0])
        self.yp=Y.item(0)+self.add
        return self.yp
