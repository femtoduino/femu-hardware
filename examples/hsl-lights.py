import machine, time, math
from machine import Timer

# See https://gist.github.com/mathebox/e0805f72e7db3269ec22
# 
# Although the internal functions use 0.0 to 1.0, the HSVColors class uses 0 to 1000 to make arithmetic operations easier for us.
# This example illustrates how to cycle through Hue in an HSV color setup, and have an RGB LED display the color.
# 
class HSVColors:
    hue = 800
    sat = 1000
    vol = 500

    R = 27
    G = 4
    B = 5
    pRed = machine.Pin(R)
    pGreen = machine.Pin(G)
    pBlue = machine.Pin(B)

    pwmRed = machine.PWM(pRed, freq=1000)
    pwmGreen = machine.PWM(pGreen, freq=1000)
    pwmBlue = machine.PWM(pBlue, freq=1000)

    def rotate(self):
        
        # print("Hue is " + str(self.hue / 1000))
        r, g, b = self.hsl_to_rgb(self.hue / 1000, self.sat / 1000, self.vol / 1000)
        # print("calling setRGB with R:" + str(r) + ", G:" + str(g) + ", B:" + str(b))
        self.setRGB([r, g, b])

        self.hue += 10
        if (self.hue > 1000):
            self.hue = 0

        
        return
    def setRGB(self, rgb):
        r, g, b = rgb
        # print("R:" + str(r) + ", G:" + str(g) + ", B:" + str(b))
        self.pwmRed.duty(1023 - int( (r / 255) * 1023 ))
        self.pwmGreen.duty(1023 - int( (g / 255) * 1023 ))
        self.pwmBlue.duty(1023 - int( (b / 255) * 1023 ))
        return

    def clamp(self, value, min_value, max_value):
        return max(min_value, min(max_value, value))

    def saturate(self, value):
        return self.clamp(value, 0.0, 1.0)

    def hue_to_rgb(self, h):
        r = abs(h * 6.0 - 3.0) - 1.0
        g = 2.0 - abs(h * 6.0 - 2.0)
        b = 2.0 - abs(h * 6.0 - 4.0)
        return self.saturate(r), self.saturate(g), self.saturate(b)

    def hsl_to_rgb(self, h, s, l):
        r, g, b = self.hue_to_rgb(h)
        c = (1.0 - abs(2.0 * l - 1.0)) * s
        r = (r - 0.5) * c + l
        g = (g - 0.5) * c + l
        b = (b - 0.5) * c + l
        return round(r * 255), round(g * 255), round(b * 255)

global colors
colors = HSVColors()



tim = Timer(-1)
tim.init(period=100, mode=Timer.PERIODIC, callback=lambda t: colors.rotate())

while True:
    state = machine.disable_irq()
    machine.enable_irq(state)
    time.sleep_ms(100)
