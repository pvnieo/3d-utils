# 3p
import numpy as np


def compute_triagle_area(pt1, pt2, pt3):
    a = np.linalg.norm(pt1 - pt2)
    b = np.linalg.norm(pt1 - pt3)
    c = np.linalg.norm(pt3 - pt2)
    s = (a + b + c) / 2
    area = np.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
