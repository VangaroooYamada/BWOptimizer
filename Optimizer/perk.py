from enum import Enum, auto

class Perk(Enum):
    UNCOMMON = 4
    RARE = auto()
    V_RARE = auto()

if __name__ == '__main__':
    print(Perk.V_RARE.value)