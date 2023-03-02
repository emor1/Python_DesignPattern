import abc


"""
インターフェース実装参考：https://zenn.dev/plhr7/articles/36ddd240ccbb97
今回のコードはテックスコア参考：https://www.techscore.com/tech/DesignPattern/Strategy
"""
class Comparator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def compare(self, h1, h2):
        pass

class Human:
    def __init__(self, name, height=1, weight=1, age=1):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age

class AgeCompare(Comparator):
    def compare(self, h1, h2):
        if(h1.age > h2.age):
            return 1
        elif(h1.age == h2.age):
            return 0
        else:
            return -1

class HeightComparator(Comparator):
    def compare(self, h1, h2):
        if(h1.height > h2.height):
            return 1
        elif(h1.height == h2.height):
            return 0
        else:
            return -1

class MyClass:
    def __init__(self, comp):
        self.comp = comp

    def compare(self,h1, h2):
        return self.comp.compare(h1, h2)

    def SetComp(self, comp):
        self.comp = comp

if __name__=="__main__":
    h1 = Human(name="neko",height=150,weight=80,age=36)
    h2 = Human(name="inu",height=170,weight=70,age=26)

    age = AgeCompare()
    height = HeightComparator()

    class1 = MyClass(age)
    print(class1.comp.compare(h1, h2))

    class1.SetComp(height)
    print(class1.comp.compare(h1, h2))
