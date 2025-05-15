from gpiozero import Servo

servo_1 = Servo(11)
servo_2 = Servo(17)

while True:
    getal = float(input("give value between 1 and -1"))
    servo_1.value = getal
    servo_2.value = getal