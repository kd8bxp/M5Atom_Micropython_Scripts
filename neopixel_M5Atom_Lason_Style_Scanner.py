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

delay = .06

for i in range(0, 5):
	strip[i] = (red_light)
strip.write()
sleep(.1)

for i in range(0, 5):
	strip[i] = (red_med)
strip.write()
sleep(.1)

for i in range(0, 5):
	strip[i] = (red)
strip.write()
sleep(.1)

for i in range(0, 5):
	strip[i] = (red_med)
strip.write()
sleep(.1)

for i in range(0, 5):
	strip[i] = (red_light)
strip.write()
sleep(.1)

while True:
	strip[0] = (red)
	strip[1] = (red_med)
	strip[2] = (red_light)
	strip[3] = (off)
	strip[4] = (off)
	strip.write()
	sleep(delay)
	strip[0] = (red_med)
	strip[1] = (red)
	strip[2] = (red_med)
	strip[3] = (red_light)
	strip[4] = (off)
	strip.write()
	sleep(delay)
	strip[0] = (red_light)
	strip[1] = (red_med)
	strip[2] = (red)
	strip[3] = (red_med)
	strip[4] = (red_light)
	strip.write()
	sleep(delay)
	strip[0] = (off)
	strip[1] = (red_light)
	strip[2] = (red_med)
	strip[3] = (red)
	strip[4] = (red_med)
	strip.write()
	sleep(delay)
	strip[0] = (off)
	strip[1] = (off)
	strip[2] = (red_light)
	strip[3] = (red_med)
	strip[4] = (red)
	strip.write()
	sleep(delay)
	strip[4] = (red_med)
	strip[3] = (red)
	strip[2] = (red_med)
	strip[1] = (red_light)
	strip[0] = (off)
	strip.write()
	sleep(delay)
	strip[4] = (red_light)
	strip[3] = (red_med)
	strip[2] = (red)
	strip[1] = (red_med)
	strip[0] = (red_light)
	strip.write()
	sleep(delay)
	strip[4] = (off)
	strip[3] = (red_light)
	strip[2] = (red_med)
	strip[1] = (red)
	strip[0] = (red_med)
	strip.write()
	sleep(delay)
	strip[4] = (off)
	strip[3] = (off)
	strip[2] = (red_light)
	strip[1] = (red_med)
	strip[0] = (red)
	strip.write()
	sleep(delay)
