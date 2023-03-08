"""参考：https://qiita.com/ttsubo/items/0860e31c392aa3b91ed5
builderパターンの実装
"""
import abc

# builderのインターフェース
class AbstractAttack(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def firstAttack(self):
        pass

    @abc.abstractclassmethod
    def secondAttack(self):
        pass

    @abc.abstractclassmethod
    def thirdAttack(self):
        pass

# 具体的なbuilder
class MagicianAttacks(AbstractAttack):
    def firstAttack(self):
        print("一つ目の攻撃：水魔法")

    def secondAttack(self):
        print("二つ目の攻撃：火魔法")

    def thirdAttack(self):
        print("三つ目の攻撃：氷魔法")

class HeroAttack(AbstractAttack):
    def firstAttack(self):
        print("一つ目の攻撃：剣の攻撃")

    def secondAttack(self):
        print("二つ目の攻撃：弓の攻撃")

    def thirdAttack(self):
        print("三つ目の攻撃：タコ殴り！")

class Director(object):
    def __init__(self, builder):
        self.builder = builder

    def Attack(self):
        self.builder.firstAttack()
        self.builder.secondAttack()
        self.builder.thirdAttack()

def PlayerAttack(player):
    if player == "magician":
        director = Director(MagicianAttacks())
    else:
        director = Director(HeroAttack())
    director.Attack()

if __name__ == "__main__":
    PlayerAttack("magician")
    print("-"*30)
    PlayerAttack("Hero")