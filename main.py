from gpiozero import LED

for i in range(1, 26):
    LED(i).on()
