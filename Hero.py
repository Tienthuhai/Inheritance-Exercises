class Hero:
    def __init__(self, username, level):
        self.username = username
        self.level = level

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{self.username} of type {class_name} has level {self.level}"

class Elf(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)

class Wizard(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)

class Knight(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)

class Museelf(Elf):
    def __init__(self, username, level):
        super().__init__(username, level)

class DarkWizard(Wizard):
    def __init__(self, username, level):
        super().__init__(username, level)

class SoulMaster(DarkWizard):
    def __init__(self, username, level):
        super().__init__(username, level)

class DarkWizard(Knight):
    def __init__(self, username, level):
        super().__init__(username, level)

class BladeKnight(DarkWizard):
    def __init__(self, username, level):
        super().__init__(username, level)

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
