import settings
from machine import Pin, PWM
from time import sleep_ms
from emitter import Emitter
from keyer import Keyer
from buzzer import Buzzer
from led import LED

key = Pin(settings.KEY_PIN, Pin.IN, Pin.PULL_UP)

tx_emitter = Emitter()

tx_keyer = Keyer(tx_emitter)

buzzer = Buzzer(PWM(Pin(settings.BUZZER_PIN)))
buzzer.frequency = settings.PITCH
tx_emitter.on("on", buzzer.on)
tx_emitter.on("off", buzzer.off)

led = LED(Pin("LED", Pin.OUT))
tx_emitter.on("on", led.on)
tx_emitter.on("off", led.off)

def loop():
    while True:
        if key.value() == 0:
            tx_keyer.on()
        else:
            tx_keyer.off()

        sleep_ms(10)

def main():
    while True:
        loop()

if __name__ == "__main__":
    main()
