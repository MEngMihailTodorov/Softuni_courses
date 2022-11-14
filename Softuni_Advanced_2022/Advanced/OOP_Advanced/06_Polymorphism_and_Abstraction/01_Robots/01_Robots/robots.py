class Robot:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def sensors_amount():
        return 1


class MedicalRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 6


class ChefRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 4


class WarRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 12


class WarKingRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 20


def print_number_of_robot_sensors(robot: Robot):
    print(robot.sensors_amount())


basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')
misho = WarKingRobot('Misho')

print_number_of_robot_sensors(basic_robot)
print_number_of_robot_sensors(da_vinci)
print_number_of_robot_sensors(moley)
print_number_of_robot_sensors(griffin)
print_number_of_robot_sensors(misho)