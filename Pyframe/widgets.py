from pygame import gfxdraw
import math
import pygame as pg


class Circle:
    def __init__(self, screen, centre_x, centre_y, rad, color, update=False) -> None:
        self.screen = screen
        # Drawing circle outline with antialiasing
        gfxdraw.aacircle(self.screen, centre_x, centre_y, rad, color)
        # Filling in the circle
        gfxdraw.filled_circle(self.screen, centre_x, centre_y, rad, color)

        if update:
            pg.display.update(pg.Rect(centre_x - rad - 2, centre_y - rad - 2, 2 * rad + 4, 2 * rad + 4))

        self.centre_x = centre_x
        self.centre_y = centre_y
        self.rad = rad

    def circle_dist(self, mouse_pos):  # Returns True is the cursor is inside the circle
        x_pos = mouse_pos[0] - self.centre_x
        y_pos = mouse_pos[1] - self.centre_y
        # Finding the distance of the cursor from the centre off the circle
        dist = math.sqrt(math.pow(x_pos, 2) + math.pow(y_pos, 2))
        if dist <= self.rad:
            return True
        return False


class Rect:
    def __init__(self, screen, top_x, top_y, width, height, color='white', update=True) -> None:
        self.screen = screen
        self.top_x = top_x
        self.top_y = top_y
        self.width = width
        self.height = height
        # Drawing the rectangle to the screen
        pg.draw.rect(screen, color, pg.Rect(self.top_x, self.top_y,
                                            self.width, self.height))
        if update:  # Updating the screen to show the rectangle
            pg.display.update(pg.Rect(self.top_x, self.top_y,
                                      self.width, self.height))

    def rect_dist(self, mouse_pos):  # Returns True is the cursor is inside the rectangle
        if self.top_x <= mouse_pos[0] <= self.top_x + self.width:
            if self.top_y <= mouse_pos[1] <= self.top_y + self.height:
                return True
        return False
