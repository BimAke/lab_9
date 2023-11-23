import pygame
import sys
import time
from datetime import datetime
pygame.init()
window_size = (400, 400)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Mickey's Clock")
mickey_image = pygame.image.load("mickey.png") 
mickey_rect.center = (window_size[0] // 2, window_size[1] // 2)  
def rotate_mickey():
    current_time = datetime.now().time()
    minutes_angle = (current_time.minute / 60) * 360
    seconds_angle = (current_time.second / 60) * 360

    rotated_minutes = pygame.transform.rotate(mickey_image, -minutes_angle)
    rotated_seconds = pygame.transform.rotate(mickey_image, -seconds_angle)

    minutes_rect = rotated_minutes.get_rect(center=mickey_rect.center)
    seconds_rect = rotated_seconds.get_rect(center=mickey_rect.center)

    return rotated_minutes, minutes_rect, rotated_seconds, seconds_rect
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((255, 255, 255))  # Clear the window

    rotated_minutes, minutes_rect, rotated_seconds, seconds_rect = rotate_mickey()

    window.blit(rotated_minutes, minutes_rect)
    window.blit(rotated_seconds, seconds_rect)

    pygame.display.update()
    time.sleep(1) 

#2
import pygame
import sys   
pygame.init()
window_size = (400, 400)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Music Player")
music_files = ["song1.mp3", "song2.mp3", "song3.mp3"] 
current_song_index = 0
is_playing = False
def play_song():
    pygame.mixer.music.load(music_files[current_song_index])
    pygame.mixer.music.play()
    while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_playing:
                    pygame.mixer.music.pause()
                    is_playing = False
                else:
                    pygame.mixer.music.unpause()
                    is_playing = True
            elif event.key == pygame.K_RIGHT:
                current_song_index = (current_song_index + 1) % len(music_files)
                play_song()
            elif event.key == pygame.K_LEFT:
                current_song_index = (current_song_index - 1) % len(music_files)
                play_song()

    window.fill((255, 255, 255))  
    pygame.display.update()
#4
import pygame
import sys
pygame.init()
window_size = (400, 400)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Moving Ball")
ball_radius = 25
ball_position = [window_size[0] // 2, window_size[1] // 2]
hile True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_position[1] -= 20
            elif event.key == pygame.K_DOWN:
                ball_position[1] += 20
            elif event.key == pygame.K_LEFT:
                ball_position[0] -= 20
            elif event.key == pygame.K_RIGHT:
                ball_position[0] += 20
    if ball_position[0] < ball_radius:
        ball_position[0] = ball_radius
    elif ball_position[0] > window_size[0] - ball_radius:
        ball_position[0] = window_size[0] - ball_radius
    if ball_position[1] < ball_radius:
        ball_position[1] = ball_radius
    elif ball_position[1] > window_size[1] - ball_radius:
        ball_position[1] = window_size[1] - ball_radius

    window.fill((255, 255, 255))  
    pygame.draw.circle(window, (255, 0, 0), ball_position, ball_radius) 
    pygame.display.update()