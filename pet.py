class Pet:
    def __init__(self, name):
        self._name = name
    def name(self):
        return self._name
    def speak(self):
        return "I'm a Pet"
