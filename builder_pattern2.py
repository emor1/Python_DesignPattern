"""
TECHSCOREを参考に実装
builderパターン：https://www.techscore.com/tech/DesignPattern/Builder

"""
import abc

class SaltWater:
    def __init__(self, salt, water):
        self.salt = salt
        self.water = water

class Builder(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def addSolute(self, saltAmount):
        pass

    @abc.abstractclassmethod
    def addSolvent(self, waterAmount):
        pass

    @abc.abstractclassmethod
    def abandonSolution(self, saltWaterAmount):
        pass

    @abc.abstractclassmethod
    def getResult(self):
        pass


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.addSolvent(100)
        self.builder.addSolute(40)
        self.builder.abandonSolution(70)
        self.builder.addSolvent(100)
        self.builder.addSolute(15)

class SaltWaterBuilder(Builder):
    def __init__(self):
        self.saltWater = SaltWater(0, 0)

    def addSolute(self, saltAmount):
        self.saltWater.salt += saltAmount

    def addSolvent(self, waterAmount):
        self.saltWater.waterAmount = waterAmount

    def abandonSolution(self, saltWaterAmount):
        saltDelta = saltWaterAmount * (self.saltWater.salt / (self.saltWater.salt + self.saltWater.water))
        waterDelta = saltWaterAmount * (self.saltWater.water / (self.saltWater.salt + self.saltWater.water))
        self.saltWater.salt -=saltDelta
        self.saltWater.water -= waterDelta

    def getResult(self):
        return self.saltWater

if __name__ == "__main__":
    builder = SaltWaterBuilder()
    director = Director(builder)
    director.construct()
    saltwater = builder.getResult()
