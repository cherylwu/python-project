class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name,age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f"{self.name} is sitting now.")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} is rolling over.")

my_dog = Dog('while', 6)
your_dog = Dog('Lucy', 3)

print(f"\nMy dog's name is {my_dog.name}.")
print(f"\nMy dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"\nYour dog is {your_dog.age} years old.")
your_dog.sit()

