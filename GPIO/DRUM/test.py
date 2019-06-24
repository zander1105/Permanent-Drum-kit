import pygame 
import time
pygame.mixer.init()
uu = input()
pygame.mixer.music.load("/root/GPIO/DRUM/sounds/drum1.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy()  == True:
	time.sleep(.04)

