import abc

class ICommand(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Execute(self):
        pass

    @abc.abstractmethod
    def Undo(self):
        pass

# 具象クラス
class Light:
    def On(self):
        print("Light On")

    def Off(self):
        print("Light Off")

class LightOnCommand(ICommand):
    def __init__(self, light):
        self.light = light

    def Execute(self):
        self.light.On()

    def Undo(self):
        self.light.Off()

if __name__ == "__main__":
    lightCommand = LightOnCommand(Light())

    lightCommand.Execute()

    lightCommand.Undo()