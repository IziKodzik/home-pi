from gpiozero import Servo

from time import sleep

servo = Servo(14)
i = -1
while i <= 1:
    servo.value = i
    i += 0.01
    sleep(0.01)
