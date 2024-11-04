from machine import Pin
import time

# GPIO setup
SENSOR_PIN = 17
LED_PIN = 2  # Ingebouwde LED op de meeste ESP32 boards

# Pins configureren
sensor = Pin(SENSOR_PIN, Pin.IN)
led = Pin(LED_PIN, Pin.OUT)

def read_QRD1114sensor():
    # Lees sensor waarde
    return sensor.value()

def main():
    try:
        while True:
            sensor_waarde = read_QRD1114sensor()
            if sensor_waarde == 0:
                print("Object gedetecteerd!")
                led.on()
            else:
                print("Geen object.")
                led.off()
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nProgramma gestopt")

if __name__ == "__main__":
    main()
