import machine
import neopixel
import time

p = machine.Pin(2)
pixels = neopixel.NeoPixel(p, 28)

d = machine.Pin(0)
dots = neopixel.NeoPixel(p, 2)

color = [0,0,50]



bootanimation = [
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1]
]

for i in range(4):
    for l in range(7):
        pixels[i*7+l] = [0,0,0]


for i in range(4):
    for l in range(7):
        if bootanimation[i][l] == 1:
            pixels[i*7+l] = [0,0,50]
            time.sleep(0.1)
            pixels.write()