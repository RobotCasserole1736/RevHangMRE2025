import wpilib

_instances = {}

class Singleton(type):
    def __call__(cls, *args, **kwargs):
        if cls not in _instances:
            _instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return _instances[cls]

def destroyAllSingletonInstances():
    global _instances
    _instances = {}


class SensorClass(metaclass=Singleton):
    def __init__(self):
        self.testDc = wpilib.DutyCycle(wpilib.DigitalInput(1))


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.testSen = SensorClass()

    def robotPeriodic(self):
        print(self.testSen.testDc.getFrequency())

    def endCompetition(self):
        destroyAllSingletonInstances()
        return super().endCompetition()
