from gpiozero import Servo

from time import sleep

servo = Servo(14)
i = -1
while True:
    servo.mid()