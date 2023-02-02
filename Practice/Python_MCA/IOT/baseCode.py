import RPI.GPIO as GPIO
import time

LED_PIN = 4
GPIO.setwarnigs(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

while 1:
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(2)
