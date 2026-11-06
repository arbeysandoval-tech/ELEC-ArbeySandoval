from machine import pin
import sys

led = pin(18,OUT)

while True:
    mensaje = sys.stdin.readline().strip()

    if mensaje == "ENCENDER":
        led.value(1)

    if mensaje =="APAGAR":
        led.value(0)
        
        
    