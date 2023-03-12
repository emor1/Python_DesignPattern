"""
Adapterパターン
参考：https://www.hanachiru-blog.com/entry/2021/03/18/120000
移譲を使ったパターン
"""
import abc

# 既に使われているようなクラス(Adaptee)
class Adaptee:
    def methodA(self):
        print("Method A")

    def methodB(self):
        print("Method B")

# 目的とするインターフェース
class Target(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def TargetMethod1(self):
        pass

    @abc.abstractclassmethod
    def TargetMethod2(self):
        pass

# Adapteeを目的のインターフェイスに変換する
class Adapter(Target):
    def __init__(self):
        self.adaptee = Adaptee()

    def TargetMethod1(self):
        self.adaptee.methodA()

    def TargetMethod2(self):
        self.adaptee.methodB()

# Client
if __name__=="__main__":
    adapter = Adapter()

    adapter.TargetMethod1()
    adapter.TargetMethod2()
