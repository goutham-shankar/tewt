import machine
import time

led = machine.Pin(2, machine.Pin.OUT)  # GPIO 2 (Built-in LED on some ESP32 boards)

while True:
    led.value(1)  # Turn LED ON
    time.sleep(10)  # Wait 1 second
    led.value(0)  # Turn LED OFF
    time.sleep(10)  # Wait 1 second

