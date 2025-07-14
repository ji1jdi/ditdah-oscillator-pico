class Keyer:
    def __init__(self, emitter):
        self._emitter = emitter
        self._keying = False

    def on(self):
        if self._keying:
            return

        print("on")
        self._keying = True
        self._emitter.emit("on")

    def off(self):
        if not self._keying:
            return

        print("off")
        self._keying = False
        self._emitter.emit("off")
