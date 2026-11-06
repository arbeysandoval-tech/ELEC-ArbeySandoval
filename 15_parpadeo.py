# puerto.write(..) //comunicacio con elpuerto de la esp32
#puerto.write(mensaje+"\n").emcode()) //encender el led "ENSENDER\n" es obligatorio fin de linea
#redline()leer linea por linea dato = purto.readline()
#decode(), dato= puerto.readline().decode() convierte los bytes en texto que phython pueda manejar con faciulidad
#preparar los datos
#dato = puerto,readline().decode().strip
from machine import pin 
from time import sleep

led=pin(18.pin.OUT)

while true:
    led.value(1)
    sleep(1)
    
    led.value(0)
    sleep(1)
    
    