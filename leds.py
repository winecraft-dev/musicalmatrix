import sys
from neopixel import Adafruit_NeoPixel, Color

CHANNELS = 15
VALUES = 10

CHANNEL_COLORS = [None] * 15

# LED strip configuration:
LED_COUNT = CHANNELS * VALUES  # Number of LED pixels.
LED_PIN = 12  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5  # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False # True to invert the signal (when using NPN transistor level shift)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def generate_colors():
    for i in range(256 * 5):
        for j in range(CHANNELS):
            CHANNEL_COLORS[j] = wheel((int(j * 256 / CHANNELS) + i) & 255)

def get_strip():
    strip = Adafruit_NeoPixel(
        LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

    strip.begin()

    for i in range(0, strip.numPixels(), 1):
        strip.setPixelColor(i, Color(0, 0, 0))

    strip.setBrightness(100)

    return strip

def fill_channel(strip, channel, value, volume):
    value = float(value) / 1000 * VALUES

    for row in range(0, VALUES, 1):
        pixel = 0
        if row % 2 == 0:
            pixel = (row + 1) * CHANNELS - channel - 1
        else:
            pixel = row * CHANNELS + channel

        if value >= 1:
            strip.setPixelColor(pixel, CHANNEL_COLORS[channel])
            value -= 1
        else:
            strip.setPixelColor(pixel, Color(0, 0, 0))
            value = 0


def handle_stdin(strip):
    while True:
        try:
            levels = sys.stdin.readline()[:-2].split(";")[:-1]
            levels = map(int, levels)

            volume = sum(levels) / CHANNELS
            volume = int(float(volume) / 1000 * 255)

            for i in range(0, CHANNELS, 1):
                fill_channel(strip, i, levels[i], volume)

            strip.setBrightness(volume)
            strip.show()
        except Exception as e:
            print e


if __name__ == '__main__':
    generate_colors()
    handle_stdin(get_strip())
