#!/usr/bin/env python3
"""
Example code to emulate an SH1116 OLED display with rotary encoder and button simulation using luma.emulator.
"""

import pygame
from luma.emulator.device import pygame as luma_pygame
from PIL import Image, ImageDraw

# Create emulator device for SH1116 (128x64)
device = luma_pygame(width=128, height=64, rotate=0, mode="1", transform="identity", scale=2)

# Initialize variables for simulation
rotary_position = 0
button_presses = 0
confirm_presses = 0
back_presses = 0

# Main loop
running = True
while running:
    # Create image and draw
    image = Image.new('1', (128, 64), 0)  # 1-bit image
    draw = ImageDraw.Draw(image)

    # Draw some text
    draw.text((10, 5), "Estardyn 1.3\"", fill=1)
    draw.text((10, 15), f"Rotary: {rotary_position}", fill=1)
    draw.text((10, 25), f"Button: {button_presses}", fill=1)
    draw.text((10, 35), f"Confirm: {confirm_presses}", fill=1)
    draw.text((10, 45), f"Back: {back_presses}", fill=1)

    # Display the image
    device.display(image)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rotary_position -= 1
            elif event.key == pygame.K_RIGHT:
                rotary_position += 1
            elif event.key == pygame.K_SPACE:
                button_presses += 1
            elif event.key == pygame.K_c:
                confirm_presses += 1
            elif event.key == pygame.K_b:
                back_presses += 1
            elif event.key == pygame.K_ESCAPE:
                running = False

# Quit pygame
pygame.quit()
