import abc

class PlayerAttack:
    def Attack(self):
        print("攻撃判定処理をします")

class AttackEffect:
    def ShowAttackEffect(self):
        print("攻撃エフェクトを表示します")

class AttackMotion:
    def PlayAttackMotion(self):
        print("攻撃モーションを再生します")

class PlayerAttackManager:
    def __init__(self, playerAttack, attackEffect, attackMotion):
        self.playerAttack = playerAttack
        self.attackEffect = attackEffect
        self.attackMotion = attackMotion

    #簡潔なインターフェースの実装
    def Attack(self):
        self.playerAttack.Attack()
        self.attackEffect.ShowAttackEffect()
        self.attackMotion.PlayAttackMotion()

if __name__ == "__main__":
    playerAttack = PlayerAttack()
    attackEffect = AttackEffect()
    attackMotion = AttackMotion()
    playerAttackManager = PlayerAttackManager(playerAttack, attackEffect, attackMotion)

    # 一連の処理を行うメソッド
    playerAttackManager.Attack()

    # サブシステムの個々のメソッドにもアクセス可能
    playerAttack.Attack()
    attackEffect.ShowAttackEffect()
    attackMotion.PlayAttackMotion()