from enum import Enum, auto

class Offering(Enum):
    EVENT = 3
    COMMON = 3
    UNCOMMON = auto()
    RARE = auto()
    V_RARE = auto()
    U_RARE = auto()

if __name__ == '__main__':
    print(Offering.V_RARE.value)