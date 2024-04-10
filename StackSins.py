"""
@authors: Matthew Mitchell

uses several sin functions to mimic random.  where each sin when above 0 tunes on a byte else keep the byte off
"""

import math


def random(seed):
    rv = 0b0000
    rv = rv | 1 if math.sin(seed) > 0 else 0
    rv = rv | (1 if math.sin(seed * 2) > 0 else 0) << 1
    rv = rv | (1 if math.sin(seed / 2) > 0 else 0) << 2
    rv = rv | (1 if math.sin(seed ** 2) > 0 else 0) << 3

    return int(rv)
