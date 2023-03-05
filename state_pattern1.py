import abc
import random

class AbstractPlayerState(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def __init__(self):
        self.PlayerAttack

    @abc.abstractmethod
    def Attack(self):
        print("攻撃方法が定義されていません")


class PlayerNormalState(AbstractPlayerState):
    def __init__(self, playerAttack):
        self.PlayerAttack = playerAttack

    def Attack(self):
        print("通常攻撃！！")
        if(random.uniform(0, 5)>= 2):
            self.PlayerAttack.SetState(self.PlayerAttack.EnhanceState)

class PlayerEnhanceState(AbstractPlayerState):
    def __init__(self, playerAttack):
        self.PlayerAttack = playerAttack

    def Attack(self):
        print("２倍の攻撃！")
        self.PlayerAttack.SetState(self.PlayerAttack.ParalysisState if random.uniform(0, 2)>=0.5 else self.PlayerAttack.NormalState)


class PlayerParalysisState(AbstractPlayerState):
    def __init__(self, playerAttack):
        self.PlayerAttack = playerAttack

    def Attack(self):
        print("痺れて攻撃ができない")
        self.PlayerAttack.SetState(self.PlayerAttack.NormalState)


class PlayerAttack:
    def __init__(self):
        self.NormalState = PlayerNormalState(self)
        self.EnhanceState = PlayerEnhanceState(self)
        self.ParalysisState = PlayerParalysisState(self)
        self._currentState = self.NormalState

    def Attack(self):
        self._currentState.Attack()

    def SetState(self, state):
        self._currentState = state

if __name__ == "__main__":
    _playerAttack = PlayerAttack()
    for i in range(10):
        _playerAttack.Attack()

