from time import sleep
import machine, neopixel

NUMBER_PIXELS = 25
STATE_MACHINE = 0
LED_PIN = 27

strip = neopixel.NeoPixel(machine.Pin(LED_PIN), NUMBER_PIXELS) #(NUMBER_PIXELS, STATE_MACHINE, LED_PIN, "GRB")


# Color RGB values
red = (255, 0, 0)
red_med = (32, 0, 0)
red_light = (8, 0, 0)
off = (0,0,0)

delay = .15
while True:
    for i in range(2, NUMBER_PIXELS-2):
        strip[i-2] = (red_light)
        strip[i-1] = (red_med)
        strip[i] = (red)
        strip[i+1] = (red_med)
        strip[i+2] = (red_light)
        if i > 0: strip[i-3] = (off)
        strip.write()
        sleep(delay)
    for i in range(NUMBER_PIXELS-4, 1, -1):
        if i < NUMBER_PIXELS-2: strip[i+3] = (off)
        strip[i-2] = (red_light)
        strip[i-1] = (red_med)
        strip[i] = (red)
        strip[i+1] = (red_med)
        strip[i+2] = (red_light)
        strip.write()
        sleep(delay)
