# ili9486_waveshare_pico.py Customise for your hardware config and rename

# Released under the MIT License (MIT). See LICENSE.

# ILI9486 on Pi Pico Waveshare Pico-Res-Touch-LCD-3.5
# See DRIVERS.md for wiring details: the board uses an ILI9488 connected via
# a serial to parallel converter. This requires the ILI9486 driver.

from machine import Pin, SPI, freq
import gc
#freq(300_000_000) Optional overclock on Pico 2

from drivers.ili94xx.ili9486 import ILI9486 as SSD
SSD.COLOR_INVERT = 0xFFFF

pdc = Pin(8, Pin.OUT, value=0)
prst = Pin(15, Pin.OUT, value=1)
pcs = Pin(9, Pin.OUT, value=1)
spi = SPI(1, sck=Pin(10), mosi=Pin(11), miso=Pin(12), baudrate=24_000_000)
gc.collect()  # Precaution before instantiating framebuf
ssd = SSD(spi, pcs, pdc, prst, height=480, width=320, usd=True)  # mirror=True)
