#!/usr/bin/python3
"""Buckets base class."""


class Buckets:
    """Buckets base class."""

    def __init__(self, x, y):
        """Init Buckets collide rec."""
        self.x = x
        self.y = y
        self.l = 200
        self.w = 200
        self.rect = Rect(self.x, self.y, self.l, self.w)

    def randompos(self):
        self.x = randint(-15,9500)
        self.rect = Rect(self.x,self.y,200,206)

    def draw(self,shipx):
        if shipx >=-10:
            screen.blit(bucket,(self.x-shipx,self.y))
        if shipx <= -10:
            screen.blit(bucket,(self.x,self.y))
    def point(self,shipx):
        if shipx >=-10:
            if 424 < self.x -shipx - 600:
                screen.blit(rightarrow,(600,300))
            if 424 > self.x - shipx + 600:
                screen.blit(leftarrow,(0,300))
        if shipx <-10:
            if shipx < self.x -600:
                screen.blit(rightarrow,(600,300))
            if shipx > self.x +600:
                screen.blit(leftarrow,(0,300))