import wpilib
from rev import SparkMax

class MyRobot(wpilib.TimedRobot):
    def __init__(self):
        wpilib._wpilib.TimedRobot.__init__(self)
        self.ctrl = SparkMax(0, SparkMax.MotorType.kBrushless)
