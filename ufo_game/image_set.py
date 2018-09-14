#!/usr/bin/python3
"""GameObject base class."""

from pygame import Rect, screen

class ImageSet(object):
    """GameObject base class."""

    def __init__(self, imagename, ):
        """Init GameObject collide rec and imageset."""
        self.rect = Rect(x, y, l, w)
