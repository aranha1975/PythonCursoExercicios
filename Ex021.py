import pygame
pygame.init()
pygame.mixer.music.load('vader.mp3')
pygame.mixer.music.play()
pygame.time.delay(50000)
pygame.event.wait()
