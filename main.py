from gpiozero import Servo

from time import sleep

servo = Servo(14)
i = -1
while i <= 1:
    servo.min()
    sleep(1)
    servo.max()
    sleep(1)