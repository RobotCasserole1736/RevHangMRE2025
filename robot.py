import wpilib
from wpilib.simulation import stepTiming

class MyRobot(wpilib.TimedRobot):
    def disabledInit(self) -> None:
        stepTiming(0.2)
        exit(1736)