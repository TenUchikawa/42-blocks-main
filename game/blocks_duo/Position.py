class Position:
    def __init__(self, x: int, y: int):
        self.__x = x - 1
        self.__y = y - 1

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y
