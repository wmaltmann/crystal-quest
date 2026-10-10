import os
import time
import pygame

# 1. Use KMS/DRM driver for direct monitor output without desktop GUI
os.environ["DISPLAY"] = ":0"
os.environ["SDL_VIDEODRIVER"] = "x11"

# 2. Initialize video subsystem
pygame.init()
pygame.font.init()

# 3. Initialize display surface
try:
    # Fullscreen mode automatically matches native monitor resolution
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    print("Display initialized successfully!")
    print(f"Screen Resolution: {screen.get_width()}x{screen.get_height()}")
except pygame.error as e:
    print(f"Failed to initialize display: {e}")
    exit(1)

# Hide mouse cursor
pygame.mouse.set_visible(False)

# 4. Draw test patterns across 3 screens
colors = [
    ((255, 0, 0), "RED SCREEN - Pygame Test"),
    ((0, 255, 0), "GREEN SCREEN - Pygame Test"),
    ((0, 0, 255), "BLUE SCREEN - Pygame Test"),
]

font = pygame.font.Font(None, 64)

for color, text in colors:
    screen.fill(color)
    text_surface = font.render(text, True, (255, 255, 255))
    rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text_surface, rect)
    pygame.display.update()
    time.sleep(1.5)

pygame.quit()
print("Test completed!")
