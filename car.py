

class Car:


    def __init__(self, name, make, model):
        self._name = name
        self._make = make
        self._model = model

    def drive(self):
        return "vroom vroom!"

    def make(self):
        return self._make
    
    def model(self):
        return self._model
    
    def name(self):
        return self._name