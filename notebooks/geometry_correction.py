import numpy as np


def homogeneous_correction_factor(x=0, radius=-1):
    if np.abs(x)>radius:
        return 0
    rp = 2*radius*np.sin(np.arccos(x/radius))
    if x == 0:
        return 1
    return (2*radius)/rp
