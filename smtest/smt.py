import time, audioop
import pygame
import pyaudio
import wave
#test is hell
# Initialisation for PyAudio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
# Object
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

# PyGame initialisations and basic objects
pygame.init()
screensize = (900, 600)
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Shout harder.. :D")

# Defining colors
WHITE = (255, 255, 255)
RED = (255, 128, 128)
YELLOW = (255, 255, 128)
BLUE = (0, 0, 255)

# Loop till close button clicked
done = False
clock = pygame.time.Clock()

# variables
score = []
width = 0.8

margin = 20
samples_per_section = screensize[0] / 3 - 2 * margin



sound_tracks = (float)[[0] * samples_per_section] * 3

max_value = [0] * 3

current_section = 0
while not done:

    # Limits CPU usage to max 10 times per second
    # Not required here because already the for loop takes averages over some time
    # clock.tick(10)

    total = 0
    # Now we read data from device for around one second
    for i in range(0, 2):
        # l,data = inp.read()
        data = stream.read(CHUNK)
        # oreo_sound.append(data)
        if True:
            reading = audioop.max(data, 2)
            total = total + reading
        time.sleep(.0001)

    # any scaling factor
    total = total / 100

    sound_tracks[current_section] = sound_tracks[current_section][1:] + [total]
    max_value[current_section] = max(max_value[current_section], total)

    screen.fill(WHITE)

    # draw highlighted section
    pygame.draw.rect(screen, YELLOW, (screensize[0] / 3 * current_section, 0, screensize[0] / 3, screensize[1]))

    for i in range(3):
        sectionx = i * screensize[0] / 3 + margin
        # add meet wala last year ka feature
        pygame.draw.rect(screen, RED,
                         (sectionx, screensize[1] - max_value[i], screensize[0] / 3 - 2 * margin, max_value[i]))

        for j in range(0, screensize[0] / 3 - 2 * margin):
            x = j + sectionx
            y = screensize[1] - sound_tracks[i][j]
            pygame.draw.rect(screen, BLUE, (x, y, 1, sound_tracks[i][j]))

    # frame flip must happen after all drawing commands
    pygame.display.flip()

    # Set close button event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                # right button pressed, clear all arrays
                sound_tracks = [[0] * samples_per_section] * 3
                max_value = [0] * 3
                current_section = 0
            else:
                pos = pygame.mouse.get_pos()
                current_section = (pos[0] * 3) / screensize[0]
                print
                pos, current_section

# clearing the resources
pygame.quit()
stream.stop_stream()
stream.close()
p.terminate()
pygame.quit()