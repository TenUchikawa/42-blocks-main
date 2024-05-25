from enum import IntEnum, auto


class FinishedReason(IntEnum):
    illegal_placement = auto()
    normal = auto()

