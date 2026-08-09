class Reflector:
    def __init__(self,wiring,notch):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        self.notch = notch
    def reflect(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal