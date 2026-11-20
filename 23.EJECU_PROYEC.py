import serial
from time import sleep


puerto = serial.Serial("COM6", 115200, timeout=1)

sleep(3)

puerto.reset_input_buffer()


while True:

    mensaje = puerto.readline().decode().strip()

    if mensaje:
        print(mensaje)