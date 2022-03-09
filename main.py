from signal import pause

from gpiozero import LED
led = LED(21)
led.blink()

pause()