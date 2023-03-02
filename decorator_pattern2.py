"""
TECH SCOREのサンプルをPythonで実装
https://www.techscore.com/tech/DesignPattern/Decorator
"""

import abc

# コンポーネント役：共通インターフェース
class IceCream(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def getName(self):
        pass

    @abc.abstractclassmethod
    def howSweet(self):
        pass

# インターフェースを持つクラス
class VanillaIceCream(IceCream):
    def getName(self):
        return "バニラアイスクリーム"

    def howSweet(self):
        return "バニラ味"

class GreenTeaIceCream(IceCream):
    def getName(self):
        return "抹茶アイスクリーム"

    def howSweet(self):
        return "抹茶味"

class CashewNutsToppingIceCream(IceCream):
    def __init__(self, ice=None):
        self.ice = ice

    def getName(self):
        name = "カシューナッツ"
        name += self.ice.getName()
        return name

    def howSweet(self):
        return self.ice.howSweet()


if __name__ == "__main__":
    ice = []
    ice.append(CashewNutsToppingIceCream(VanillaIceCream()))
    ice.append(CashewNutsToppingIceCream(GreenTeaIceCream()))
    ice.append(GreenTeaIceCream())

    [print(i.getName()) for i in ice]
    [print(i.howSweet()) for i in ice]
