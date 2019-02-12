from enum import Enum, auto

class Item(Enum):
    EVENT = 3
    COMMON = 3
    UNCOMMON = auto()
    RARE = auto()
    V_RARE = auto()
    U_RARE = auto()

if __name__ == '__main__':
    print(Item.V_RARE.value)