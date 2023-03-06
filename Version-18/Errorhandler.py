import machine
import neopixel
import time

p = machine.Pin(2)
pixels = neopixel.NeoPixel(p, 28)

d = machine.Pin(0)
dots = neopixel.NeoPixel(p, 2)

erranimation = [
  [0, 0, 0, 0, 0, 0, 0],
  [0, 1, 1, 0, 0, 0, 1],
  [0, 1, 1, 0, 0, 0, 1],
  [0, 1, 1, 1, 0, 1, 1]
]

color = [50, 0, 0]
offcolor = [0, 0, 0]
dots[0] = color
dots[1] = color
for i in range(4):
    for l in range(7):
        if erranimation[i][l] == 1:
            pixels[i*7+l] = color
        else:
            pixels[i*7+l] = offcolor
pixels.write()