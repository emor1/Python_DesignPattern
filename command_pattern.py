"""
参考：https://www.techscore.com/tech/DesignPattern/Command
Commandパターン
"""

import abc

class Beaker:
    def __init__(self, water=0, salt=0):
        self.water = water
        self.salt = salt
        self.melted = True # 食塩が全て溶けたか
        self.mix()

    # 塩を加えるメソッド
    def addSalt(self, salt):
        self.salt += salt

    # 水を加えるメソッド
    def addWater(self, water):
        self.water += water

    # かき混ぜるメソッド
    def mix(self):
        if((self.salt / (self.salt + self.water))*100 < 26.4):
            self.melted = True
        else:
            self.melted = False

    def getSalt(self):
        return self.salt

    def getWater(self):
        return self.water

    def isMelted(self):
        return self.melted

    def note(self):
        print(f"水：{self.water}g")
        print(f"食塩：{self.salt}g")
        print(f"濃度：{self.salt/(self.water+self.salt)*100}%")

class Command(metaclass=abc.ABCMeta):
    def setBeaker(self, beaker):
        self.beaker = beaker
        # print(self.beaker.water)

    @abc.abstractmethod
    def Execute(self):
        pass

class AddSaltCommand(Command):
    def Execute(self):
        while(self.beaker.isMelted()):
            self.beaker.addSalt(1)
            self.beaker.mix()
        print("食塩を1gずつ加える実験")
        self.beaker.note()


#水を10gずつ加える実験のコマンドクラス
class AddWaterCommand(Command):
    def Execute(self):
        while(not self.beaker.isMelted):
            self.beaker.addWater(10)
            self.beaker.mix()
        print("水を10gずつ加える実験")
        self.beaker.note()

# 食塩水を作る実験のコマンドクラス
class MakeSaltWaterCommand(Command):
    def Execute(self):
        self.beaker.mix()
        print("食塩水を作る実験")
        self.beaker.note()

# 実験する生徒
class Student:
    def __init__(self):
        addSalt = AddSaltCommand()
        addWater = AddWaterCommand()
        makeSaltWater = MakeSaltWaterCommand()
        # 実験セットを実験内容にセットする
        addSalt.setBeaker(Beaker(100,0))        # 水100gの入ったビーカーをセットする
        addWater.setBeaker(Beaker(0,10))        # 食塩10gの入ったビーカーをセットする
        makeSaltWater.setBeaker(Beaker(90,10))

        # 実験を行う
        addSalt.Execute()
        addWater.Execute()
        makeSaltWater.Execute()


if __name__ == "__main__":
    students = Student()