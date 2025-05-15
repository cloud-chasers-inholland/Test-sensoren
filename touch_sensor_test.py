from gpiozero import LineSensor, LED
from signal import pause

led = LED(17)
sensor = LineSensor(4)

sensor.when_line = lambda: led.on()
sensor.when_no_line = lambda: led.off()
pause()

print("test")
