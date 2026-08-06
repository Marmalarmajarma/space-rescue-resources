from GameFrame import RoomObject, Globals
from Objects.Laser import Laser
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

        self.can_shoot = True
        
    def key_pressed(self, key):
                
        if key[pygame.K_w]:
            self.y_speed -= 5
        elif key[pygame.K_s]:
            self.y_speed += 5

        if key[pygame.K_SPACE]:
            self.shoot_laser()

    def keep_in_room(self):

        if self.y < 0:
            self.y = Globals.SCREEN_HEIGHT - self.height

        elif self.y + self.height> Globals.SCREEN_HEIGHT:
            self.y = 0

    def step(self):
        self.keep_in_room()

    def shoot_laser(self):

        if self.can_shoot:
            new_laser = Laser(self.room, 
                            self.x + self.width, 
                            self.y + self.height/2 - 4)

            self.room.add_room_object(new_laser)
            self.can_shoot = False
            self.set_timer(10, self.reset_shot)

    def reset_shot(self):
        self.can_shoot = True