class Container:
    name: str = 'name'
    _volume: int = 0
    _current_volume: int = 0
    pour_out: int = 0

    def pour_out_liquid(self) -> int:
        if self._current_volume > 0:
            self._current_volume -= self.pour_out
            return self.pour_out
        else:
            print(f"{self.name} empty")
            return 0

    def pour_liquid(self, volume: int) -> None:
        if self._current_volume + volume <= self._volume:
            self._current_volume += volume
        else:
            print(f"{self.name} full")

    def info(self):
        print(f'{self.name} = {self._volume}')


class Jug(Container):
    name: str = 'Jag'
    _volume: int = 1000
    _current_volume: int = 600
    pour_out: int = 100


class Glass(Container):
    name: str = 'Glass'
    _volume: int = 300
    _current_volume: int = 0
    pour_out: int = 50


def main() -> None:
    jug = Jug()
    glass = Glass()
    i = 0
    while i < 15:
        jug.info()
        glass.info()
        i += 1
        glass.pour_liquid(jug.pour_out_liquid())


main()
