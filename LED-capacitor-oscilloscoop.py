from machine import Pin, PWM
import time

# GPIO setup
LED_PIN1 = 22
LED_PIN2 = 26
SENSOR_PIN = 17

# Pins configureren
led1 = PWM(Pin(LED_PIN1))
led2 = PWM(Pin(LED_PIN2))
sensor = Pin(SENSOR_PIN, Pin.IN)

# PWM frequentie instellen
led1.freq(1000)
led2.freq(1000)

# Vertraging
delay = 0.05

def fade_led():
    """Demonstreert het laad/ontlaad effect van de capacitor"""
    try:
        while True:
            if sensor.value() == 1:
                # LEDs aan - capacitor laadt op
                led1.duty(1023)  # Max helderheid voor ESP32 (0-1023)
                led2.duty(1023)
                time.sleep(delay)
                
                # LEDs uit - capacitor ontlaadt
                led1.duty(0)
                led2.duty(0)
                time.sleep(delay)
    except KeyboardInterrupt:
        # Cleanup
        led1.deinit()
        led2.deinit()
        print("\nProgramma gestopt")

if __name__ == '__main__':
    fade_led()
