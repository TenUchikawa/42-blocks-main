from enum import Enum


class BlockRotation(Enum):
    Rotation_0 = 0
    Rotation_1 = 1
    Rotation_2 = 2
    Rotation_3 = 3
    Rotation_4 = 4
    Rotation_5 = 5
    Rotation_6 = 6
    Rotation_7 = 7

    def rotation_count(self) -> int:
        return (self.value & 0x06) >> 1

    def reversed(self) -> bool:
        return self.value & 0x01 == 0x01
