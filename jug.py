"""First steps with OOP"""


class Container:
    def __init__(self, name: str, volume: int, current_volume: int, pour_out: int = 100) -> None:
        self.__name = name
        self.__volume = volume
        self.current_volume = current_volume
        self.pour_out = pour_out

    def pour_out_liquid(self) -> int:
        if self.current_volume > 0:
            self.current_volume -= self.pour_out
            return self.pour_out
        else:
            print(f"{self.__name} empty")
            return 0

    def pour_liquid(self, volume: int) -> None:
        if self.current_volume + volume <= self.__volume:
            self.current_volume += volume
        else:
            print(f"{self.__name} full")

    def info(self):
        print(f'{self.__name} = {self.__volume}')


def main() -> None:
    jug = Container(name='Jag', volume=1000, current_volume=1000)
    glass = Container(name='Glass', volume=200, current_volume=0, pour_out=50)
    i = 0
    while i < 15:
        jug.info()
        glass.info()
        i += 1
        glass.pour_liquid(jug.pour_out_liquid())


main()
