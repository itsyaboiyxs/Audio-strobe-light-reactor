import pygame
import sounddevice as sd
import numpy as np
import threading
from scipy.signal import butter, lfilter
import random
import time
import hashlib 


ACTUAL_DISPLAY_TEXT = "yxs wrldwde™"


SECURE_TEXT_HASH = "a1d3448ed44b3444a223d6b167b1a92a7d9f8461b24c6e0e0948e7db6520c318"

def verify_text_integrity():
    """
    Verifies the integrity of the display text.
    Calculates the SHA256 hash of ACTUAL_DISPLAY_TEXT and compares it
    to the predefined SECURE_TEXT_HASH. If they do not match,
    the program prints an error and exits.
    """
    
    current_text_bytes = ACTUAL_DISPLAY_TEXT.encode('utf-8')
    
    current_hash = hashlib.sha256(current_text_bytes).hexdigest()

    
    if current_hash != SECURE_TEXT_HASH:
        print("--------------------------------------------------")
        print("!!! INTEGRITY CHECK FAILED: Display text has been altered. !!!")
        print("!!! The program will now exit to maintain integrity. !!!")
        print("--------------------------------------------------")
        pygame.quit()
        exit()        


pygame.init()
screen_width, screen_height = 1366, 786
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Strobe reactor jon")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Horizon", 48, bold=True)


sample_rate = 44100
block_size = 1024


min_delay = 0.00001
max_delay = 0.1
silent_threshold = 0.01
strobe_threshold = 0.55
text_threshold = 0.9
color_strobe_threshold = 0.95

color_choices = ["red", "blue", "green", "yellow", "purple", "cyan", "orange", "pink"]


current_delay = max_delay
current_brightness = 0
show_text = False
show_color_flash = False
running = True

def butter_lowpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order)
    return lfilter(b, a, data)

def audio_callback(indata, frames, time_info, status):
    global current_delay, current_brightness, show_text, show_color_flash

    if status:
        print(status)

    bass_data = butter_lowpass_filter(indata[:, 0], cutoff=200, fs=sample_rate)
    volume_norm = float(np.linalg.norm(bass_data)) / 10
    volume_norm = min(volume_norm, 1)

    if volume_norm < silent_threshold:
        current_brightness = 0
        current_delay = max_delay
        show_text = False
        show_color_flash = False 

    elif volume_norm < strobe_threshold:
        current_brightness = int(255 * (volume_norm / strobe_threshold))
        current_delay = max_delay - (volume_norm * (max_delay - min_delay))
        show_text = False
        show_color_flash = False

    else:
        current_brightness = 255
        current_delay = max_delay - (volume_norm * (max_delay - min_delay))
        
    show_text = volume_norm >= text_threshold
    show_color_flash = volume_norm >= color_strobe_threshold


def strobe_loop():
    global running


    verify_text_integrity()
    

    flash_white = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

       
        if current_brightness == 0:
            color = (0, 0, 0)

        elif current_brightness < 255:
            color = (current_brightness, current_brightness, current_brightness)

        else:
            if show_color_flash and random.random() < 0.3:
                color = pygame.Color(random.choice(color_choices))
            else:
                color = (255, 255, 255) if flash_white else (0, 0, 0)
                flash_white = not flash_white

        screen.fill(color)

        
        if show_text:
            text_color = (0, 0, 0) if color == (255, 255, 255) else (255, 255, 255)
            
            text_surface = font.render(ACTUAL_DISPLAY_TEXT, True, text_color)
            
            text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(text_surface, text_rect)

        pygame.display.flip()
        time.sleep(current_delay)


try:
    with sd.InputStream(callback=audio_callback, samplerate=sample_rate, blocksize=block_size, channels=1, device=3):
        print("Listening... Press the window's close button to exit.")
        strobe_loop()
except Exception as e:
    print(f"An error occurred with the audio stream: {e}")
    print("Please ensure your audio input device is correctly configured and available.")
finally:
    pygame.quit()
    print("Program exited.")
