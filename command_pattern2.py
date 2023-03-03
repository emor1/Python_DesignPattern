"""
参考：https://ao-log.hatenablog.com/entry/2013/11/25/223043
Commandパターン
"""

import abc

class Command(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Execute(self):
        pass

class CompositeCommand(Command):
    def __init__(self):
        self.cmd_lst = []

    def appendCommand(self, cmd):
        self.cmd_lst.append(cmd)

    def Execute(self):
        for cmd in self.cmd_lst:
            cmd.Execute()

class SomethingCommand1(Command):
    def __init__(self, txt="This is Cmd1"):
        self.txt = txt

    def Execute(self):
        print(self.txt)

class SomethingCommand2(Command):
    def __init__(self, txt="This is Cmd2"):
        self.txt = txt

    def Execute(self):
        print(self.txt)

if __name__ == "__main__":

    # コマンドのインスタンス作成
    compositeCmd = CompositeCommand()

    # コマンドの中身の組み立て
    compositeCmd.appendCommand(SomethingCommand1())
    compositeCmd.appendCommand(SomethingCommand1())
    compositeCmd.appendCommand(SomethingCommand2())

    # 組み立てたコマンドの実行
    compositeCmd.Execute()