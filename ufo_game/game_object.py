#!/usr/bin/python3
"""GameObject base class."""

from pygame import Rect, screen


class GameObject(object):
    """GameObject base class."""

    def __init__(self, x, y, l, w, ufo_game):
        """Init GameObject collide rec and imageset."""
        self.rect = Rect(x, y, l, w)
        self.sprite_obj = 

    def draw(self, main_player_x_pos):
        """Draw gameobject on screen relative to main_player_x_pos."""
            screen.blit(bucket, (self.x, self.y))