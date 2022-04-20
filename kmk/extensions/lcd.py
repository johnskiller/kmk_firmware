# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

from board import *
from kmk.extensions import Extension 
import busio
import terminalio
import displayio
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
from adafruit_st7735r import ST7735R
import adafruit_imageload
import microcontroller
import time

class LCD(Extension):
    def __init__(self):

        displayio.release_displays()  # Release any resources

        self.spi = busio.SPI(clock=GP10, MOSI=GP11)  # SPI0BUS PIN
        #spi = busio.SPI(clock=GP2, MOSI=GP3)  # SPI0BUS PIN
        self.display_bus = displayio.FourWire(
            self.spi, command=GP8, chip_select=GP9, reset=GP12) # other PIN
            #spi, command=GP7, chip_select=GP5, reset=GP6) # other PIN
        self.display = ST7735R(self.display_bus, width=132, height=162,rotation=180,invert=True)
        self.splash = displayio.Group()  # Make the display context
        self.display.show(self.splash)
# show bmp
# Setup the file as the bitmap data source
#bitmap = displayio.OnDiskBitmap("/purple.bmp")

# Create a TileGrid to hold the bitmap
#tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)

        bitmap, palette = adafruit_imageload.load("/lcd.bmp",
                                          bitmap=displayio.Bitmap, palette=displayio.Palette)
        tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
# Create a Group to hold the TileGrid
        group = displayio.Group()

# Add the TileGrid to the Group
        group.append(tile_grid)

# Add the Group to the Display
#display.show(group)
        self.splash.append(group)

# Draw a label=text
        text_group = displayio.Group(scale=2, x=40, y=120)
        text = "L0"
        font = bitmap_font.load_font("/LeagueSpartan-Bold-16.bdf")
        label.anchor_point = (0.0, 0.0)
        label.anchored_position = (0, 0)
        text_area = label.Label(font, text=text, color=0xFFFFFF)
        text_group.append(text_area)  # Subgroup for text
        self.splash.append(text_group)

        self.textarea = text_area
        self.layer=0

    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, sandbox):
        return

    def before_matrix_scan(self, sandbox):
        return

    def after_matrix_scan(self, sandbox):
        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, keyboard):
        layer = keyboard.active_layers[0]
        if self.layer != layer:
            text = f'L{layer}'
            self.textarea.text = text
            self.layer = layer
        return

    def on_powersave_enable(self, sandbox):
        return

    def on_powersave_disable(self, sandbox):
        return
