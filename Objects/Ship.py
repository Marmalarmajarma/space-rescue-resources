from GameFrame import RoomObject, Globals
import pygame

class Ship(RoomObject):
    """
    A class for the player's avitar (the Ship)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Ship object
        """
        RoomObject.__init__(self, room, x, y)
        image = self.load_image("Ship.png")
        self.set_image(image,100,100)
        self.handle_key_events = True
        
    def key_pressed(self, key):
                
        if key[pygame.K_w]:
            self.y_speed -= 10
        elif key[pygame.K_s]:
            self.y_speed += 10

    def keep_in_room(self):

        if self.y < 0:
            self.y = 0

        elif self.y + self.height> Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height

    def step(self):
        self.keep_in_room()