from abc import ABCMeta, abstractmethod

class Enemy(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def attackPlayer(self, player):
        pass

class EnviromentAsset(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        self.mobile = False

class Trap(Enemy, EnviromentAsset):
    def __init__(self):
        super(Trap, self).__init__()

    def attackPlayer(self, player):
        player.health -= 10

class Player(object):

    def __init__(self):
        self.health = 100


player = Player()
trap = Trap()

trap.attackPlayer(player)

print(player.health)