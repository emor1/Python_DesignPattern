import abc


"""
インターフェース実装参考：https://zenn.dev/plhr7/articles/36ddd240ccbb97
"""
class IAttack(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Attack(self):
        pass

class Hit(IAttack):
    def Attack(self):
        print("打撃攻撃")

class Slash(IAttack):
    def Attack(self):
        print("斬撃攻撃")

class Magic(IAttack):
    def Attack(self):
        print("魔法攻撃")


class PlayerAttack:
    def __init__(self,attack):
        self._attack = attack

    # プレイヤーは攻撃するだけ、詳細は他のクラスが管理
    def Attack(self):
        self._attack.Attack()

    def SetAttack(self,attack):
        self._attack = attack

if __name__=="__main__":
    hit = Hit()
    slash = Slash()
    magic = Magic()

    # 初期は打撃攻撃
    playerAttack = PlayerAttack(hit)
    playerAttack.Attack()

    # 斬撃攻撃に切り替え
    playerAttack.SetAttack(slash)
    playerAttack.Attack()

    # 魔法攻撃に切り替える
    playerAttack.SetAttack(magic)
    playerAttack.Attack()