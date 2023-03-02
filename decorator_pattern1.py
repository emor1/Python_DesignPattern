import abc

# コンポーネント役（スポンジのケーキ）
class IPlayerAction(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def Attack(self):
        pass

# コンポーネント役のインターフェイスを実装（具体的なスポンジケーキ）
class PlayerAction(IPlayerAction):

    def Attack(self):
        print("-"*10 + "\n"+"攻撃します")

# 装飾（デコレーション）役（クリームなどの飾り）
class PlayerActionAttr(metaclass=abc.ABCMeta):
    def __init__(self, playerAction):
        self.PlayerAction = playerAction

    @abc.abstractclassmethod
    def Attack():
        pass

# デコレーション役の実装１（具体的な飾り）
class Water(PlayerActionAttr):
    def Attack(self):
        self.PlayerAction.Attack()
        print("水属性の攻撃")

# デコレーション役の実装２（具体的な飾り）
class Poison(PlayerActionAttr):
    def Attack(self):
        self.PlayerAction.Attack()
        print("毒属性のダメージ")

class Magic(PlayerActionAttr):
    def Attack(self):
        self.PlayerAction.Attack()
        print("魔法攻撃")

if __name__=="__main__":
    playerAction = PlayerAction()
    playerAction.Attack()

    # PlayerAcgtionを装飾して新たな攻撃を追加
    playerAction = Poison(playerAction)
    playerAction.Attack()

    # # さらに水属性の追加
    playerAction = Water(playerAction)
    playerAction.Attack()

    # 追加
    playerAction = Magic(playerAction)
    playerAction.Attack()
