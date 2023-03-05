"""
    state_pattern1.pyのAttackの変更をPlayerAttack内で変更するもの、contextで切り替えを行う形式に変更
"""

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

class PlayerEnhanceState(AbstractPlayerState):
    def __init__(self, playerAttack):
        self.PlayerAttack = playerAttack

    def Attack(self):
        print("２倍の攻撃！")
        # self.PlayerAttack.SetState(self.PlayerAttack.ParalysisState if random.uniform(0, 2)>=0.5 else self.PlayerAttack.NormalState)


class PlayerParalysisState(AbstractPlayerState):
    def __init__(self, playerAttack):
        self.PlayerAttack = playerAttack

    def Attack(self):
        print("痺れて攻撃ができない")
        # self.PlayerAttack.SetState(self.PlayerAttack.NormalState)


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

    # 全ての関数のifを書き換えなくても、ここで集約できる
    def ChangeByTxt(self, txt):
        if txt == "通常":
            self.SetState(self.NormalState)
        elif txt == "アップ":
            self.SetState(self.EnhanceState)
        else:
            self.SetState(self.ParalysisState)

if __name__ == "__main__":
    _playerAttack = PlayerAttack()
    _playerAttack.Attack()

    # 切り替え
    _playerAttack.ChangeByTxt("猫")
    _playerAttack.Attack()

    # 切り替え
    _playerAttack.ChangeByTxt("アップ")
    _playerAttack.Attack()
