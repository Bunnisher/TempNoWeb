from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime as time
from dht import DHT11, InvalidChecksum

WIDTH  = 128                                           
HEIGHT = 64                                             
 
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)       
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) 
print("I2C Configuration: "+str(i2c))                   
 
 
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  

while True:
    time.sleep(2)
    pin = Pin(13, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    t  = (sensor.temperature)
    h = (sensor.humidity)
    print("Temperature: {}".format(sensor.temperature))
    print("Humidity: {}".format(sensor.humidity))
    
    
    
    oled.fill(0)       
    
    # Add some text
    oled.text("Temp: ",10,10)
    oled.text(str(sensor.temperature),50,10)
    oled.text("*C",90,10)
    
    oled.text("Humi: ",10,30)
    oled.text(str(sensor.humidity),50,30)
    oled.text("%",90,30)
    
    time.sleep(.08)
    oled.show()
    time.sleep(2)
    